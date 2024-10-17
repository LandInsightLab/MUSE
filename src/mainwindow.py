# MIT License
#
# Copyright (c) 2023 LandInsightLab 
# Author: Rui Shi
# Date: May 2023
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


def load_large_modules():
    global pd, pickle, configparser, logging, sys
    global QFileDialog, QMessageBox, QDesktopServices, QPainter, QColor
    global QUrl, QSettings, QPropertyAnimation, Qt
    global MUSE_API, CheckTifDimensions
    global UDSA_Dialog, PSSA_Dialog
    global Ui_MainWindow
    global Path
    
    import sys
    import pandas as pd
    import pickle
    import configparser
    import logging

    from PySide6.QtWidgets import QFileDialog, QMessageBox
    from PySide6.QtGui import QDesktopServices, QPainter, QColor
    from PySide6.QtCore import QUrl, QSettings, QPropertyAnimation, Qt
    from libs import MUSE_API, CheckTifDimensions
    from src.UDSA import UDSA_Dialog
    from src.PSSA import PSSA_Dialog

    from resources.ui.mainwindow_ui import Ui_MainWindow
    from pathlib import Path

from src.POT import POT_Widget
from PySide6.QtWidgets import QDialog, QWidget, QMainWindow
from PySide6.QtCore import Signal, QThread
from resources.ui.aboutus_ui import Ui_AboutUs


class AboutDialog(QDialog):
    def __init__(self):
        super().__init__()
        
        # Set up the UI from Ui_AboutUs
        self.ui = Ui_AboutUs()
        self.ui.setupUi(self)


class MUSEThread(QThread):
    success = Signal(bool)
    finished = Signal(list)
    progress = Signal(str)
    update_progress_bar = Signal(int)

    def __init__(self, MUSE_API, params):
        super().__init__()
        self.MUSE_API = MUSE_API
        self.params = params

    def run(self):
        try:
            self.MUSE_API.set_callback(lambda message: self.progress.emit(message))
            # self.MUSE_API.set_progress_callback(lambda progress_value: self.update_progress_bar.emit(progress_value))
            self.MUSE_API.set_progress_callback(lambda progress_value: self.update_progress_bar.emit(progress_value))
            running_information = self.MUSE_API.main(self.params)
            if running_information == 1:
                self.progress.emit("success")
                values = self.MUSE_API.valuation()
                self.success.emit(True)
                self.finished.emit(values)
        except Exception as e:
            # Handle the exception as needed
            self.progress.emit("error: {}".format(str(e)))
        finally:
            self.MUSE_API.stop()


class WriteThread(QThread):
    success = Signal(bool)
    progress = Signal(str)

    def __init__(self, MUSE_API, save_path):
        super().__init__()
        self.MUSE_API = MUSE_API
        self.save_path = save_path

    def run(self):
        try:
            result = self.MUSE_API.write_to_tif(self.save_path)
            if result == 1:
                self.progress.emit(f"Simulation results saved to {self.save_path}")
                self.success.emit(True)
            else:
                self.progress.emit(f"Write failed and the return is not 1. Result: {result}")
        except Exception as e:
            self.progress.emit(f"Error: {str(e)}")
            self.success.emit(False)


class SlipButton(QWidget):
    toggled = Signal(bool) 
    def __init__(self, parent=None):
        super(SlipButton, self).__init__(parent)
        self.setFixedSize(40, 20)
        self.isChecked = False
        self.btnAni = QPropertyAnimation(self, b"pos")
        self.btnAni.setDuration(100)
        
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setPen(Qt.NoPen)
        painter.setBrush(QColor(34, 169, 173) if self.isChecked else QColor(200, 200, 200))
        painter.drawRoundedRect(0, 0, self.width(), self.height(), self.height() / 2, self.height() / 2)
        painter.setBrush(QColor(255, 255, 255))
        knob_x = self.width() - self.height() if self.isChecked else 0
        painter.drawEllipse(knob_x, 0, self.height(), self.height())
        
    def mouseReleaseEvent(self, event):
        self.isChecked = not self.isChecked
        self.update()
        self.toggled.emit(self.isChecked)
        super(SlipButton, self).mouseReleaseEvent(event)


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        load_large_modules()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.mlcs_widget = UDSA_Dialog()
        self.pst_widget = PSSA_Dialog()
        self.mgot_widget = POT_Widget()
        self.settings = QSettings("LandInisightLab", "MUSE")
        self.config_file = './config.ini'
        self.config = configparser.ConfigParser()

        self.language = -1
        # Instantiate SlipButton and add to frame_02
        self.slip_button = SlipButton(self.ui.frame_02)
        self.slip_button.move(10, 10) 
        self.is_sliped = False
        self.scenario_simulation = False
        self.success = False
        self.write_thread = None
        self.muse_thread = None
        self.setup_logging()
        self.load_config()
        self.set_default_parameters()

        # action ---------------------------------------------------------------------------------------- connect
        self.ui.action_00_open.triggered.connect(self.on_action_00_open_triggered)
        self.ui.action_00_save.triggered.connect(self.on_action_00_save_triggered)
        self.ui.action_00_mlcs.triggered.connect(self.on_action_00_mlcs_triggered)
        self.ui.action_00_pst.triggered.connect(self.on_action_00_pst_triggered)
        self.ui.action_00_Chinese_Simplified.triggered.connect(self.on_action_00_Chinese_simplified_triggered)
        self.ui.action_00_English.triggered.connect(self.on_action_00_English_triggered)
        self.ui.action_00_simulation.triggered.connect(self.on_action_00_simulation_triggered)
        self.ui.action_00_verification.triggered.connect(self.on_action_00_verification_triggered)
        self.ui.action_00_about.triggered.connect(self.on_action_00_about_triggered)
        self.ui.action_00_exit.triggered.connect(self.on_action_00_exit_triggered)
        self.ui.actionge_00_ParsByGa.triggered.connect(self.on_action_00_ga_triggered)
        self.ui.action_00_patch_info.triggered.connect(self.on_action_00_patch_info_triggered)
        self.ui.action_00_version.triggered.connect(self.on_action_00_version_triggered)
        self.ui.action_00_user_guid.triggered.connect(self.on_action_00_user_guide_triggered)
        self.ui.action_00_MUSE_Toolbox.triggered.connect(self.on_action_00_muse_toolbox_triggered)
        # input ------------------------------------------------------------------------------------connect end

        # input ----------------------------------------------------------------------------------------connect
        self.ui.btn_01_urban_start.clicked.connect(self.on_btn_01_urban_start_clicked)
        self.ui.btn_01_urban_constraint.clicked.connect(self.on_btn_01_urban_constraint_clicked)
        self.ui.btn_01_urban_probability.clicked.connect(self.on_btn_01_urban_probability_clicked)
        self.ui.btn_01_urban_end.clicked.connect(self.on_btn_01_urban_end_clicked)
        self.ui.btn_01_urban_area.clicked.connect(self.on_btn_01_urban_area_clicked)
        #input -------------------------------------------------------------------------------------connect end

        # 02 modifing-----------------------------------------------------------------------------------connect
        self.slip_button.toggled.connect(self.on_slip_button_toggled)
        self.ui.btn_02_modifing_csv.clicked.connect(self.on_btn_02_modifing_csv_clicked)
        self.ui.btn_02_modifing_tif.clicked.connect(self.on_btn_02_modifing_tif_clicked)
        # 02 modifing-------------------------------------------------------------------------------connect end

        # 03 model parameters---------------------------------------------------------------------------connect
        self.ui.checkBox_03_organic_by_step.stateChanged.connect(self.on_checkBox_03_organic_by_step_changed)
        self.ui.toolButton_03_organic_by_step.clicked.connect(self.on_toolButton_03_organic_by_step_clicked)
        # 03 model parameters-----------------------------------------------------------------------connect end

        # 04 patch size generator-----------------------------------------------------------------------connect
        self.ui.comboBox_04_generator_select.currentIndexChanged.connect(self.comboBox_04_generator_select_changed)
        self.ui.btn_04_self_defining_generator.clicked.connect(self.on_btn_04_self_defining_generator_clicked)
        # 04 patch size generator-------------------------------------------------------------------connect end

        # 05 generator engine---------------------------------------------------------------------------connect
        self.ui.comboBox_05_engine_select.currentIndexChanged.connect(self.comboBox_05_engine_select_changed)
        self.ui.btn_05_shape_parameters_path.clicked.connect(self.on_btn_05_shape_parameters_path_clicked)
        # 05 generator engine-----------------------------------------------------------------------connect end

        # 06 Results and performance--------------------------------------------------------------------connect
        self.ui.btn_06_run.clicked.connect(self.on_btn_06_run_clicked)
        self.ui.btn_06_save.clicked.connect(self.on_btn_06_save_clicked)
        # 06 Results and performance----------------------------------------------------------------connect end

        self.mgot_widget.ui.btn_04_run.clicked.connect(self.on_mgot_ui_btn_04_run_clicked)

    def set_default_parameters(self):
        self.on_checkBox_03_organic_by_step_changed(True)
        self.ui.frame_02.setFixedWidth(64)
        self.on_slip_button_toggled(False)
        self.ui.btn_06_save.setDisabled(True)
        self.comboBox_04_generator_select_changed(0)
        self.comboBox_05_engine_select_changed(0)
        self.ui.lineEdit_05_shape_parameters_path.setMinimumWidth(180)  # Set the minimum width

    def setup_logging(self):
        """Set up logging configuration"""
        logging.basicConfig(
            filename='program.log',  # Log file name
            level=logging.ERROR,  # Log only ERROR and above
            format='%(asctime)s - %(levelname)s - %(message)s',  # Log format
        )

    def load_config(self):
        """Load the config file and check the Language item"""
        try:
            if not Path(self.config_file).exists():
                raise FileNotFoundError(f"Config file {self.config_file} not found.")
            
            self.config.read(self.config_file)

            if 'Settings' not in self.config or 'Language' not in self.config['Settings']:
                raise KeyError("Missing 'Settings' section or 'Language' item in the config file.")

            # Get the current language value from the config file
            current_language = self.config['Settings']['Language']
            
            if current_language == '0':
                self.on_action_00_English_triggered()
            elif current_language == '1':
                self.on_action_00_Chinese_simplified_triggered()
            else:
                raise ValueError("Invalid language setting value, must be '0' (English) or '1' (Chinese).")
        except Exception as e:
            logging.error(f"Error while loading config file: {e}")
        
    def save_config(self):
        with open(self.config_file, 'w') as configfile:
            self.config.write(configfile)

    def open_file_with_filter(self, dir_path, data_type):
        # Define supported data types
        file_filters = {
            'tif': "TIF Files (*.tif *.tiff)",
            'tiff': "TIFF Files (*.tif *.tiff)",
            'csv': "CSV Files (*.csv)"
        }
        # Ensure the provided data type is supported
        if data_type not in file_filters:
            raise ValueError(f"Unsupported data type: {data_type}")
        # Get file path
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.ExistingFiles)
        file_path, _ = file_dialog.getOpenFileName(None, "Select File", dir_path, file_filters[data_type])
        return file_path

    def show_message(self, message, msg_type="error"):
        msg_box = QMessageBox()
        if msg_type == "error":
            msg_box.setIcon(QMessageBox.Critical)
            msg_box.setWindowTitle("Error")
        elif msg_type == "info":
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setWindowTitle("Information")
        elif msg_type == "warning":
            msg_box.setIcon(QMessageBox.Warning)
            msg_box.setWindowTitle("Warning")
        else:
            msg_box.setIcon(QMessageBox.NoIcon)
            msg_box.setWindowTitle("Message")

        msg_box.setText(message)
        msg_box.setStandardButtons(QMessageBox.Ok)
        msg_box.exec()

    def on_mgot_ui_btn_04_run_clicked(self):
        if self.ui.checkBox_03_organic_by_step.isChecked():
            self.ui.checkBox_03_organic_by_step.setChecked(False)
            if not self.check_parameters_validity():
                return
            self.ui.checkBox_03_organic_by_step.setChecked(True)
        else:
            if not self.check_parameters_validity():
                return
        
        if self.scenario_simulation:
            self.show_message("Multi-Goal optimization tool only allows use in model validation mode.")

        ga_muse_parameters = {
            'mode': self.scenario_simulation,

            'initialUrbanLand': self.ui.lineEdit_01_urban_start.text(),
            'developmentConstraints': self.ui.lineEdit_01_urban_constraint.text(), 
            'finalUrbanLand': self.ui.lineEdit_01_urban_end.text(),   
            'urbanSuitability': self.ui.lineEdit_01_urban_probability.text(),
            'additionalUrbanLandArea': self.ui.lineEdit_01_urban_Area.text(),

            'expansionControl': self.is_sliped,
            'cityCenter': self.ui.lineEdit_02_modifing_tif.text(),   
            'correctionParameters': self.ui.lineEdit_02_modifing_csv.text(), 
            'cityCenterWeight': self.ui.doubleSpinbox_02_modifing_weight.value(),

            'initialNode': self.ui.spinbox_03_start_year.value(),   
            'finalNode': self.ui.spinbox_03_end_year.value(),   
            'uncertainty': 1,   
            'neighborhoodType': int(self.ui.comboBox_03_neibor_type.currentText()),   
            'additionalUrbanLandOrganic': self.ui.doubleSpinBox_03_organic.value(),   

            'controllerType': self.ui.comboBox_04_generator_select.currentIndex(),   
            'lognormalMean': self.ui.doubleSpinBox_04_mean.value(),
            'lognormalStdDev': self.ui.doubleSpinBox_04_standard_deviation.value(),
            'powerLawConstant': self.ui.doubleSpinBox_04_scale_constant.value(),
            'powerLawExponent': self.ui.doubleSpinBox_04_power.value(),
            'historicalBlockSizes': self.ui.lineEdit_04_self_defining_generator.text(),

            'blockEngineType': self.ui.comboBox_05_engine_select.currentIndex(),
            'neighborhoodControlParam': self.ui.doubleSpinBox_05_parameter_beta.value(),
            'distanceControlParam': self.ui.doubleSpinBox_05_parameter_delta.value(),
        }

        self.mgot_widget.run(ga_muse_parameters)

    # 00 action function
    def on_action_00_open_triggered(self):
        # Open a file dialog to select the file to open
        last_mud_dir = self.settings.value("last_mud_dir", "")
        options = QFileDialog.Options()
        filePath, _ = QFileDialog.getOpenFileName(self, "Open File", last_mud_dir, "MUD Files (*.mud);;All Files (*)", options=options)

        if filePath:
            try:
                # Load data from the .mud file using pickle
                with open(filePath, 'rb') as file:
                    data = pickle.load(file)

                    # Apply the loaded data to the corresponding parts of the program
                    language = data.get("language", "")
                    scenario_simulation = data.get("mode", "")
                    self.ui.lineEdit_01_urban_start.setText(data.get("initialUrbanLand", ""))
                    self.ui.lineEdit_01_urban_end.setText(data.get("finalUrbanLand", ""))
                    self.ui.lineEdit_01_urban_constraint.setText(data.get("developmentConstraints", ""))
                    self.ui.lineEdit_01_urban_probability.setText(data.get("urbanSuitability", ""))
                    self.ui.lineEdit_01_urban_Area.setText(data.get("additionalUrbanLandArea", ""))
                    is_sliped = data.get("expansionControl", False)
                    self.ui.lineEdit_02_modifing_tif.setText(data.get("cityCenter", ""))
                    self.ui.lineEdit_02_modifing_csv.setText(data.get("correctionParameters", ""))
                    self.ui.doubleSpinbox_02_modifing_weight.setValue(data.get("cityCenterWeight", 0))
                    self.ui.spinbox_03_start_year.setValue(data.get("initialNode", 0))
                    self.ui.spinbox_03_end_year.setValue(data.get("finalNode", 0))
                    self.ui.doubleSpinbox_03_pool_slice.setValue(data.get("pruningCoefficient", 0))
                    self.ui.comboBox_03_neibor_type.setCurrentText(str(data.get("neighborhoodType", "")))
                    self.ui.doubleSpinBox_03_organic.setValue(data.get("additionalUrbanLandOrganic", 0))
                    self.ui.comboBox_04_generator_select.setCurrentIndex(data.get("controllerType", 0))
                    self.ui.doubleSpinBox_04_mean.setValue(data.get("lognormalMean", 0.0))
                    self.ui.doubleSpinBox_04_standard_deviation.setValue(data.get("lognormalStdDev", 0.0))
                    self.ui.doubleSpinBox_04_scale_constant.setValue(data.get("powerLawConstant", 0.0))
                    self.ui.doubleSpinBox_04_power.setValue(data.get("powerLawExponent", 0.0))
                    self.ui.lineEdit_04_self_defining_generator.setText(data.get("historicalBlockSizes", ""))
                    self.ui.comboBox_05_engine_select.setCurrentIndex(data.get("engineType", 0))
                    self.ui.doubleSpinBox_05_parameter_beta.setValue(data.get("neighborhoodControlParam", 0.0))
                    self.ui.doubleSpinBox_05_parameter_delta.setValue(data.get("distanceControlParam", 0.0))
                    self.ui.lineEdit_05_shape_parameters_path.setText(data.get("PRG_Parameters", ""))
                    # Continue loading the remaining data items
                    if language == 0:
                        self.on_action_00_English_triggered()
                    elif language == 1:
                        self.on_action_00_Chinese_simplified_triggered()

                    if scenario_simulation:
                        self.on_action_00_verification_triggered()
                    else:
                        self.on_action_00_simulation_triggered()

                    self.on_slip_button_toggled(is_sliped)

                    self.settings.setValue("last_mud_dir", filePath)

            except Exception as e:
                # Display an error message
                QMessageBox.critical(self, "Error", f"Failed to open file: {e}")

    def on_action_00_save_triggered(self):
        # Collect all the user input parameters
        data = {
            "language": self.language,
            "mode": self.scenario_simulation,
            "initialUrbanLand": self.ui.lineEdit_01_urban_start.text(),
            "finalUrbanLand": self.ui.lineEdit_01_urban_end.text(),
            "developmentConstraints": self.ui.lineEdit_01_urban_constraint.text(),
            "urbanSuitability": self.ui.lineEdit_01_urban_probability.text(),
            "additionalUrbanLandArea": self.ui.lineEdit_01_urban_Area.text(),
            "expansionControl": self.is_sliped,
            "cityCenter": self.ui.lineEdit_02_modifing_tif.text(),
            "correctionParameters": self.ui.lineEdit_02_modifing_csv.text(),
            "cityCenterWeight": self.ui.doubleSpinbox_02_modifing_weight.value(),
            "initialNode": self.ui.spinbox_03_start_year.value(),
            "finalNode": self.ui.spinbox_03_end_year.value(),
            "uncertainty": 1,
            "pruningCoefficient": self.ui.doubleSpinbox_03_pool_slice.value(),
            "neighborhoodType": int(self.ui.comboBox_03_neibor_type.currentText()),
            "additionalUrbanLandOrganic": self.ui.doubleSpinBox_03_organic.value(),
            "controllerType": self.ui.comboBox_04_generator_select.currentIndex(),
            "lognormalMean": self.ui.doubleSpinBox_04_mean.value(),
            "lognormalStdDev": self.ui.doubleSpinBox_04_standard_deviation.value(),
            "powerLawConstant": self.ui.doubleSpinBox_04_scale_constant.value(),
            "powerLawExponent": self.ui.doubleSpinBox_04_power.value(),
            "historicalBlockSizes": self.ui.lineEdit_04_self_defining_generator.text(),
            "engineType": self.ui.comboBox_05_engine_select.currentIndex(),
            "neighborhoodControlParam": self.ui.doubleSpinBox_05_parameter_beta.value(),
            "distanceControlParam": self.ui.doubleSpinBox_05_parameter_delta.value(),
            "PRG_Parameters":self.ui.lineEdit_05_shape_parameters_path.text(),
        }

        # Open the save file dialog
        last_mud_dir = self.settings.value("last_mud_dir", "")
        options = QFileDialog.Options()
        filePath, _ = QFileDialog.getSaveFileName(self, "Save File", last_mud_dir, "MUD Files (*.mud);;All Files (*)", options=options)
        
        if filePath:
            # Check the file extension
            if not filePath.endswith('.mud'):
                filePath += '.mud'
            
            try:
                # Save the dictionary as a binary file
                with open(filePath, 'wb') as file:
                    pickle.dump(data, file)
                
                # Show a success message
                self.settings.setValue("last_mud_dir", filePath)
                QMessageBox.information(self, "Success", "File saved successfully!")
            except Exception as e:
                # Show an error message
                QMessageBox.critical(self, "Error", f"Failed to save file: {e}")

    def on_action_00_exit_triggered(self):
        sys.exit()

    def on_action_00_ga_triggered(self):
        self.mgot_widget.show()
        self.mgot_widget.set_weight_for_gauss(self.is_sliped)
        self.mgot_widget.set_engine_checkBox(self.ui.comboBox_05_engine_select.currentIndex())
        
    def on_action_00_muse_toolbox_triggered(self):
        url = QUrl("https://github.com/LandInsightLab/MUSE_ArcGIS_Pro_Toolbox")
        QDesktopServices.openUrl(url)

    def on_action_00_mlcs_triggered(self):
        self.mlcs_widget.show()
        self.mlcs_widget.set_initial_column_widths()
    
    def on_action_00_pst_triggered(self):
        self.pst_widget.show()
        self.pst_widget.adjust_column_widths()

    def on_action_00_Chinese_simplified_triggered(self):
        if self.language != 1:
            self.ui.files.setTitle("文件")
            self.ui.tools.setTitle("工具")
            self.ui.preferences.setTitle("首选项")
            self.ui.help.setTitle("帮助")

            self.ui.action_00_save.setText("保存")
            self.ui.action_00_open.setText("打开")
            self.ui.action_00_exit.setText("退出")

            self.ui.action_00_MUSE_Toolbox.setText("MUSE ArcGIS Pro工具箱")
            self.ui.actionge_00_ParsByGa.setText("参数优化工具模块")
            self.ui.action_00_mlcs.setText("城市发展适宜性评估模块")
            self.ui.action_00_pst.setText("斑块大小统计分析")

            self.ui.language.setTitle("语言")
            self.ui.action_00_English.setText("英文")
            self.ui.action_00_Chinese_Simplified.setText("简体中文")
            self.ui.menumodel.setTitle("模式")
            self.ui.action_00_simulation.setText("模型验证")
            self.ui.action_00_verification.setText("情景模拟")

            self.ui.action_00_user_guid.setText("用户指南")
            self.ui.action_00_version.setText("版本")
            self.ui.action_00_about.setText("关于")

            self.ui.box_01_data_Input.setTitle("数据输入")
            self.ui.label_01_urban_start.setText("模拟初期城市土地")
            self.ui.label_01_urban_contraint.setText("空间约束")
            self.ui.label_01_urban_probability.setText("城市发展适宜性")
            self.ui.label_01_urban_area.setText("新增城市土地面积")
            self.ui.label_01_urban_end.setText("模拟末期城市土地")

            self.ui.box_02_modifing.setTitle("基于高斯的调控")
            self.ui.label_02_modifing_tif.setText("城市中心")
            self.ui.label_02_modifing_csv.setText("高斯参数")
            self.ui.label_02_modifing_weight.setText("高斯函数权重")

            self.ui.box_03_model_parameters.setTitle("全局参数")
            self.ui.label_03_strat_year.setText("起始时间")
            self.ui.label_03_end_Year.setText("结束时间")
            self.ui.label_03_neibor_type.setText("邻域类型")
            self.ui.label_03_pool_Slice.setText("修剪系数")
            self.ui.label_03_location_uncertainty.setText("斑块位置不确定度")
            self.ui.checkBox_03_organic_by_step.setText("逐年有机斑块比例")

            self.ui.box_04_patch_size_generator.setTitle("斑块大小生成器")
            self.ui.comboBox_04_generator_select.setItemText(0, "对数正态分布")
            self.ui.comboBox_04_generator_select.setItemText(1, "幂律分布")
            self.ui.comboBox_04_generator_select.setItemText(2, "历史时期斑块大小")
            self.ui.label_04_mean.setText("均值")
            self.ui.label_04_standard_deviation.setText("标准差")
            self.ui.label_04_scale_constant.setText("比例常数")
            self.ui.label_04_power.setText("幂次")

            self.ui.box_05_engine_select.setTitle("斑块生成引擎选择")
            self.ui.comboBox_05_engine_select.setItemText(0, "简单斑块生成引擎")
            self.ui.comboBox_05_engine_select.setItemText(1, "邻域控制斑块生成引擎")
            self.ui.comboBox_05_engine_select.setItemText(2, "距离控制斑块生成引擎")
            self.ui.comboBox_05_engine_select.setItemText(3, "权衡优化斑块生成引擎")
            self.ui.label_05_shape_parameters_path.setText("形状参数")

            self.ui.box_06_run_and_export.setTitle("模型验证")
            self.ui.btn_06_run.setText("运行")
            self.ui.btn_06_save.setText("保存")

            # 设置占位符文本，指导用户输入
            self.ui.lineEdit_01_urban_start.setPlaceholderText("初始城市土地栅格（tif/tiff，值为0和1）。")
            self.ui.lineEdit_01_urban_constraint.setPlaceholderText("限制因子栅格（tif/tiff，值为0和1）。")
            self.ui.lineEdit_01_urban_Area.setPlaceholderText("新增城市土地面积需求（csv，2列）。")
            self.ui.lineEdit_01_urban_probability.setPlaceholderText("城市适宜性概率栅格（tif/tiff，值为0-1）。")
            self.ui.lineEdit_01_urban_end.setPlaceholderText("最终城市土地栅格（tif/tiff，值为0和1）。")
            self.ui.lineEdit_02_modifing_tif.setPlaceholderText("城市中心点栅格（tif/tiff，值为0和1）。")
            self.ui.lineEdit_02_modifing_csv.setPlaceholderText("高斯修正参数（csv，4列）。")
            self.ui.lineEdit_03_organic_by_step.setPlaceholderText("有机增长步长数据（csv，2列）。")
            self.ui.lineEdit_04_self_defining_generator.setPlaceholderText("生成器的patch大小数据（csv，2列）。")
            self.ui.lineEdit_05_shape_parameters_path.setPlaceholderText("可选输入：CSV，5列")

            # 在 textBrowser 中显示初始说明
            self.ui.textBrowser.setPlaceholderText("模型输出将在此显示。")

            try:
                self.config['Settings']['Language'] = '1'
                self.language = 1
                self.save_config()  # Save the updated config
            except Exception as e:
                logging.error(f"Error while setting language to English: {e}")

    def on_action_00_English_triggered(self):
        if self.language != 0:
            self.ui.files.setTitle("File")
            self.ui.tools.setTitle("Tool")
            self.ui.preferences.setTitle("Preference")
            self.ui.help.setTitle("Help")

            self.ui.action_00_save.setText("save")
            self.ui.action_00_open.setText("open")
            self.ui.action_00_exit.setText("Exit")

            self.ui.action_00_MUSE_Toolbox.setText("MUSE Toolbox")
            self.ui.actionge_00_ParsByGa.setText("Parameter Optimization Tool (POT) module")
            self.ui.action_00_mlcs.setText("Urban Development Suitability Assessment (UDSA) module")
            self.ui.action_00_pst.setText("Patch Size Statistical Analysis (PSSA) ")

            self.ui.language.setTitle("Language")
            self.ui.action_00_English.setText("English")
            self.ui.action_00_Chinese_Simplified.setText("Chinese(Simplified)")
            self.ui.menumodel.setTitle("Mode")
            self.ui.action_00_simulation.setText("Model validation")       
            self.ui.action_00_verification.setText("Scenario simulation") 

            self.ui.action_00_user_guid.setText("User Guide")
            self.ui.action_00_version.setText("version")
            self.ui.action_00_about.setText("About")
    
            self.ui.box_01_data_Input.setTitle("Input files")
            self.ui.label_01_urban_start.setText("Urban land use map of starting time")
            self.ui.label_01_urban_contraint.setText("Spatial Constraints")
            self.ui.label_01_urban_probability.setText("Urban development suitability")
            self.ui.label_01_urban_area.setText("Stepwise demand of urban development")
            self.ui.label_01_urban_end.setText("Urban land use map of ending time")        

            self.ui.box_02_modifing.setTitle("Gaussian-based regulation")
            self.ui.label_02_modifing_tif.setText("City centers")
            self.ui.label_02_modifing_csv.setText("Gaussian parameters")
            self.ui.label_02_modifing_weight.setText("Weight for Gaussian function")
            
            self.ui.box_03_model_parameters.setTitle("Global parameters")
            self.ui.label_03_strat_year.setText("Starting time")
            self.ui.label_03_end_Year.setText("Ending time")
            self.ui.label_03_neibor_type.setText("Type of Neighborhood")
            self.ui.label_03_pool_Slice.setText("Pruning parameter")
            self.ui.label_03_location_uncertainty.setText("Location uncertainty")
            self.ui.checkBox_03_organic_by_step.setText("Enable Stepwise Organic Growth")

            self.ui.box_04_patch_size_generator.setTitle("Patch size generator")
            self.ui.comboBox_04_generator_select.setItemText(0, "Lognormal Distribution")
            self.ui.comboBox_04_generator_select.setItemText(1, "Power Distribution")
            self.ui.comboBox_04_generator_select.setItemText(2, "History patch size")
            self.ui.label_04_mean.setText("Mean")
            self.ui.label_04_standard_deviation.setText("Standard deviation")
            self.ui.label_04_scale_constant.setText("Scale Constant")
            self.ui.label_04_power.setText("Power")

            self.ui.box_05_engine_select.setTitle("Patch generation operator")
            self.ui.comboBox_05_engine_select.setItemText(0, "Simple Patch Generation Engine (SPGE)")
            self.ui.comboBox_05_engine_select.setItemText(1, "Neighbor Patch Generation Engine (NeiPGE)")
            self.ui.comboBox_05_engine_select.setItemText(2, "Distance Patch Generation Engine (DisPGE)")
            self.ui.comboBox_05_engine_select.setItemText(3, "Parameterized Patch Generation Engine (PPGE)")
            self.ui.label_05_shape_parameters_path.setText("Shape Parameter Path")

            self.ui.box_06_run_and_export.setTitle("Results and performance")
            self.ui.btn_06_run.setText("Run")
            self.ui.btn_06_save.setText("Save")

            self.ui.lineEdit_01_urban_start.setPlaceholderText("Initial urban land raster (tif/tiff, values 0 and 1).")
            self.ui.lineEdit_01_urban_constraint.setPlaceholderText("Constraint factor raster (tif/tiff, values 0 and 1).")
            self.ui.lineEdit_01_urban_Area.setPlaceholderText("New urban land area demand (csv, 2 columns).")
            self.ui.lineEdit_01_urban_probability.setPlaceholderText("Urban suitability probability raster (tif/tiff, values 0-1).")
            self.ui.lineEdit_01_urban_end.setPlaceholderText("Final urban land raster (tif/tiff, values 0 and 1).")
            self.ui.lineEdit_02_modifing_tif.setPlaceholderText("Urban center point raster (tif/tiff, values 0 and 1).")
            self.ui.lineEdit_02_modifing_csv.setPlaceholderText("Gaussian correction parameters (csv, 4 columns).")
            self.ui.lineEdit_03_organic_by_step.setPlaceholderText("Organic growth step data (csv, 2 columns).")
            self.ui.lineEdit_04_self_defining_generator.setPlaceholderText("Patch size data (csv, 2 columns).")
            self.ui.lineEdit_05_shape_parameters_path.setPlaceholderText("Optional input, (csv, 2 columns)")

            # Display initial instruction in textBrowser
            self.ui.textBrowser.setPlaceholderText("Run Information Output...")

            try:
                self.config['Settings']['Language'] = '0'
                self.language = 0
                self.save_config()  # Save the updated config
            except Exception as e:
                logging.error(f"Error while setting language to English: {e}")

    def on_action_00_simulation_triggered(self):
        self.ui.urban_End_Frame.setVisible(True)
        self.ui.frame_06_accuracy.setVisible(True)
        self.scenario_simulation = False
        self.ui.actionge_00_ParsByGa.setDisabled(False)

    def on_action_00_verification_triggered(self):
        self.ui.urban_End_Frame.setVisible(False)
        self.ui.frame_06_accuracy.setVisible(False)
        self.scenario_simulation = True
        self.ui.actionge_00_ParsByGa.setDisabled(True)

    def on_action_00_user_guide_triggered(self):
        try:
            if self.language == 0:
                file_path = "Guide_ENG.pdf"
            elif self.language == 1:
                file_path = "Guide_CH.pdf"
            else:
                logging.error("Unsupported language setting.")
                return
            
            # Convert the file path to a URL
            file_url = QUrl.fromLocalFile(file_path)
            
            # Attempt to open the file using the default system application
            if not QDesktopServices.openUrl(file_url):
                logging.error(f"Failed to open the file: {file_path}")
            
        except Exception as e:
            logging.error(f"Unexpected error: {e}")

    def on_action_00_patch_info_triggered(self):   

        pass

    def on_action_00_version_triggered(self):

        pass

    def on_action_00_about_triggered(self):
        about_dialog = AboutDialog()
        about_dialog.exec_()
    # 00 action function end

    # 01 input function
    def on_btn_01_urban_start_clicked(self):
        last_dir_path = self.settings.value("last_dir_start", "")
        selected_file = self.open_file_with_filter(last_dir_path, "tif")
        if selected_file:
            self.ui.lineEdit_01_urban_start.setText(selected_file)
            self.settings.setValue("last_dir_start", selected_file)

    def on_btn_01_urban_constraint_clicked(self):
        last_dir_path = self.settings.value("last_dir_start", "")
        selected_file = self.open_file_with_filter(last_dir_path, "tif")
        if selected_file:
            self.ui.lineEdit_01_urban_constraint.setText(selected_file)
            self.settings.setValue("last_dir_start", selected_file)

    def on_btn_01_urban_probability_clicked(self):
        last_dir_path = self.settings.value("last_dir_start", "")
        selected_file = self.open_file_with_filter(last_dir_path, "tif")
        if selected_file:
            self.ui.lineEdit_01_urban_probability.setText(selected_file)
            self.settings.setValue("last_dir_start", selected_file)

    def on_btn_01_urban_end_clicked(self):
        last_dir_path = self.settings.value("last_dir_start", "")
        selected_file = self.open_file_with_filter(last_dir_path, "tif")
        if selected_file:
            self.ui.lineEdit_01_urban_end.setText(selected_file)
            self.settings.setValue("last_dir_start", selected_file)

    def on_btn_01_urban_area_clicked(self):
        last_dir_path = self.settings.value("last_dir_urban_area", "")
        selected_file = self.open_file_with_filter(last_dir_path, "csv")
        if selected_file:
            self.ui.lineEdit_01_urban_Area.setText(selected_file)
            self.settings.setValue("last_dir_urban_area", selected_file)
    # 01 input function end

    # 02 modifing function
    def on_slip_button_toggled(self, checked):
        self.ui.modifing_csv_frame.setVisible(checked)
        self.ui.modifing_tif_frame.setVisible(checked)
        self.ui.modifing_weight_frame.setVisible(checked)
        self.is_sliped = checked

    def on_btn_02_modifing_tif_clicked(self):
        last_dir_path = self.settings.value("last_dir_start", "")
        selected_file = self.open_file_with_filter(last_dir_path, "tif")
        if selected_file:
            self.ui.lineEdit_02_modifing_tif.setText(selected_file)
            self.settings.setValue("last_dir_start", selected_file)

    def on_btn_02_modifing_csv_clicked(self):
        last_dir_path = self.settings.value("last_dir_urban_area", "")
        selected_file = self.open_file_with_filter(last_dir_path, "csv")
        if selected_file:
            self.ui.lineEdit_02_modifing_csv.setText(selected_file)
            self.settings.setValue("last_dir_urban_area", selected_file)
    # 02 modifing function end

    # 03 model parametres
    def on_checkBox_03_organic_by_step_changed(self, check):
        if check:
            self.ui.lineEdit_03_organic_by_step.show()
            self.ui.toolButton_03_organic_by_step.show()
            self.ui.doubleSpinBox_03_organic.hide()
        else:
            self.ui.lineEdit_03_organic_by_step.hide()
            self.ui.toolButton_03_organic_by_step.hide()
            self.ui.doubleSpinBox_03_organic.show()
  
    def on_toolButton_03_organic_by_step_clicked(self):
        last_dir_path = self.settings.value("last_dir_urban_area", "")
        selected_file = self.open_file_with_filter(last_dir_path, "csv")
        if selected_file:
            self.ui.lineEdit_03_organic_by_step.setText(selected_file)
            self.settings.setValue("last_dir_urban_area", selected_file)
    # 03 model parametres end

    # 04 patch size generator
    def comboBox_04_generator_select_changed(self, index):
        if index == 0:  # Lognormal distribution
            self.ui.frame_04_lognormal.show()
            self.ui.frame_04_power.hide()
            self.ui.frame_04_history_patch.hide()
        elif index == 1:  # Power distribution
            self.ui.frame_04_lognormal.hide()
            self.ui.frame_04_power.show()
            self.ui.frame_04_history_patch.hide()
        elif index == 2:  # History patch size
            self.ui.frame_04_lognormal.hide()
            self.ui.frame_04_power.hide()
            self.ui.frame_04_history_patch.show()
    
    def on_btn_04_self_defining_generator_clicked(self):
        last_dir_path = self.settings.value("last_dir_urban_area", "")
        selected_file = self.open_file_with_filter(last_dir_path, "csv")
        if selected_file:
            self.ui.lineEdit_04_self_defining_generator.setText(selected_file)
            self.settings.setValue("last_dir_urban_area", selected_file)
    # 04_patch size generator end
    # 05 generator engine
    def comboBox_05_engine_select_changed(self, index):
        if index == 0:
            self.ui.frame_05_engine_parameters.hide()
            self.ui.comboBox_03_neibor_type.setEnabled(True)
            self.ui.doubleSpinBox_03_location_uncertainty.setEnabled(True)
        elif index == 1:
            self.ui.frame_05_engine_parameters.show()
            self.ui.label_05_parameter_beta.show()
            self.ui.doubleSpinBox_05_parameter_beta.show()
            self.ui.label_05_parameter_delta.hide()
            self.ui.doubleSpinBox_05_parameter_delta.hide()
            self.ui.label_05_shape_parameters_path.hide()
            self.ui.lineEdit_05_shape_parameters_path.hide()
            self.ui.comboBox_03_neibor_type.setCurrentIndex(1)
            self.ui.btn_05_shape_parameters_path.hide()
            self.ui.doubleSpinBox_03_location_uncertainty.setValue(1)
            self.ui.doubleSpinBox_03_location_uncertainty.setEnabled(False)
            self.ui.comboBox_03_neibor_type.setEnabled(False)
        elif index == 2:
            self.ui.frame_05_engine_parameters.show()
            self.ui.label_05_parameter_beta.hide()
            self.ui.doubleSpinBox_05_parameter_beta.hide()
            self.ui.label_05_parameter_delta.show()
            self.ui.doubleSpinBox_05_parameter_delta.show()
            self.ui.label_05_shape_parameters_path.hide()
            self.ui.lineEdit_05_shape_parameters_path.hide()
            self.ui.btn_05_shape_parameters_path.hide()
            self.ui.comboBox_03_neibor_type.setEnabled(True)
            self.ui.doubleSpinBox_03_location_uncertainty.setEnabled(True)
        elif index == 3:
            self.ui.frame_05_engine_parameters.show()
            self.ui.label_05_parameter_beta.hide()
            self.ui.doubleSpinBox_05_parameter_beta.hide()
            self.ui.label_05_parameter_delta.hide()
            self.ui.doubleSpinBox_05_parameter_delta.hide()  
            self.ui.label_05_shape_parameters_path.show()
            self.ui.lineEdit_05_shape_parameters_path.show()
            self.ui.comboBox_03_neibor_type.setEnabled(True)
            self.ui.btn_05_shape_parameters_path.show()
            self.ui.doubleSpinBox_03_location_uncertainty.setEnabled(True)
        
    def on_btn_05_shape_parameters_path_clicked(self):
        last_dir_path = self.settings.value("last_dir_urban_area", "")
        selected_file = self.open_file_with_filter(last_dir_path, "csv")
        if selected_file:
            self.ui.lineEdit_05_shape_parameters_path.setText(selected_file)
            self.settings.setValue("last_dir_urban_area", selected_file)
        
    # 05 generator engine end

    # 06 Results and performance
    def check_addresses(self, paths):
        invalid_files = [index + 1 for index, path in enumerate(paths) if not Path(path).is_file()]
        if invalid_files:
            error_message = f"The following fields contain invalid or non-existent files: {', '.join(map(str, invalid_files))}"
            self.show_message(error_message, "error")
            return False
        return True
    
    def check_tif_values(self, file_path):
        distinct_count = CheckTifDimensions.CountDistinctIntegers(file_path)
        if distinct_count == -1:
            self.show_message("MUSE software only supports single-band TIFFs for now. {file_path}")
            return False
        if distinct_count != 2:
            self.show_message(f"The tif file {file_path} should contain exactly two distinct values, which are 0 and 1, but it contains {distinct_count} distinct values.")
            return False
        return True

    def check_csv_file(self, file_path, min_rows, min_cols):
        try:
            # Attempt to read the CSV file using UTF-8 encoding
            df = pd.read_csv(file_path, encoding='utf-8')
        except UnicodeDecodeError:
            try:
                # If UTF-8 fails, attempt to read the CSV file using GBK encoding
                df = pd.read_csv(file_path, encoding='gbk')
            except UnicodeDecodeError:
                try:
                    # If GBK also fails, attempt to read the CSV file using Windows-1252 encoding
                    df = pd.read_csv(file_path, encoding='windows-1252')
                except UnicodeDecodeError:
                    self.show_message(f"Encoding error: Unable to read the file {file_path}. Please ensure the file is encoded in UTF-8, GBK, or Windows-1252.")
                    return False
                except Exception as e:
                    self.show_message(f"Error reading the file {file_path}: {str(e)}")
                    return False
            except Exception as e:
                self.show_message(f"Error reading the file {file_path}: {str(e)}")
                return False

        try:
            # Check number of columns
            num_cols = len(df.columns)
            if num_cols < min_cols:
                self.show_message(f"The file “{file_path}” has {num_cols} columns, which is less than the minimum required {min_cols}.")
                return False
            
            # Check header existence and non-empty (including Chinese characters)
            if df.columns.empty or any(df.columns.astype(str).str.strip() == ''):
                self.show_message("The file “{file_path}” must have a non-empty header.")
                return False
            
            # Total rows including header
            total_rows = len(df) + 1
            if total_rows <= min_rows:
                self.show_message(f"The file “{file_path}” has {total_rows} rows including header, which is not greater than the minimum required {min_rows}.")
                return False
            
            # If all checks pass
            return True
        except FileNotFoundError:
            self.show_message(f"File not found: {file_path}")
        except Exception as e:
            self.show_message(f"Error reading the file {file_path}: {str(e)}")
        return False

    def check_parameters_validity(self):
        urban_area_path = self.ui.lineEdit_01_urban_Area.text()
        file_paths_csv = [urban_area_path]

        urban_start_path = self.ui.lineEdit_01_urban_start.text()
        urban_constraint_path = self.ui.lineEdit_01_urban_constraint.text()
        urban_probability_path = self.ui.lineEdit_01_urban_probability.text()
        file_paths_tif = [urban_start_path, urban_constraint_path, urban_probability_path]
        if not self.scenario_simulation:
            urban_end_path = self.ui.lineEdit_01_urban_end.text()
            file_paths_tif.append(urban_end_path)
        if self.is_sliped:
            file_paths_tif.append(self.ui.lineEdit_02_modifing_tif.text())
            file_paths_csv.append(self.ui.lineEdit_02_modifing_csv.text())
        if self.ui.comboBox_04_generator_select.currentIndex() == 2:
            file_paths_csv.append(self.ui.lineEdit_04_self_defining_generator.text())
        if self.ui.checkBox_03_organic_by_step.isChecked():
            file_paths_csv.append(self.ui.lineEdit_03_organic_by_step.text())

        for file_path in file_paths_tif:

            if not (file_path.lower().endswith('.tif') or file_path.lower().endswith('.tiff')):
                self.show_message(f"File is not a .tif or .tiff file: {file_path}")
                return False
            if not Path(file_path).exists():
                self.show_message(f"File does not exist: {file_path}")
                return False
            
        for file_path in file_paths_csv:
            if not file_path.lower().endswith('.csv'):
                self.show_message(f"File is not a .csv file: {file_path}")
                return False
            if not Path(file_path).exists():
                self.show_message(f"File does not exist: {file_path}")
                return False

        if not CheckTifDimensions.CheckTifDimensions(file_paths_tif):
            self.show_message("All TIF files must have the same number of rows and columns.")
            return False
        
        if not self.check_tif_values(urban_start_path):
            return False
        if not self.check_tif_values(urban_constraint_path):
            return False
        if not self.scenario_simulation:
            if not self.check_tif_values(urban_end_path):
                return False
        if self.is_sliped:
            if not self.check_tif_values(self.ui.lineEdit_02_modifing_tif.text()):
                return False
        
        years = self.ui.spinbox_03_end_year.value() - self.ui.spinbox_03_start_year.value()
        if years <= 0:
            self.show_message("Simulation end time must be later than simulation start time.")
            return False
        
        if not self.check_csv_file(urban_area_path, years, 2):
            return False
        if self.ui.checkBox_03_organic_by_step.isChecked():
            if not self.check_csv_file(self.ui.lineEdit_03_organic_by_step.text(), years, 2):
                return False

        if self.is_sliped:
            if not self.check_csv_file(self.ui.lineEdit_02_modifing_csv.text(), years, 4):
                return False
        if self.ui.comboBox_04_generator_select.currentIndex() == 2:
            if not self.check_csv_file(self.ui.lineEdit_04_self_defining_generator.text(), 3, 2):
                return False
            
        if self.ui.comboBox_05_engine_select.currentIndex() == 3:
            shape_parameters_path = self.ui.lineEdit_05_shape_parameters_path.text()
            if shape_parameters_path:
                if not shape_parameters_path.lower().endswith('.csv'):
                    self.show_message(f"File is not a .csv file: {file_path}")
                    return False
                if not Path(file_path).exists():
                    self.show_message(f"File does not exist: {file_path}")
                    return False
                if not self.check_csv_file(shape_parameters_path, 5, 5):
                    return False
        return True
    
    def muse_successed_running(self, success):
        self.success = success

    def finished_simulation(self, finished):
        if self.success:
            self.ui.btn_06_save.setEnabled(True)
            if not self.scenario_simulation:
                self.ui.lineEdit_06_kappa.setText(f"{finished[0]:.8f}")
                self.ui.lineEdit_06_fom.setText(f"{finished[1]:.8f}")
                self.ui.lineEdit_06_oa.setText(f"{finished[2]:.8f}")

    def parse_data_list(self, data_list):
        parsed_list = []
        for sublist in data_list:
            if isinstance(sublist, list):
                parsed_sublist = []
                for item in sublist:
                    if isinstance(item, str):
                        try:
                            parsed_sublist.append(float(item))
                        except ValueError:
                            self.show_message(f"Error converting {item} to float")
                            return None
                parsed_list.append(parsed_sublist)
            else:
                self.show_message(f"Expected list but got {type(sublist)}")
                return None
        return parsed_list

    def on_btn_06_run_clicked(self):
        if not self.check_parameters_validity():
            return False
        
        self.success = False
        self.ui.btn_06_save.setDisabled(True)

        params = MUSE_API.ModelParameters()
        params.mode = self.scenario_simulation
        params.expansionControl = self.is_sliped
        if self.is_sliped:
            params.cityCenter = self.ui.lineEdit_02_modifing_tif.text()
            params.correctionParameters = self.ui.lineEdit_02_modifing_csv.text()
            params.cityCenterWeight = self.ui.doubleSpinbox_02_modifing_weight.value()
            
        params.initialUrbanLand = self.ui.lineEdit_01_urban_start.text()
        if not self.scenario_simulation:
            params.finalUrbanLand = self.ui.lineEdit_01_urban_end.text()
        params.developmentConstraints = self.ui.lineEdit_01_urban_constraint.text()
        params.urbanSuitability = self.ui.lineEdit_01_urban_probability.text()
        params.additionalUrbanLandArea = self.ui.lineEdit_01_urban_Area.text()
        
        if self.ui.checkBox_03_organic_by_step.isChecked():
            params.csvOrganic = self.ui.checkBox_03_organic_by_step.isChecked()
            params.additionalUrbanLandOrganicFile = self.ui.lineEdit_03_organic_by_step.text()

        params.initialNode = self.ui.spinbox_03_start_year.value()
        params.finalNode =  self.ui.spinbox_03_end_year.value()
        params.uncertainty = self.ui.doubleSpinBox_03_location_uncertainty.value()
        params.pruningCoefficient = self.ui.doubleSpinbox_03_pool_slice.value()
        params.neighborhoodType = int(self.ui.comboBox_03_neibor_type.currentText())
        params.additionalUrbanLandOrganic = self.ui.doubleSpinBox_03_organic.value()

        params.controllerType = self.ui.comboBox_04_generator_select.currentIndex()
        if params.controllerType == 0:
            params.lognormalMean = self.ui.doubleSpinBox_04_mean.value()
            params.lognormalStdDev = self.ui.doubleSpinBox_04_standard_deviation.value()
        elif params.controllerType == 1:
            params.powerLawConstant = self.ui.doubleSpinBox_04_scale_constant.value()
            params.powerLawExponent = self.ui.doubleSpinBox_04_power.value()
        elif params.controllerType == 3:
            params.historicalBlockSizes = self.ui.lineEdit_04_self_defining_generator.text()

        engineType = self.ui.comboBox_05_engine_select.currentIndex()
        if engineType == 0:
            params.blockEngineType = 0
        elif engineType == 1:
            params.blockEngineType = 2
            params.neighborhoodControlParam = self.ui.doubleSpinBox_05_parameter_beta.value()
        elif engineType == 2:
            params.blockEngineType = 3
            params.distanceControlParam = self.ui.doubleSpinBox_05_parameter_delta.value()
        elif engineType == 3:
            params.blockEngineType = 1
            shape_parameters_path = self.ui.lineEdit_05_shape_parameters_path.text()
            if shape_parameters_path:
                df = pd.read_csv(shape_parameters_path, header=None)  # 使用header=None跳过表头
                data_list = df.values.tolist()
                data_list = data_list[1:]
                parsed_data_list = self.parse_data_list(data_list)
                if parsed_data_list is not None:
                    params.PRG_Parameters = parsed_data_list
                else:
                    self.show_message("Failed to parse data_list correctly")
                    return False

        self.muse_thread = MUSEThread(MUSE_API, params)
        self.muse_thread.progress.connect(lambda progress: self.ui.textBrowser.append(progress))
        self.muse_thread.update_progress_bar.connect(lambda progress_bar: self.ui.progressBar.setValue(progress_bar))
        self.muse_thread.success.connect(self.muse_successed_running)
        self.muse_thread.finished.connect(self.finished_simulation)
        self.muse_thread.start()

    def on_btn_06_save_clicked(self):
        file_dialog = QFileDialog()
        file_dialog.setAcceptMode(QFileDialog.AcceptSave)
        file_dialog.setNameFilter("Raster files (*.tif *.tiff)")
        file_dialog.setDefaultSuffix("tif")
        file_dialog.setDirectory(self.settings.value("last_dir_save", ""))
        if file_dialog.exec():
            file_path = file_dialog.selectedFiles()[0]
            if not file_path.endswith(('.tif', '.tiff')):
                file_path += '.tif'
            self.settings.setValue("last_dir_save", file_dialog.directory().absolutePath())
            
            # Display save path setting message in text browser
            self.ui.textBrowser.append(f"Save path set to: {file_path}")

            self.write_thread = WriteThread(MUSE_API, file_path)
            self.write_thread.progress.connect(lambda message: self.ui.textBrowser.append(message))
            self.write_thread.start()
        # 06 Results and performance end

    def closeEvent(self, event):
        threads = [
            self.write_thread, 
            self.muse_thread
        ]
        for thread in threads:
            if thread and thread.isRunning():
                MUSE_API.stop()
                thread.terminate()
                thread.wait()
        self.mlcs_widget.close()
        self.pst_widget.close()
        self.mgot_widget.close()
        event.accept()
