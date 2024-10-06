# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PSSA.ui'
##
## Created by: Qt User Interface Compiler version 6.7.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSplitter, QTableWidget,
    QTableWidgetItem, QToolButton, QVBoxLayout, QWidget)

from mytextbrowser import CustomTextBrowser
import res_rc

class Ui_PSSA(object):
    def setupUi(self, PSSA):
        if not PSSA.objectName():
            PSSA.setObjectName(u"PSSA")
        PSSA.resize(936, 484)
        self.horizontalLayout_16 = QHBoxLayout(PSSA)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.splitter = QSplitter(PSSA)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Orientation.Horizontal)
        self.splitter.setHandleWidth(2)
        self.frame = QFrame(self.splitter)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_01_02 = QFrame(self.frame)
        self.frame_01_02.setObjectName(u"frame_01_02")
        self.frame_01_02.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_01_02.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_01_02)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_01_input = QFrame(self.frame_01_02)
        self.frame_01_input.setObjectName(u"frame_01_input")
        self.frame_01_input.setMaximumSize(QSize(16777215, 80))
        self.frame_01_input.setFrameShape(QFrame.Shape.NoFrame)
        self.horizontalLayout = QHBoxLayout(self.frame_01_input)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 6)
        self.lineEdit_01_input = QLineEdit(self.frame_01_input)
        self.lineEdit_01_input.setObjectName(u"lineEdit_01_input")

        self.horizontalLayout.addWidget(self.lineEdit_01_input)

        self.Button_01_input = QToolButton(self.frame_01_input)
        self.Button_01_input.setObjectName(u"Button_01_input")
        self.Button_01_input.setMinimumSize(QSize(56, 0))
        self.Button_01_input.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout.addWidget(self.Button_01_input)


        self.verticalLayout_4.addWidget(self.frame_01_input)

        self.frame_02_input_show = QFrame(self.frame_01_02)
        self.frame_02_input_show.setObjectName(u"frame_02_input_show")
        self.frame_02_input_show.setFrameShape(QFrame.Shape.NoFrame)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_02_input_show)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(9, 6, 9, 9)
        self.frame_02_01 = QFrame(self.frame_02_input_show)
        self.frame_02_01.setObjectName(u"frame_02_01")
        self.frame_02_01.setFrameShape(QFrame.Shape.NoFrame)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_02_01)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.table_02_input_show = QTableWidget(self.frame_02_01)
        self.table_02_input_show.setObjectName(u"table_02_input_show")

        self.horizontalLayout_3.addWidget(self.table_02_input_show)


        self.horizontalLayout_2.addWidget(self.frame_02_01)

        self.frame_02_02 = QFrame(self.frame_02_input_show)
        self.frame_02_02.setObjectName(u"frame_02_02")
        self.frame_02_02.setMinimumSize(QSize(0, 0))
        self.frame_02_02.setMaximumSize(QSize(16777215, 16777215))
        self.frame_02_02.setStyleSheet(u"QPushButton {\n"
"border-style: outset; /* \u8fb9\u6846\u98ce\u683c */\n"
"border-width: 0px; /* \u8fb9\u6846\u5bbd\u5ea6 */\n"
"border-radius: 5px; /* \u8fb9\u6846\u5706\u89d2 */\n"
"}\n"
"QPushButton:hover { background-color: rgb(236, 236, 236); }")
        self.frame_02_02.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalLayout_2 = QVBoxLayout(self.frame_02_02)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 3, 0, 0)
        self.frame_02_button = QFrame(self.frame_02_02)
        self.frame_02_button.setObjectName(u"frame_02_button")
        self.frame_02_button.setMinimumSize(QSize(0, 0))
        self.frame_02_button.setFrameShape(QFrame.Shape.StyledPanel)
        self.verticalLayout_3 = QVBoxLayout(self.frame_02_button)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.Button_02_remove = QPushButton(self.frame_02_button)
        self.Button_02_remove.setObjectName(u"Button_02_remove")
        icon = QIcon()
        icon.addFile(u":/resources/remove.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Button_02_remove.setIcon(icon)
        self.Button_02_remove.setIconSize(QSize(32, 32))

        self.verticalLayout_3.addWidget(self.Button_02_remove)

        self.Button_02_up = QPushButton(self.frame_02_button)
        self.Button_02_up.setObjectName(u"Button_02_up")
        icon1 = QIcon()
        icon1.addFile(u":/resources/up.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Button_02_up.setIcon(icon1)
        self.Button_02_up.setIconSize(QSize(32, 32))

        self.verticalLayout_3.addWidget(self.Button_02_up)

        self.Button_02_down = QPushButton(self.frame_02_button)
        self.Button_02_down.setObjectName(u"Button_02_down")
        icon2 = QIcon()
        icon2.addFile(u":/resources/down.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Button_02_down.setIcon(icon2)
        self.Button_02_down.setIconSize(QSize(32, 32))

        self.verticalLayout_3.addWidget(self.Button_02_down)

        self.Button_02_check = QPushButton(self.frame_02_button)
        self.Button_02_check.setObjectName(u"Button_02_check")
        icon3 = QIcon()
        icon3.addFile(u":/resources/check.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Button_02_check.setIcon(icon3)
        self.Button_02_check.setIconSize(QSize(32, 32))
        self.Button_02_check.setCheckable(False)
        self.Button_02_check.setAutoRepeat(True)
        self.Button_02_check.setAutoExclusive(False)

        self.verticalLayout_3.addWidget(self.Button_02_check)


        self.verticalLayout_2.addWidget(self.frame_02_button)


        self.horizontalLayout_2.addWidget(self.frame_02_02)


        self.verticalLayout_4.addWidget(self.frame_02_input_show)


        self.verticalLayout_7.addWidget(self.frame_01_02)

        self.frame_03_04 = QFrame(self.frame)
        self.frame_03_04.setObjectName(u"frame_03_04")
        self.frame_03_04.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_03_04.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_03_04)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_03_pdc_parameters = QFrame(self.frame_03_04)
        self.frame_03_pdc_parameters.setObjectName(u"frame_03_pdc_parameters")
        self.frame_03_pdc_parameters.setMinimumSize(QSize(0, 0))
        self.frame_03_pdc_parameters.setMaximumSize(QSize(16777215, 80))
        self.frame_03_pdc_parameters.setFrameShape(QFrame.Shape.NoFrame)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_03_pdc_parameters)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.checkBox_03_print_patch = QCheckBox(self.frame_03_pdc_parameters)
        self.checkBox_03_print_patch.setObjectName(u"checkBox_03_print_patch")

        self.horizontalLayout_13.addWidget(self.checkBox_03_print_patch)

        self.checkBox_03_calculate_gaussian_parrameters = QCheckBox(self.frame_03_pdc_parameters)
        self.checkBox_03_calculate_gaussian_parrameters.setObjectName(u"checkBox_03_calculate_gaussian_parrameters")

        self.horizontalLayout_13.addWidget(self.checkBox_03_calculate_gaussian_parrameters)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label__03_neighbor_type = QLabel(self.frame_03_pdc_parameters)
        self.label__03_neighbor_type.setObjectName(u"label__03_neighbor_type")

        self.horizontalLayout_12.addWidget(self.label__03_neighbor_type)

        self.comBox_03_neighbor_type = QComboBox(self.frame_03_pdc_parameters)
        self.comBox_03_neighbor_type.addItem("")
        self.comBox_03_neighbor_type.addItem("")
        self.comBox_03_neighbor_type.setObjectName(u"comBox_03_neighbor_type")

        self.horizontalLayout_12.addWidget(self.comBox_03_neighbor_type)


        self.horizontalLayout_13.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_13.setStretch(0, 3)
        self.horizontalLayout_13.setStretch(1, 6)
        self.horizontalLayout_13.setStretch(2, 4)

        self.verticalLayout_5.addWidget(self.frame_03_pdc_parameters)

        self.frame_04_patch = QFrame(self.frame_03_04)
        self.frame_04_patch.setObjectName(u"frame_04_patch")
        self.frame_04_patch.setFrameShape(QFrame.Shape.NoFrame)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_04_patch)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.frame_04_save_location = QFrame(self.frame_04_patch)
        self.frame_04_save_location.setObjectName(u"frame_04_save_location")
        self.frame_04_save_location.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_04_save_location.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_04_save_location)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_04_save_location = QLabel(self.frame_04_save_location)
        self.label_04_save_location.setObjectName(u"label_04_save_location")

        self.horizontalLayout_8.addWidget(self.label_04_save_location)

        self.lineEdit_04_save_location = QLineEdit(self.frame_04_save_location)
        self.lineEdit_04_save_location.setObjectName(u"lineEdit_04_save_location")

        self.horizontalLayout_8.addWidget(self.lineEdit_04_save_location)

        self.Button_04_save_location = QToolButton(self.frame_04_save_location)
        self.Button_04_save_location.setObjectName(u"Button_04_save_location")
        self.Button_04_save_location.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_8.addWidget(self.Button_04_save_location)


        self.horizontalLayout_15.addWidget(self.frame_04_save_location)

        self.frame_04_center_data = QFrame(self.frame_04_patch)
        self.frame_04_center_data.setObjectName(u"frame_04_center_data")
        self.frame_04_center_data.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_04_center_data.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_04_center_data)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_04_center_data = QLabel(self.frame_04_center_data)
        self.label_04_center_data.setObjectName(u"label_04_center_data")

        self.horizontalLayout_14.addWidget(self.label_04_center_data)

        self.lineEdit_04_center_data = QLineEdit(self.frame_04_center_data)
        self.lineEdit_04_center_data.setObjectName(u"lineEdit_04_center_data")

        self.horizontalLayout_14.addWidget(self.lineEdit_04_center_data)

        self.toolButton_04_center_data = QToolButton(self.frame_04_center_data)
        self.toolButton_04_center_data.setObjectName(u"toolButton_04_center_data")

        self.horizontalLayout_14.addWidget(self.toolButton_04_center_data)


        self.horizontalLayout_15.addWidget(self.frame_04_center_data)


        self.verticalLayout_5.addWidget(self.frame_04_patch)


        self.verticalLayout_7.addWidget(self.frame_03_04)

        self.frame_05_run = QFrame(self.frame)
        self.frame_05_run.setObjectName(u"frame_05_run")
        self.frame_05_run.setMaximumSize(QSize(16777215, 80))
        self.frame_05_run.setFrameShape(QFrame.Shape.StyledPanel)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_05_run)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.Button_05_calculate = QPushButton(self.frame_05_run)
        self.Button_05_calculate.setObjectName(u"Button_05_calculate")

        self.horizontalLayout_4.addWidget(self.Button_05_calculate)


        self.verticalLayout_7.addWidget(self.frame_05_run)

        self.frame_06_result = QFrame(self.frame)
        self.frame_06_result.setObjectName(u"frame_06_result")
        self.frame_06_result.setFrameShape(QFrame.Shape.StyledPanel)
        self.verticalLayout = QVBoxLayout(self.frame_06_result)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_06_lognormal_distribution = QFrame(self.frame_06_result)
        self.frame_06_lognormal_distribution.setObjectName(u"frame_06_lognormal_distribution")
        self.frame_06_lognormal_distribution.setFrameShape(QFrame.Shape.NoFrame)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_06_lognormal_distribution)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(9, 0, -1, 0)
        self.label_06_standard_deviation_2 = QLabel(self.frame_06_lognormal_distribution)
        self.label_06_standard_deviation_2.setObjectName(u"label_06_standard_deviation_2")

        self.horizontalLayout_7.addWidget(self.label_06_standard_deviation_2)

        self.frame_06_mean = QFrame(self.frame_06_lognormal_distribution)
        self.frame_06_mean.setObjectName(u"frame_06_mean")
        self.frame_06_mean.setFrameShape(QFrame.Shape.NoFrame)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_06_mean)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, 3, -1, 3)
        self.label_06_mean = QLabel(self.frame_06_mean)
        self.label_06_mean.setObjectName(u"label_06_mean")

        self.horizontalLayout_5.addWidget(self.label_06_mean)

        self.lineEdit_06_mean = QLineEdit(self.frame_06_mean)
        self.lineEdit_06_mean.setObjectName(u"lineEdit_06_mean")
        self.lineEdit_06_mean.setMinimumSize(QSize(90, 0))
        self.lineEdit_06_mean.setReadOnly(True)

        self.horizontalLayout_5.addWidget(self.lineEdit_06_mean)


        self.horizontalLayout_7.addWidget(self.frame_06_mean)

        self.frame_06_standard_deviation = QFrame(self.frame_06_lognormal_distribution)
        self.frame_06_standard_deviation.setObjectName(u"frame_06_standard_deviation")
        self.frame_06_standard_deviation.setFrameShape(QFrame.Shape.NoFrame)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_06_standard_deviation)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(-1, 3, -1, 3)
        self.label_06_standard_deviation = QLabel(self.frame_06_standard_deviation)
        self.label_06_standard_deviation.setObjectName(u"label_06_standard_deviation")

        self.horizontalLayout_6.addWidget(self.label_06_standard_deviation)

        self.lineEdit_06_standard_deviation = QLineEdit(self.frame_06_standard_deviation)
        self.lineEdit_06_standard_deviation.setObjectName(u"lineEdit_06_standard_deviation")
        self.lineEdit_06_standard_deviation.setMinimumSize(QSize(90, 0))
        self.lineEdit_06_standard_deviation.setReadOnly(True)

        self.horizontalLayout_6.addWidget(self.lineEdit_06_standard_deviation)


        self.horizontalLayout_7.addWidget(self.frame_06_standard_deviation)


        self.verticalLayout.addWidget(self.frame_06_lognormal_distribution)

        self.frame_06_power_law_distribution = QFrame(self.frame_06_result)
        self.frame_06_power_law_distribution.setObjectName(u"frame_06_power_law_distribution")
        self.frame_06_power_law_distribution.setFrameShape(QFrame.Shape.NoFrame)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_06_power_law_distribution)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(-1, 0, -1, 0)
        self.label_3 = QLabel(self.frame_06_power_law_distribution)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_9.addWidget(self.label_3)

        self.frame_06_scale_constant = QFrame(self.frame_06_power_law_distribution)
        self.frame_06_scale_constant.setObjectName(u"frame_06_scale_constant")
        self.frame_06_scale_constant.setFrameShape(QFrame.Shape.NoFrame)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_06_scale_constant)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(-1, 3, -1, 3)
        self.label_06_scale_constant = QLabel(self.frame_06_scale_constant)
        self.label_06_scale_constant.setObjectName(u"label_06_scale_constant")

        self.horizontalLayout_10.addWidget(self.label_06_scale_constant)

        self.lineEdit_06_scale_constant = QLineEdit(self.frame_06_scale_constant)
        self.lineEdit_06_scale_constant.setObjectName(u"lineEdit_06_scale_constant")
        self.lineEdit_06_scale_constant.setMinimumSize(QSize(90, 0))
        self.lineEdit_06_scale_constant.setReadOnly(True)

        self.horizontalLayout_10.addWidget(self.lineEdit_06_scale_constant)


        self.horizontalLayout_9.addWidget(self.frame_06_scale_constant)

        self.frame_06_power = QFrame(self.frame_06_power_law_distribution)
        self.frame_06_power.setObjectName(u"frame_06_power")
        self.frame_06_power.setFrameShape(QFrame.Shape.NoFrame)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_06_power)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(-1, 3, -1, 3)
        self.label_06_power = QLabel(self.frame_06_power)
        self.label_06_power.setObjectName(u"label_06_power")

        self.horizontalLayout_11.addWidget(self.label_06_power)

        self.lineEdit_06_power = QLineEdit(self.frame_06_power)
        self.lineEdit_06_power.setObjectName(u"lineEdit_06_power")
        self.lineEdit_06_power.setMinimumSize(QSize(90, 0))
        self.lineEdit_06_power.setReadOnly(True)

        self.horizontalLayout_11.addWidget(self.lineEdit_06_power)


        self.horizontalLayout_9.addWidget(self.frame_06_power)


        self.verticalLayout.addWidget(self.frame_06_power_law_distribution)


        self.verticalLayout_7.addWidget(self.frame_06_result)

        self.splitter.addWidget(self.frame)
        self.frame_07_output = QFrame(self.splitter)
        self.frame_07_output.setObjectName(u"frame_07_output")
        self.frame_07_output.setFrameShape(QFrame.Shape.StyledPanel)
        self.verticalLayout_6 = QVBoxLayout(self.frame_07_output)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.textBrowser = CustomTextBrowser(self.frame_07_output)
        self.textBrowser.setObjectName(u"textBrowser")

        self.verticalLayout_6.addWidget(self.textBrowser)

        self.widget = QWidget(self.frame_07_output)
        self.widget.setObjectName(u"widget")

        self.verticalLayout_6.addWidget(self.widget)

        self.splitter.addWidget(self.frame_07_output)

        self.horizontalLayout_16.addWidget(self.splitter)


        self.retranslateUi(PSSA)

        self.comBox_03_neighbor_type.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(PSSA)
    # setupUi

    def retranslateUi(self, PSSA):
        PSSA.setWindowTitle(QCoreApplication.translate("PSSA", u"Patch Size Statistical Analysis (PSSA) ", None))
        self.Button_01_input.setText(QCoreApplication.translate("PSSA", u"...", None))
        self.Button_02_remove.setText("")
        self.Button_02_up.setText("")
        self.Button_02_down.setText("")
        self.Button_02_check.setText("")
        self.checkBox_03_print_patch.setText(QCoreApplication.translate("PSSA", u"Print patch", None))
        self.checkBox_03_calculate_gaussian_parrameters.setText(QCoreApplication.translate("PSSA", u"Calculate Gaussian parameters", None))
        self.label__03_neighbor_type.setText(QCoreApplication.translate("PSSA", u"Neighbor type", None))
        self.comBox_03_neighbor_type.setItemText(0, QCoreApplication.translate("PSSA", u"4", None))
        self.comBox_03_neighbor_type.setItemText(1, QCoreApplication.translate("PSSA", u"8", None))

        self.label_04_save_location.setText(QCoreApplication.translate("PSSA", u"Save location", None))
        self.Button_04_save_location.setText(QCoreApplication.translate("PSSA", u"...", None))
        self.label_04_center_data.setText(QCoreApplication.translate("PSSA", u"Center data", None))
        self.toolButton_04_center_data.setText(QCoreApplication.translate("PSSA", u"...", None))
        self.Button_05_calculate.setText(QCoreApplication.translate("PSSA", u"Calculate", None))
        self.label_06_standard_deviation_2.setText(QCoreApplication.translate("PSSA", u"Lognormal distribution (cell):", None))
        self.label_06_mean.setText(QCoreApplication.translate("PSSA", u"Mean", None))
        self.label_06_standard_deviation.setText(QCoreApplication.translate("PSSA", u"Standard deviation", None))
        self.label_3.setText(QCoreApplication.translate("PSSA", u"Power-law distribution (cell):", None))
        self.label_06_scale_constant.setText(QCoreApplication.translate("PSSA", u"Scale constant", None))
        self.label_06_power.setText(QCoreApplication.translate("PSSA", u"Power", None))
    # retranslateUi

