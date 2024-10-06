# MIT License
#
# Copyright (c) 2023 LandInsightLab 
# Author: Rui Shi
# Date: July 2023
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os, sys
from PySide6 import QtWidgets
from PySide6.QtWidgets import QWidget, QFileDialog, QTableWidgetItem, QHeaderView, QMessageBox, QApplication
from PySide6.QtCore import QSettings, Qt, QTimer, QThread, Signal
from PySide6 import QtGui
from PSSA_ui import Ui_PSSA

from libs.PatchStatistics import PatchStatistics, ErrorCode
from libs.CheckTifDimensions import CheckTifDimensions

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from scipy.optimize import curve_fit, differential_evolution
from scipy.stats import lognorm, powerlaw
from gaussFigure_ui import Ui_GaussFigureWidget
from libs import RingAndArea
from gaussFigure import GaussFigure

buffer_spacing = 10
# Define a mapping from ErrorCode values to error messages
ERROR_CODE_MESSAGES = {
    0: "Success",
    -1: "Invalid GDAL Dataset Pointer",
    -2: "Failed to Get Raster Band",
    -3: "Failed to Read Raster Data",
    -4: "File Open Failed",
    -5: "Memory Allocation Failed",
    -6: "Create Output Dataset Failed",
    -7: "Exception Caught",
    -8: "Failed to Write Raster Data"
}

def r2(y_true, y_pred):
    residuals = y_true - y_pred
    ss_res = np.sum(residuals ** 2)
    ss_tot = np.sum((y_true - np.mean(y_true)) ** 2)
    return 1 - (ss_res / ss_tot)

def gaussian(x, amp, mu, sigma):
    return amp * np.exp(- (x - mu)**2 / (2 * sigma**2))

# 数据平滑函数
def smooth_data(y_data, window_size=3):
    return np.convolve(y_data, np.ones(window_size)/window_size, mode='valid')


def get_error_message(error_code):
    # Convert ErrorCode enum to integer and get the corresponding error message
    error_code_int = int(error_code)  # Ensure that the ErrorCode can be cast to int
    return ERROR_CODE_MESSAGES.get(error_code_int, "Unknown Error")


class WorkerThread(QThread):
    error_message = Signal(str)
    send_message = Signal(str)
    plot_ready = Signal(Figure)  # Signal to emit the matplotlib Figure
    show_result_lognormal_mean = Signal(str)
    show_result_lognormal_stddev = Signal(str)
    show_result_power_constant = Signal(str)
    show_result_power_power = Signal(str)
    
    def __init__(self, file_paths, output_folder, out, neighbor_type, center, center_path):
        super().__init__()
        self.file_paths = file_paths
        self.output_folder = output_folder
        self.out = out
        self.center = center
        self.center_path = center_path
        self.neighbor_type = neighbor_type

    def run(self):
        try:
            self.send_message.emit("Creating PatchStatistics instance...")
            patch_statistics = PatchStatistics(self.file_paths, self.neighbor_type)

            self.send_message.emit("Calculating patch properties...")
            error_code = patch_statistics.calculate_patch_properties()
            if (error_code != ErrorCode.Success):
                raise RuntimeError(get_error_message(error_code))
            patches = patch_statistics.getPatches()
            self.send_message.emit("Patch properties calculated successfully.")

            if (self.out):
                self.send_message.emit("Writing labels to TIFF file...")
                error_code = patch_statistics.writeLabelsToTif(self.output_folder)
                if (error_code != ErrorCode.Success):
                    raise RuntimeError(get_error_message(error_code))
                self.write_patches_to_csv(patches)
                self.send_message.emit("Labels written to TIFF file and CSV file created.")

            self.send_message.emit("Calculating lognormal distribution parameters...")
            self.calculate_lognormal_distribution_parameters(patches)

            self.send_message.emit("Calculating power law distribution parameters...")
            self.calculate_power_law_distribution_parameters(patches)

            if self.center:
                self.send_message.emit("Calculating buffer counts...")
                calculator = RingAndArea.BufferCalculator(self.file_paths, self.center_path, 1)
                error_code = calculator.calculateBufferCounts()

                if error_code == RingAndArea.ErrorCode_RR.Success:
                    try:
                        all_buffer_counts = calculator.getAllBufferCounts()
                        developed_buffer_counts = calculator.getDevelopedBufferCounts()

                        self.send_message.emit("Fitting ring and area data...")
                        self.ring_and_area_fit(all_buffer_counts, developed_buffer_counts, buffer_spacing)
                        self.send_message.emit("Ring and area data fitted successfully.")
                    except Exception as e:
                        error_message = f"Fitting failed: {str(e)}\nPlease click 'calculate' and try again."
                        self.send_message.emit(error_message)
                        return
                else:
                    raise RuntimeError(get_error_message(error_code))
                    
        except Exception as e:
            self.error_message.emit(f"An unexpected error occurred: {str(e)}")

    def calculate_lognormal_distribution_parameters(self, patches):
        cell_counts = [patch.cell_count for patch_list in patches for patch in patch_list]
        if len(cell_counts) == 0:
            self.error_message.emit("No patch data available for lognormal distribution calculation.")
            return

        mean = np.mean(cell_counts)
        stddev = np.std(cell_counts)

        mean_formatted = f"{mean:.6f}"
        stddev_formatted = f"{stddev:.6f}"

        self.show_result_lognormal_mean.emit(mean_formatted)
        self.show_result_lognormal_stddev.emit(stddev_formatted)

        self.send_message.emit(f"Lognormal distribution parameters calculated: Mean = {mean_formatted}, StdDev = {stddev_formatted}")

    def calculate_power_law_distribution_parameters(self, patches):
        cell_counts = [patch.cell_count for patch_list in patches for patch in patch_list]
        if len(cell_counts) == 0:
            self.error_message.emit("No patch data available for power law distribution calculation.")
            return

        a, loc, scale = powerlaw.fit(cell_counts, floc=0)
        power = a
        constant = scale

        power_formatted = f"{power:.6f}"
        constant_formatted = f"{constant:.6f}"

        self.show_result_power_constant.emit(constant_formatted)
        self.show_result_power_power.emit(power_formatted)

        self.send_message.emit(f"Power law distribution parameters calculated: Power = {power_formatted}, Constant = {constant_formatted}")

    def write_patches_to_csv(self, patches):
        max_length_patch_list = max(patches, key=len)

        data = {'patchId': [patch.patch_id for patch in max_length_patch_list]}
        
        for idx, patch_list in enumerate(patches):
            column_name = f'Patch Size Index {idx+1}-{idx+2} (cell)'
            patch_dict = {patch.patch_id: patch.cell_count for patch in patch_list}
            column_data = [patch_dict.get(patch.patch_id, None) for patch in max_length_patch_list]
            data[column_name] = column_data

        df = pd.DataFrame(data)
        
        csv_file_path = f"{self.output_folder}/patch_sizes.csv"
        df.to_csv(csv_file_path, index=False)
        
        self.send_message.emit(f"Patches have been successfully written to {csv_file_path}")

    def ring_and_area_fit(self, all_buffer_counts, develope_buffer_counts, buffer_spacing):
        fits = self.calculate_fits(all_buffer_counts, develope_buffer_counts)
        fig = self.plot_fits(fits)
        self.plot_ready.emit(fig)
        self.send_message.emit("Ring and area plot is ready.")

    def calculate_fits(self, all_buffer_counts, develope_buffer_counts):
        fits = []

        def fit_gaussian(buffer_spacing, p0):
            buffer_spacing = int(buffer_spacing)
            best_R2 = -np.inf
            best_params = None
            for all_counts, develop_counts in zip(all_buffer_counts, develope_buffer_counts):
                summed_all_counts = [sum(all_counts[i:i + buffer_spacing]) for i in range(0, len(all_counts), buffer_spacing)]
                summed_develop_counts = [sum(develop_counts[i:i + buffer_spacing]) for i in range(0, len(develop_counts), buffer_spacing)]

                proportions = [d / a for d, a in zip(summed_develop_counts, summed_all_counts)]

                y_data = smooth_data(proportions, window_size=3)
                x_data = np.arange(len(y_data))

                try:
                    popt, _ = curve_fit(gaussian, x_data, y_data, p0=p0)
                    y_fit = gaussian(x_data, *popt)

                    R2 = r2(y_data, y_fit)

                    if R2 > best_R2:
                        best_R2 = R2
                        best_params = (buffer_spacing, popt)

                    if R2 >= 0.95:
                        return -R2, buffer_spacing, popt

                except RuntimeError:
                    continue

            return -best_R2, best_params[0], best_params[1] if best_params else p0

        def objective(params):
            buffer_spacing, p0_amp, p0_mu, p0_sigma = params
            p0 = [p0_amp, p0_mu, p0_sigma]
            result = fit_gaussian(buffer_spacing, p0)
            return result[0]

        max_buffer_spacing = min(len(all_buffer_counts[0]), len(develope_buffer_counts[0])) // 200
        bounds = [
            (10, max_buffer_spacing),  # buffer_spacing范围
            (0.001, 1),                 # p0_amplitude范围
            (0.1, 200),                 # p0_mean范围
            (0.1, 200)                  # p0_stddev范围
        ]

        result = differential_evolution(objective, bounds)

        best_buffer_spacing = int(result.x[0])
        best_p0 = result.x[1:]

        # 表头
        self.send_message.emit("\n******* Gaussion Parameters Fit Results *******")
        self.send_message.emit("Amplitude\tMean\tStdDev")

        for all_counts, develop_counts in zip(all_buffer_counts, develope_buffer_counts):
            summed_all_counts = [sum(all_counts[i:i + best_buffer_spacing]) for i in range(0, len(all_counts), best_buffer_spacing)]
            summed_develop_counts = [sum(develop_counts[i:i + best_buffer_spacing]) for i in range(0, len(develop_counts), best_buffer_spacing)]
            proportions = [d / a for d, a in zip(summed_develop_counts, summed_all_counts)]

            y_data = smooth_data(proportions, window_size=3)
            x_data = np.arange(len(y_data))

            try:
                popt, _ = curve_fit(gaussian, x_data, y_data, p0=best_p0)
                y_fit = gaussian(x_data, *popt)
                R2 = r2(y_data, y_fit)
                mu_actual = popt[1] * best_buffer_spacing
                sigma_actual = popt[2] * best_buffer_spacing

                fits.append((x_data, y_data, y_fit, popt[0], mu_actual, sigma_actual, R2))
                
                # 输出结果
                self.send_message.emit(f"{popt[0]:.6f}\t{mu_actual:.6f}\t{abs(sigma_actual):.6f}")
                
            except RuntimeError:
                fits.append((x_data, y_data, None, None, None, None, None))

        # 结果封闭
        self.send_message.emit("*************** End of Fit Results ****************\n")

        return fits

    def plot_fits(self, fits):
        fig = Figure(figsize=(3, len(fits) * 2))
        axs = fig.subplots(nrows=len(fits), ncols=1, sharex=True, sharey=False)

        if len(fits) == 1:
            axs = [axs]  # Ensure handling single subplot case

        for i, (x_data, y_data, y_fit, amp, mu_actual, sigma_actual, R2) in enumerate(fits):
            axs[i].bar(x_data, y_data, edgecolor='black', label='Buffer Proportions')
            if y_fit is not None:
                axs[i].plot(x_data, y_fit, 'r-', label='Gaussian Fit', linewidth=1.5)
                axs[i].text(0.95, 0.95, f'R2 = {R2:.2f}', horizontalalignment='right', verticalalignment='top', transform=axs[i].transAxes, fontsize=8, bbox=dict(facecolor='white', alpha=0.5))
            else:
                axs[i].text(0.95, 0.95, 'Fitting Failed', horizontalalignment='right', verticalalignment='top', transform=axs[i].transAxes, fontsize=8, bbox=dict(facecolor='white', alpha=0.5))

            axs[i].set_xlabel('Buffer Ring Index', fontsize=8)
            axs[i].set_ylabel('Proportion of Developed Cells', fontsize=8)
            axs[i].legend(fontsize=8)

            for label in axs[i].get_yticklabels():
                label.set_fontsize(8)
            for label in axs[i].get_xticklabels():
                label.set_fontsize(8)

        fig.tight_layout()

        return fig
    

class PSSA_Dialog(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_PSSA()
        self.ui.setupUi(self)
        self.setWindowTitle("Patch Size Statistical Analysis (PSSA) ")  # Set window title
        self.settings = QSettings("MyCompany", "MyApp")
        self.can_run = False
        self.worker_thread = None
        self.gfw = GaussFigure()
        self.set_default_parameters()

        self.ui.checkBox_03_calculate_gaussian_parrameters.stateChanged.connect(self.update_checkBox_03_calculate_gaussian_parrameters)
        self.ui.checkBox_03_print_patch.stateChanged.connect(self.update_checkBox_03_print_patch)
        
        self.ui.Button_01_input.clicked.connect(self.on_button_01_input_clicked)
        self.ui.Button_02_remove.clicked.connect(self.remove_selected_rows)
        self.ui.toolButton_04_center_data.clicked.connect(self.on_toolButton_04_center_data_clicked)
        self.ui.Button_02_up.clicked.connect(self.move_up_rows)
        self.ui.Button_02_down.clicked.connect(self.move_down_rows)
        self.ui.Button_04_save_location.clicked.connect(self.on_Button_04_save_location_clicked)
        self.ui.Button_02_check.clicked.connect(self.check_files)
        self.ui.Button_05_calculate.clicked.connect(self.calculate)
        self.ui.splitter.splitterMoved.connect(self.adjust_column_widths)

        self.ui.textBrowser.setPlaceholderText("Run Information Output...")

    def set_default_parameters(self):
        self.update_checkBox_03_calculate_gaussian_parrameters(False)
        self.update_checkBox_03_print_patch(False)
        self.ui.table_02_input_show.setColumnCount(2)
        self.ui.table_02_input_show.setHorizontalHeaderLabels(["Index", "Path"])
        self.ui.table_02_input_show.verticalHeader().setVisible(False)
        header = self.ui.table_02_input_show.horizontalHeader()
        header.setDefaultAlignment(Qt.AlignCenter)
        self.ui.table_02_input_show.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.adjust_column_widths()

    def adjust_column_widths(self):
        total_width = self.ui.table_02_input_show.width() - 6
        column_1_width = total_width * 0.1
        column_2_width = total_width * 0.9
        self.ui.table_02_input_show.setColumnWidth(0, column_1_width)
        self.ui.table_02_input_show.setColumnWidth(1, column_2_width)

    def update_checkBox_03_calculate_gaussian_parrameters(self, check):
        if check:
            self.ui.frame_04_center_data.show()
            # self.ui.widget.show()
        else:
            self.ui.frame_04_center_data.hide()
            # self.ui.widget.hide()
    
    def update_checkBox_03_print_patch(self, check):
        if check:
            self.ui.frame_04_save_location.show()
        else:
            self.ui.frame_04_save_location.hide()

    def on_button_01_input_clicked(self):
        last_path = self.settings.value("last_path", "")
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Select Raster Image File",
            last_path,
            "Raster Image Files (*.tif *.tiff)"
        )
        if file_path:
            self.settings.setValue("last_path", file_path)
            self.add_file_to_table(file_path)

    def on_Button_04_save_location_clicked(self):
        last_folder_path = self.settings.value("last_folder_path", "")
        folder_path = QFileDialog.getExistingDirectory(
            self,
            "Select Folder",
            last_folder_path
        )
        if folder_path:
            self.settings.setValue("last_folder_path", folder_path)
            self.ui.lineEdit_04_save_location.setText(folder_path)

    def on_toolButton_04_center_data_clicked(self):
        last_path = self.settings.value("last_path", "")
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Select Raster Image File",
            last_path,
            "Raster Image Files (*.tif *.tiff)"
        )
        if file_path:
            self.settings.setValue("last_path", file_path)
            self.ui.lineEdit_04_center_data.setText(file_path)

    def add_file_to_table(self, file_path):
        if self.is_path_in_table(file_path):
            print(f"File path already exists: {file_path}")
            return

        row_position = self.ui.table_02_input_show.rowCount()
        self.ui.table_02_input_show.insertRow(row_position)

        index_item = QTableWidgetItem(str(row_position + 1))
        index_item.setTextAlignment(Qt.AlignCenter)

        path_item = QTableWidgetItem(file_path)
        path_item.setTextAlignment(Qt.AlignCenter)

        self.ui.table_02_input_show.setItem(row_position, 0, index_item)
        self.ui.table_02_input_show.setItem(row_position, 1, path_item)

    def is_path_in_table(self, file_path):
        for row in range(self.ui.table_02_input_show.rowCount()):
            path_item = self.ui.table_02_input_show.item(row, 1)
            if path_item and path_item.text() == file_path:
                return True
        return False

    def remove_selected_rows(self):
        selected_rows = set()
        for item in self.ui.table_02_input_show.selectedItems():
            selected_rows.add(item.row())
        
        for row in sorted(selected_rows, reverse=True):
            self.ui.table_02_input_show.removeRow(row)
        self.renumber_rows()

    def renumber_rows(self):
        for row in range(self.ui.table_02_input_show.rowCount()):
            index_item = QTableWidgetItem(str(row + 1))
            index_item.setTextAlignment(Qt.AlignCenter)
            path_item = self.ui.table_02_input_show.item(row, 1)
            if path_item:
                path_item.setTextAlignment(Qt.AlignCenter)

            self.ui.table_02_input_show.setItem(row, 0, index_item)
    
    def move_up_rows(self):
        selected_rows = set()
        for item in self.ui.table_02_input_show.selectedItems():
            selected_rows.add(item.row())

        if min(selected_rows) > 0:
            for row in sorted(selected_rows):
                self.ui.table_02_input_show.insertRow(row - 1)
                for column in range(self.ui.table_02_input_show.columnCount()):
                    item = self.ui.table_02_input_show.takeItem(row + 1, column)
                    self.ui.table_02_input_show.setItem(row - 1, column, item)
                self.ui.table_02_input_show.removeRow(row + 1)
        
            self.renumber_rows()

            for row in selected_rows:
                next_row = row - 1
                for column in range(self.ui.table_02_input_show.columnCount()):
                    item = self.ui.table_02_input_show.item(next_row, column)
                    if item:
                        item.setSelected(True)

    def move_down_rows(self):
        selected_rows = set()
        for item in self.ui.table_02_input_show.selectedItems():
            selected_rows.add(item.row())

        if max(selected_rows) < self.ui.table_02_input_show.rowCount() - 1:
            for row in sorted(selected_rows, reverse=True):
                self.ui.table_02_input_show.insertRow(row + 2)
                for column in range(self.ui.table_02_input_show.columnCount()):
                    item = self.ui.table_02_input_show.takeItem(row, column)
                    self.ui.table_02_input_show.setItem(row + 2, column, item)
                self.ui.table_02_input_show.removeRow(row)
            
            self.renumber_rows()

            for row in selected_rows:
                next_row = row + 1
                for column in range(self.ui.table_02_input_show.columnCount()):
                    item = self.ui.table_02_input_show.item(next_row, column)
                    if item:
                        item.setSelected(True)

    def check_files(self):
        self.can_run = False
        row_count = self.ui.table_02_input_show.rowCount()
        if row_count <= 1:
            self.show_error_message("At least two raster images are required.")
            self.set_success(0)
            return

        file_paths = [self.ui.table_02_input_show.item(row, 1).text() for row in range(row_count)]

        for file_path in file_paths:
            if not os.path.exists(file_path):
                self.show_error_message(f"File does not exist: {file_path}")
                self.set_success(0)
                return

        try:
            if (not CheckTifDimensions(file_paths)):
                self.show_error_message("All TIF files must have the same shape (rows and columns).")
                self.set_success(0)
                return
                        
            if self.ui.checkBox_03_print_patch.isChecked():
                folder_path = self.ui.lineEdit_04_save_location.text()

                # 检查 folder_path 是否为空
                if not folder_path:
                    self.show_error_message("Enter the patch save directory.")
                    self.set_success(0)
                    return

                if not os.path.exists(folder_path):
                    response = QMessageBox.question(
                        self,
                        "Create Folder",
                        f"Folder does not exist: {folder_path}\nDo you want to create it?",
                        QMessageBox.Yes | QMessageBox.No
                    )
                    if response == QMessageBox.Yes:
                        os.makedirs(folder_path)
                    else:
                        self.set_success(0)
                        return

            self.set_success(1)
        except Exception as e:
            self.show_error_message(f"An error occurred while checking files: {e}")
            self.set_success(0)
        
    def show_error_message(self, message):
        QMessageBox.critical(self, "Error", message)
    
    def check_file_statement(self):
        if not self.ui.checkBox_03_print_patch.isChecked():
            return True
        
        row_count = self.ui.table_02_input_show.rowCount()
        file_path = self.ui.lineEdit_04_save_location.text()
        # Generate paths
        paths = []
        for i in range(row_count-1):
            path_tif = os.path.join(file_path, f"patch_index_{i+1}-{i+2}.tif")
            paths.append(path_tif)
        paths.append(os.path.join(file_path, "patch_sizes.csv"))

        files_to_overwrite = []
        for path in paths:
            if os.path.exists(path):
                files_to_overwrite.append(path)

        # Prompt the user
        if files_to_overwrite:
            # Prepare message for files that will be overwritten
            msg = f"The following files will be overwritten and must be closed:\n\n"
            msg += "\n".join(files_to_overwrite)
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Warning)
            msg_box.setText(msg)
            msg_box.setInformativeText("Do you want to proceed?")
            msg_box.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            msg_box.setDefaultButton(QMessageBox.Cancel)
            
            reply = msg_box.exec_()
            
            if reply == QMessageBox.Ok:
                return True
            else:
                return False
        else:
            # If no files need to be overwritten, return True directly
            return True

    def calculate(self):
        file_paths = [self.ui.table_02_input_show.item(row, 1).text() for row in range(self.ui.table_02_input_show.rowCount())]
        output_folder = self.ui.lineEdit_04_save_location.text()
        self.check_files()
        
        statement = self.check_file_statement()

        if(not self.can_run or not statement):
            return
        
        neighbor_type = int(self.ui.comBox_03_neighbor_type.currentText())
        print_patch = self.ui.checkBox_03_print_patch.isChecked()

        center = self.ui.checkBox_03_calculate_gaussian_parrameters.isChecked()
        center_path = self.ui.lineEdit_04_center_data.text()

        self.worker_thread = WorkerThread(file_paths, output_folder, print_patch, neighbor_type, center, center_path)

        self.worker_thread.show_result_lognormal_mean.connect(self.ui.lineEdit_06_mean.setText)
        self.worker_thread.show_result_lognormal_stddev.connect(self.ui.lineEdit_06_standard_deviation.setText)
        self.worker_thread.show_result_power_constant.connect(self.ui.lineEdit_06_scale_constant.setText)
        self.worker_thread.show_result_power_power.connect(self.ui.lineEdit_06_power.setText)
        self.worker_thread.error_message.connect(self.ui.textBrowser.append)
        self.worker_thread.send_message.connect(self.ui.textBrowser.append)
        self.worker_thread.plot_ready.connect(self.update_widget_with_plot)

        self.worker_thread.start()
        # self.worker_thread.run()  # when debug
 
    def update_widget_with_plot(self, fig):
        self.gfw.update_widget_with_plot(fig)
        self.gfw.show()

    def set_success(self, success):
        if success:
            icon_path = ":/resources/successfully_checked.svg"  # Using the :/ prefix to reference the resource
            self.ui.Button_02_check.setIcon(QtGui.QIcon(icon_path))
            self.can_run = True
        else:
            icon_path = ":/resources/failed_check.svg"
            self.ui.Button_02_check.setIcon(QtGui.QIcon(icon_path))
    
    def closeEvent(self, event):
        if self.worker_thread and self.worker_thread.isRunning():
            self.worker_thread.terminate()
            self.worker_thread.wait()
        self.gfw.close()
        event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = PSSA_Dialog()
    widget.show()
    sys.exit(app.exec())
