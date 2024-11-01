# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QCheckBox, QComboBox,
    QDoubleSpinBox, QFrame, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QLayout, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QProgressBar,
    QPushButton, QSizePolicy, QSpinBox, QSplitter,
    QStatusBar, QToolButton, QVBoxLayout, QWidget)

from src.mytextbrowser import MyTextBrowser
import resources.qrc.res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1194, 761)
        font = QFont()
        font.setPointSize(9)
        font.setBold(False)
        MainWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u":/ico/MUSE.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        self.actionnewFile = QAction(MainWindow)
        self.actionnewFile.setObjectName(u"actionnewFile")
        self.actionopen = QAction(MainWindow)
        self.actionopen.setObjectName(u"actionopen")
        self.actionge_00_ParsByGa = QAction(MainWindow)
        self.actionge_00_ParsByGa.setObjectName(u"actionge_00_ParsByGa")
        self.action_00_about = QAction(MainWindow)
        self.action_00_about.setObjectName(u"action_00_about")
        self.action_00_Chinese_Simplified = QAction(MainWindow)
        self.action_00_Chinese_Simplified.setObjectName(u"action_00_Chinese_Simplified")
        self.action_00_Chinese_Simplified.setCheckable(False)
        self.action_00_English = QAction(MainWindow)
        self.action_00_English.setObjectName(u"action_00_English")
        self.action_00_English.setCheckable(False)
        self.action_00_simulation = QAction(MainWindow)
        self.action_00_simulation.setObjectName(u"action_00_simulation")
        self.action_00_verification = QAction(MainWindow)
        self.action_00_verification.setObjectName(u"action_00_verification")
        self.action_00_exit = QAction(MainWindow)
        self.action_00_exit.setObjectName(u"action_00_exit")
        self.action_00_save = QAction(MainWindow)
        self.action_00_save.setObjectName(u"action_00_save")
        self.action_00_open = QAction(MainWindow)
        self.action_00_open.setObjectName(u"action_00_open")
        self.actionpatchInfo = QAction(MainWindow)
        self.actionpatchInfo.setObjectName(u"actionpatchInfo")
        self.actionversionInfo = QAction(MainWindow)
        self.actionversionInfo.setObjectName(u"actionversionInfo")
        self.action_00_patch_info = QAction(MainWindow)
        self.action_00_patch_info.setObjectName(u"action_00_patch_info")
        self.action_00_version = QAction(MainWindow)
        self.action_00_version.setObjectName(u"action_00_version")
        self.action_00_user_guid = QAction(MainWindow)
        self.action_00_user_guid.setObjectName(u"action_00_user_guid")
        self.action_00_MUSE_Toolbox = QAction(MainWindow)
        self.action_00_MUSE_Toolbox.setObjectName(u"action_00_MUSE_Toolbox")
        self.action_00_mlcs = QAction(MainWindow)
        self.action_00_mlcs.setObjectName(u"action_00_mlcs")
        self.action_00_pst = QAction(MainWindow)
        self.action_00_pst.setObjectName(u"action_00_pst")
        self.action_00_open_paper = QAction(MainWindow)
        self.action_00_open_paper.setObjectName(u"action_00_open_paper")
        self.action_00_open_testdir = QAction(MainWindow)
        self.action_00_open_testdir.setObjectName(u"action_00_open_testdir")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Orientation.Horizontal)
        self.frame_20 = QFrame(self.splitter)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_20)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SizeConstraint.SetMinAndMaxSize)
        self.box_01_data_Input = QGroupBox(self.frame_20)
        self.box_01_data_Input.setObjectName(u"box_01_data_Input")
        self.box_01_data_Input.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.box_01_data_Input.setCheckable(False)
        self.verticalLayout_2 = QVBoxLayout(self.box_01_data_Input)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.urban_Start_Frame = QFrame(self.box_01_data_Input)
        self.urban_Start_Frame.setObjectName(u"urban_Start_Frame")
        self.urban_Start_Frame.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalLayout_14 = QVBoxLayout(self.urban_Start_Frame)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_01_urban_start = QLabel(self.urban_Start_Frame)
        self.label_01_urban_start.setObjectName(u"label_01_urban_start")

        self.verticalLayout_14.addWidget(self.label_01_urban_start)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setSpacing(6)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.lineEdit_01_urban_start = QLineEdit(self.urban_Start_Frame)
        self.lineEdit_01_urban_start.setObjectName(u"lineEdit_01_urban_start")

        self.horizontalLayout_19.addWidget(self.lineEdit_01_urban_start)

        self.btn_01_urban_start = QToolButton(self.urban_Start_Frame)
        self.btn_01_urban_start.setObjectName(u"btn_01_urban_start")

        self.horizontalLayout_19.addWidget(self.btn_01_urban_start)


        self.verticalLayout_14.addLayout(self.horizontalLayout_19)


        self.gridLayout_3.addWidget(self.urban_Start_Frame, 0, 0, 1, 1)

        self.urban_Constraint_Frame = QFrame(self.box_01_data_Input)
        self.urban_Constraint_Frame.setObjectName(u"urban_Constraint_Frame")
        self.urban_Constraint_Frame.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalLayout_13 = QVBoxLayout(self.urban_Constraint_Frame)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_01_urban_contraint = QLabel(self.urban_Constraint_Frame)
        self.label_01_urban_contraint.setObjectName(u"label_01_urban_contraint")

        self.verticalLayout_13.addWidget(self.label_01_urban_contraint)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.lineEdit_01_urban_constraint = QLineEdit(self.urban_Constraint_Frame)
        self.lineEdit_01_urban_constraint.setObjectName(u"lineEdit_01_urban_constraint")

        self.horizontalLayout_21.addWidget(self.lineEdit_01_urban_constraint)

        self.btn_01_urban_constraint = QToolButton(self.urban_Constraint_Frame)
        self.btn_01_urban_constraint.setObjectName(u"btn_01_urban_constraint")

        self.horizontalLayout_21.addWidget(self.btn_01_urban_constraint)


        self.verticalLayout_13.addLayout(self.horizontalLayout_21)


        self.gridLayout_3.addWidget(self.urban_Constraint_Frame, 0, 1, 1, 1)

        self.urban_Area_Frame = QFrame(self.box_01_data_Input)
        self.urban_Area_Frame.setObjectName(u"urban_Area_Frame")
        self.urban_Area_Frame.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalLayout_10 = QVBoxLayout(self.urban_Area_Frame)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_01_urban_area = QLabel(self.urban_Area_Frame)
        self.label_01_urban_area.setObjectName(u"label_01_urban_area")

        self.verticalLayout_10.addWidget(self.label_01_urban_area)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.lineEdit_01_urban_Area = QLineEdit(self.urban_Area_Frame)
        self.lineEdit_01_urban_Area.setObjectName(u"lineEdit_01_urban_Area")

        self.horizontalLayout_18.addWidget(self.lineEdit_01_urban_Area)

        self.btn_01_urban_area = QToolButton(self.urban_Area_Frame)
        self.btn_01_urban_area.setObjectName(u"btn_01_urban_area")

        self.horizontalLayout_18.addWidget(self.btn_01_urban_area)


        self.verticalLayout_10.addLayout(self.horizontalLayout_18)


        self.gridLayout_3.addWidget(self.urban_Area_Frame, 1, 0, 1, 1)

        self.urban_Probability_Frame = QFrame(self.box_01_data_Input)
        self.urban_Probability_Frame.setObjectName(u"urban_Probability_Frame")
        self.urban_Probability_Frame.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalLayout_12 = QVBoxLayout(self.urban_Probability_Frame)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_01_urban_probability = QLabel(self.urban_Probability_Frame)
        self.label_01_urban_probability.setObjectName(u"label_01_urban_probability")

        self.verticalLayout_12.addWidget(self.label_01_urban_probability)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.lineEdit_01_urban_probability = QLineEdit(self.urban_Probability_Frame)
        self.lineEdit_01_urban_probability.setObjectName(u"lineEdit_01_urban_probability")

        self.horizontalLayout_22.addWidget(self.lineEdit_01_urban_probability)

        self.btn_01_urban_probability = QToolButton(self.urban_Probability_Frame)
        self.btn_01_urban_probability.setObjectName(u"btn_01_urban_probability")

        self.horizontalLayout_22.addWidget(self.btn_01_urban_probability)


        self.verticalLayout_12.addLayout(self.horizontalLayout_22)


        self.gridLayout_3.addWidget(self.urban_Probability_Frame, 1, 1, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout_3)

        self.urban_End_Frame = QFrame(self.box_01_data_Input)
        self.urban_End_Frame.setObjectName(u"urban_End_Frame")
        self.urban_End_Frame.setFrameShape(QFrame.Shape.NoFrame)
        self.horizontalLayout = QHBoxLayout(self.urban_End_Frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label_01_urban_end = QLabel(self.urban_End_Frame)
        self.label_01_urban_end.setObjectName(u"label_01_urban_end")

        self.horizontalLayout_20.addWidget(self.label_01_urban_end)

        self.lineEdit_01_urban_end = QLineEdit(self.urban_End_Frame)
        self.lineEdit_01_urban_end.setObjectName(u"lineEdit_01_urban_end")

        self.horizontalLayout_20.addWidget(self.lineEdit_01_urban_end)

        self.btn_01_urban_end = QToolButton(self.urban_End_Frame)
        self.btn_01_urban_end.setObjectName(u"btn_01_urban_end")

        self.horizontalLayout_20.addWidget(self.btn_01_urban_end)


        self.horizontalLayout.addLayout(self.horizontalLayout_20)


        self.verticalLayout_2.addWidget(self.urban_End_Frame)


        self.verticalLayout.addWidget(self.box_01_data_Input)

        self.box_02_modifing = QGroupBox(self.frame_20)
        self.box_02_modifing.setObjectName(u"box_02_modifing")
        self.box_02_modifing.setMinimumSize(QSize(0, 62))
        self.box_02_modifing.setMaximumSize(QSize(16777215, 62))
        self.box_02_modifing.setStyleSheet(u"")
        self.box_02_modifing.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.horizontalLayout_37 = QHBoxLayout(self.box_02_modifing)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.horizontalLayout_37.setContentsMargins(-1, 0, -1, 9)
        self.frame_02 = QFrame(self.box_02_modifing)
        self.frame_02.setObjectName(u"frame_02")
        self.frame_02.setMaximumSize(QSize(16777215, 16777215))
        self.frame_02.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalLayout_22 = QVBoxLayout(self.frame_02)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")

        self.horizontalLayout_37.addWidget(self.frame_02)

        self.modifing_tif_frame = QFrame(self.box_02_modifing)
        self.modifing_tif_frame.setObjectName(u"modifing_tif_frame")
        self.modifing_tif_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.horizontalLayout_42 = QHBoxLayout(self.modifing_tif_frame)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.horizontalLayout_42.setContentsMargins(-1, 9, -1, 9)
        self.label_02_modifing_tif = QLabel(self.modifing_tif_frame)
        self.label_02_modifing_tif.setObjectName(u"label_02_modifing_tif")

        self.horizontalLayout_42.addWidget(self.label_02_modifing_tif)

        self.lineEdit_02_modifing_tif = QLineEdit(self.modifing_tif_frame)
        self.lineEdit_02_modifing_tif.setObjectName(u"lineEdit_02_modifing_tif")

        self.horizontalLayout_42.addWidget(self.lineEdit_02_modifing_tif)

        self.btn_02_modifing_tif = QToolButton(self.modifing_tif_frame)
        self.btn_02_modifing_tif.setObjectName(u"btn_02_modifing_tif")

        self.horizontalLayout_42.addWidget(self.btn_02_modifing_tif)


        self.horizontalLayout_37.addWidget(self.modifing_tif_frame)

        self.modifing_csv_frame = QFrame(self.box_02_modifing)
        self.modifing_csv_frame.setObjectName(u"modifing_csv_frame")
        self.modifing_csv_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.horizontalLayout_41 = QHBoxLayout(self.modifing_csv_frame)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.horizontalLayout_41.setContentsMargins(-1, 9, -1, 9)
        self.label_02_modifing_csv = QLabel(self.modifing_csv_frame)
        self.label_02_modifing_csv.setObjectName(u"label_02_modifing_csv")

        self.horizontalLayout_41.addWidget(self.label_02_modifing_csv)

        self.lineEdit_02_modifing_csv = QLineEdit(self.modifing_csv_frame)
        self.lineEdit_02_modifing_csv.setObjectName(u"lineEdit_02_modifing_csv")

        self.horizontalLayout_41.addWidget(self.lineEdit_02_modifing_csv)

        self.btn_02_modifing_csv = QToolButton(self.modifing_csv_frame)
        self.btn_02_modifing_csv.setObjectName(u"btn_02_modifing_csv")

        self.horizontalLayout_41.addWidget(self.btn_02_modifing_csv)


        self.horizontalLayout_37.addWidget(self.modifing_csv_frame)

        self.modifing_weight_frame = QFrame(self.box_02_modifing)
        self.modifing_weight_frame.setObjectName(u"modifing_weight_frame")
        self.modifing_weight_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.horizontalLayout_38 = QHBoxLayout(self.modifing_weight_frame)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.label_02_modifing_weight = QLabel(self.modifing_weight_frame)
        self.label_02_modifing_weight.setObjectName(u"label_02_modifing_weight")

        self.horizontalLayout_38.addWidget(self.label_02_modifing_weight)

        self.doubleSpinbox_02_modifing_weight = QDoubleSpinBox(self.modifing_weight_frame)
        self.doubleSpinbox_02_modifing_weight.setObjectName(u"doubleSpinbox_02_modifing_weight")
        self.doubleSpinbox_02_modifing_weight.setMinimumSize(QSize(125, 0))
        self.doubleSpinbox_02_modifing_weight.setDecimals(6)
        self.doubleSpinbox_02_modifing_weight.setMinimum(0.010000000000000)
        self.doubleSpinbox_02_modifing_weight.setMaximum(1.000000000000000)
        self.doubleSpinbox_02_modifing_weight.setSingleStep(0.010000000000000)
        self.doubleSpinbox_02_modifing_weight.setValue(0.500000000000000)

        self.horizontalLayout_38.addWidget(self.doubleSpinbox_02_modifing_weight)


        self.horizontalLayout_37.addWidget(self.modifing_weight_frame)


        self.verticalLayout.addWidget(self.box_02_modifing)

        self.box_03_model_parameters = QGroupBox(self.frame_20)
        self.box_03_model_parameters.setObjectName(u"box_03_model_parameters")
        self.box_03_model_parameters.setMaximumSize(QSize(16777215, 16777215))
        self.box_03_model_parameters.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.box_03_model_parameters.setFlat(False)
        self.box_03_model_parameters.setCheckable(False)
        self.horizontalLayout_16 = QHBoxLayout(self.box_03_model_parameters)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_03_strat_year = QLabel(self.box_03_model_parameters)
        self.label_03_strat_year.setObjectName(u"label_03_strat_year")
        self.label_03_strat_year.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_10.addWidget(self.label_03_strat_year)

        self.spinbox_03_start_year = QSpinBox(self.box_03_model_parameters)
        self.spinbox_03_start_year.setObjectName(u"spinbox_03_start_year")
        self.spinbox_03_start_year.setMinimumSize(QSize(105, 0))
        self.spinbox_03_start_year.setMaximumSize(QSize(105, 16777215))
        self.spinbox_03_start_year.setMinimum(1)
        self.spinbox_03_start_year.setMaximum(36767)

        self.horizontalLayout_10.addWidget(self.spinbox_03_start_year)


        self.verticalLayout_3.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_03_end_Year = QLabel(self.box_03_model_parameters)
        self.label_03_end_Year.setObjectName(u"label_03_end_Year")
        self.label_03_end_Year.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_9.addWidget(self.label_03_end_Year)

        self.spinbox_03_end_year = QSpinBox(self.box_03_model_parameters)
        self.spinbox_03_end_year.setObjectName(u"spinbox_03_end_year")
        self.spinbox_03_end_year.setMinimumSize(QSize(105, 0))
        self.spinbox_03_end_year.setMaximumSize(QSize(105, 16777215))
        self.spinbox_03_end_year.setMinimum(2)
        self.spinbox_03_end_year.setMaximum(36767)
        self.spinbox_03_end_year.setValue(11)

        self.horizontalLayout_9.addWidget(self.spinbox_03_end_year)


        self.verticalLayout_3.addLayout(self.horizontalLayout_9)


        self.horizontalLayout_16.addLayout(self.verticalLayout_3)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_03_location_uncertainty = QLabel(self.box_03_model_parameters)
        self.label_03_location_uncertainty.setObjectName(u"label_03_location_uncertainty")

        self.horizontalLayout_13.addWidget(self.label_03_location_uncertainty)

        self.doubleSpinBox_03_location_uncertainty = QDoubleSpinBox(self.box_03_model_parameters)
        self.doubleSpinBox_03_location_uncertainty.setObjectName(u"doubleSpinBox_03_location_uncertainty")
        self.doubleSpinBox_03_location_uncertainty.setMinimumSize(QSize(115, 0))
        self.doubleSpinBox_03_location_uncertainty.setMaximumSize(QSize(115, 16777215))
        self.doubleSpinBox_03_location_uncertainty.setDecimals(4)
        self.doubleSpinBox_03_location_uncertainty.setMaximum(1.000000000000000)
        self.doubleSpinBox_03_location_uncertainty.setSingleStep(0.100000000000000)
        self.doubleSpinBox_03_location_uncertainty.setValue(1.000000000000000)

        self.horizontalLayout_13.addWidget(self.doubleSpinBox_03_location_uncertainty)


        self.verticalLayout_5.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_03_neibor_type = QLabel(self.box_03_model_parameters)
        self.label_03_neibor_type.setObjectName(u"label_03_neibor_type")
        self.label_03_neibor_type.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_11.addWidget(self.label_03_neibor_type)

        self.comboBox_03_neibor_type = QComboBox(self.box_03_model_parameters)
        self.comboBox_03_neibor_type.addItem("")
        self.comboBox_03_neibor_type.addItem("")
        self.comboBox_03_neibor_type.setObjectName(u"comboBox_03_neibor_type")
        self.comboBox_03_neibor_type.setMinimumSize(QSize(115, 0))
        self.comboBox_03_neibor_type.setMaximumSize(QSize(115, 16777215))

        self.horizontalLayout_11.addWidget(self.comboBox_03_neibor_type)


        self.verticalLayout_5.addLayout(self.horizontalLayout_11)


        self.horizontalLayout_16.addLayout(self.verticalLayout_5)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_03_pool_Slice = QLabel(self.box_03_model_parameters)
        self.label_03_pool_Slice.setObjectName(u"label_03_pool_Slice")
        self.label_03_pool_Slice.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.label_03_pool_Slice)

        self.doubleSpinbox_03_pool_slice = QDoubleSpinBox(self.box_03_model_parameters)
        self.doubleSpinbox_03_pool_slice.setObjectName(u"doubleSpinbox_03_pool_slice")
        self.doubleSpinbox_03_pool_slice.setMinimumSize(QSize(125, 0))
        self.doubleSpinbox_03_pool_slice.setMaximumSize(QSize(125, 16777215))
        self.doubleSpinbox_03_pool_slice.setDecimals(6)
        self.doubleSpinbox_03_pool_slice.setMinimum(0.000001000000000)
        self.doubleSpinbox_03_pool_slice.setMaximum(1.000000000000000)
        self.doubleSpinbox_03_pool_slice.setSingleStep(0.010000000000000)
        self.doubleSpinbox_03_pool_slice.setValue(0.130000000000000)

        self.horizontalLayout_8.addWidget(self.doubleSpinbox_03_pool_slice)


        self.verticalLayout_6.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.checkBox_03_organic_by_step = QCheckBox(self.box_03_model_parameters)
        self.checkBox_03_organic_by_step.setObjectName(u"checkBox_03_organic_by_step")
        self.checkBox_03_organic_by_step.setChecked(True)

        self.horizontalLayout_12.addWidget(self.checkBox_03_organic_by_step)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.doubleSpinBox_03_organic = QDoubleSpinBox(self.box_03_model_parameters)
        self.doubleSpinBox_03_organic.setObjectName(u"doubleSpinBox_03_organic")
        self.doubleSpinBox_03_organic.setMinimumSize(QSize(125, 0))
        self.doubleSpinBox_03_organic.setMaximumSize(QSize(125, 16777215))
        self.doubleSpinBox_03_organic.setDecimals(6)
        self.doubleSpinBox_03_organic.setMinimum(0.000010000000000)
        self.doubleSpinBox_03_organic.setMaximum(1.000000000000000)
        self.doubleSpinBox_03_organic.setSingleStep(0.010000000000000)
        self.doubleSpinBox_03_organic.setValue(0.720000000000000)

        self.horizontalLayout_3.addWidget(self.doubleSpinBox_03_organic)

        self.lineEdit_03_organic_by_step = QLineEdit(self.box_03_model_parameters)
        self.lineEdit_03_organic_by_step.setObjectName(u"lineEdit_03_organic_by_step")
        self.lineEdit_03_organic_by_step.setMinimumSize(QSize(95, 0))
        self.lineEdit_03_organic_by_step.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_3.addWidget(self.lineEdit_03_organic_by_step)

        self.toolButton_03_organic_by_step = QToolButton(self.box_03_model_parameters)
        self.toolButton_03_organic_by_step.setObjectName(u"toolButton_03_organic_by_step")

        self.horizontalLayout_3.addWidget(self.toolButton_03_organic_by_step)


        self.horizontalLayout_12.addLayout(self.horizontalLayout_3)


        self.verticalLayout_6.addLayout(self.horizontalLayout_12)


        self.horizontalLayout_16.addLayout(self.verticalLayout_6)

        self.horizontalLayout_16.setStretch(0, 2)
        self.horizontalLayout_16.setStretch(1, 3)
        self.horizontalLayout_16.setStretch(2, 4)

        self.verticalLayout.addWidget(self.box_03_model_parameters)

        self.box_04_patch_size_generator = QGroupBox(self.frame_20)
        self.box_04_patch_size_generator.setObjectName(u"box_04_patch_size_generator")
        self.box_04_patch_size_generator.setStyleSheet(u"")
        self.box_04_patch_size_generator.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)
        self.horizontalLayout_14 = QHBoxLayout(self.box_04_patch_size_generator)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.frame_04_generator_select = QFrame(self.box_04_patch_size_generator)
        self.frame_04_generator_select.setObjectName(u"frame_04_generator_select")
        self.frame_04_generator_select.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_04_generator_select.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_04_generator_select.setLineWidth(1)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_04_generator_select)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.horizontalLayout_6.setContentsMargins(-1, 9, -1, -1)
        self.comboBox_04_generator_select = QComboBox(self.frame_04_generator_select)
        self.comboBox_04_generator_select.addItem("")
        self.comboBox_04_generator_select.addItem("")
        self.comboBox_04_generator_select.addItem("")
        self.comboBox_04_generator_select.setObjectName(u"comboBox_04_generator_select")

        self.horizontalLayout_6.addWidget(self.comboBox_04_generator_select)


        self.horizontalLayout_14.addWidget(self.frame_04_generator_select)

        self.frame_04_lognormal = QFrame(self.box_04_patch_size_generator)
        self.frame_04_lognormal.setObjectName(u"frame_04_lognormal")
        self.frame_04_lognormal.setStyleSheet(u"")
        self.frame_04_lognormal.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_04_lognormal.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_04_lognormal.setLineWidth(1)
        self.gridLayout_2 = QGridLayout(self.frame_04_lognormal)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.doubleSpinBox_04_mean = QDoubleSpinBox(self.frame_04_lognormal)
        self.doubleSpinBox_04_mean.setObjectName(u"doubleSpinBox_04_mean")
        self.doubleSpinBox_04_mean.setMinimum(1.000000000000000)
        self.doubleSpinBox_04_mean.setMaximum(10000000.000000000000000)
        self.doubleSpinBox_04_mean.setSingleStep(10.000000000000000)
        self.doubleSpinBox_04_mean.setStepType(QAbstractSpinBox.StepType.DefaultStepType)
        self.doubleSpinBox_04_mean.setValue(50.000000000000000)

        self.gridLayout_2.addWidget(self.doubleSpinBox_04_mean, 1, 1, 1, 1)

        self.label_04_mean = QLabel(self.frame_04_lognormal)
        self.label_04_mean.setObjectName(u"label_04_mean")
        self.label_04_mean.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_04_mean.setMargin(0)

        self.gridLayout_2.addWidget(self.label_04_mean, 1, 0, 1, 1)

        self.doubleSpinBox_04_standard_deviation = QDoubleSpinBox(self.frame_04_lognormal)
        self.doubleSpinBox_04_standard_deviation.setObjectName(u"doubleSpinBox_04_standard_deviation")
        self.doubleSpinBox_04_standard_deviation.setMinimum(1.000000000000000)
        self.doubleSpinBox_04_standard_deviation.setMaximum(10000000.000000000000000)
        self.doubleSpinBox_04_standard_deviation.setSingleStep(50.000000000000000)
        self.doubleSpinBox_04_standard_deviation.setValue(100.000000000000000)

        self.gridLayout_2.addWidget(self.doubleSpinBox_04_standard_deviation, 1, 3, 1, 1)

        self.label_04_standard_deviation = QLabel(self.frame_04_lognormal)
        self.label_04_standard_deviation.setObjectName(u"label_04_standard_deviation")
        self.label_04_standard_deviation.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_04_standard_deviation.setMargin(0)

        self.gridLayout_2.addWidget(self.label_04_standard_deviation, 1, 2, 1, 1)

        self.gridLayout_2.setColumnStretch(0, 1)
        self.gridLayout_2.setColumnStretch(1, 4)
        self.gridLayout_2.setColumnStretch(2, 1)
        self.gridLayout_2.setColumnStretch(3, 4)

        self.horizontalLayout_14.addWidget(self.frame_04_lognormal)

        self.frame_04_power = QFrame(self.box_04_patch_size_generator)
        self.frame_04_power.setObjectName(u"frame_04_power")
        self.frame_04_power.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_04_power.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_04_power.setLineWidth(1)
        self.gridLayout = QGridLayout(self.frame_04_power)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_04_scale_constant = QLabel(self.frame_04_power)
        self.label_04_scale_constant.setObjectName(u"label_04_scale_constant")
        self.label_04_scale_constant.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_04_scale_constant, 1, 0, 1, 1)

        self.doubleSpinBox_04_scale_constant = QDoubleSpinBox(self.frame_04_power)
        self.doubleSpinBox_04_scale_constant.setObjectName(u"doubleSpinBox_04_scale_constant")
        self.doubleSpinBox_04_scale_constant.setDecimals(6)
        self.doubleSpinBox_04_scale_constant.setMinimum(-10000.000000000000000)
        self.doubleSpinBox_04_scale_constant.setMaximum(10000000.000000000000000)
        self.doubleSpinBox_04_scale_constant.setSingleStep(10.000000000000000)
        self.doubleSpinBox_04_scale_constant.setValue(10.000000000000000)

        self.gridLayout.addWidget(self.doubleSpinBox_04_scale_constant, 1, 1, 1, 1)

        self.doubleSpinBox_04_power = QDoubleSpinBox(self.frame_04_power)
        self.doubleSpinBox_04_power.setObjectName(u"doubleSpinBox_04_power")
        self.doubleSpinBox_04_power.setDecimals(6)
        self.doubleSpinBox_04_power.setMinimum(-10000.000000000000000)
        self.doubleSpinBox_04_power.setMaximum(10000.000000000000000)
        self.doubleSpinBox_04_power.setValue(2.000000000000000)

        self.gridLayout.addWidget(self.doubleSpinBox_04_power, 1, 3, 1, 1)

        self.label_04_power = QLabel(self.frame_04_power)
        self.label_04_power.setObjectName(u"label_04_power")
        self.label_04_power.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_04_power, 1, 2, 1, 1)


        self.horizontalLayout_14.addWidget(self.frame_04_power)

        self.frame_04_history_patch = QFrame(self.box_04_patch_size_generator)
        self.frame_04_history_patch.setObjectName(u"frame_04_history_patch")
        self.frame_04_history_patch.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_04_history_patch.setLineWidth(1)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_04_history_patch)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(-1, 0, -1, 0)
        self.lineEdit_04_self_defining_generator = QLineEdit(self.frame_04_history_patch)
        self.lineEdit_04_self_defining_generator.setObjectName(u"lineEdit_04_self_defining_generator")

        self.horizontalLayout_17.addWidget(self.lineEdit_04_self_defining_generator)

        self.btn_04_self_defining_generator = QToolButton(self.frame_04_history_patch)
        self.btn_04_self_defining_generator.setObjectName(u"btn_04_self_defining_generator")

        self.horizontalLayout_17.addWidget(self.btn_04_self_defining_generator)


        self.horizontalLayout_14.addWidget(self.frame_04_history_patch)


        self.verticalLayout.addWidget(self.box_04_patch_size_generator)

        self.box_05_engine_select = QGroupBox(self.frame_20)
        self.box_05_engine_select.setObjectName(u"box_05_engine_select")
        self.box_05_engine_select.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.horizontalLayout_5 = QHBoxLayout(self.box_05_engine_select)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.frame_05_engine = QFrame(self.box_05_engine_select)
        self.frame_05_engine.setObjectName(u"frame_05_engine")
        self.frame_05_engine.setFrameShape(QFrame.Shape.NoFrame)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_05_engine)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.horizontalLayout_23.setContentsMargins(9, 0, 9, 0)
        self.comboBox_05_engine_select = QComboBox(self.frame_05_engine)
        self.comboBox_05_engine_select.addItem("")
        self.comboBox_05_engine_select.addItem("")
        self.comboBox_05_engine_select.addItem("")
        self.comboBox_05_engine_select.addItem("")
        self.comboBox_05_engine_select.setObjectName(u"comboBox_05_engine_select")

        self.horizontalLayout_23.addWidget(self.comboBox_05_engine_select)


        self.horizontalLayout_5.addWidget(self.frame_05_engine)

        self.frame_05_engine_parameters = QFrame(self.box_05_engine_select)
        self.frame_05_engine_parameters.setObjectName(u"frame_05_engine_parameters")
        self.frame_05_engine_parameters.setFrameShape(QFrame.Shape.NoFrame)
        self.horizontalLayout_25 = QHBoxLayout(self.frame_05_engine_parameters)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.horizontalLayout_25.setContentsMargins(9, 0, 9, 0)
        self.label_05_parameter_beta = QLabel(self.frame_05_engine_parameters)
        self.label_05_parameter_beta.setObjectName(u"label_05_parameter_beta")

        self.horizontalLayout_25.addWidget(self.label_05_parameter_beta)

        self.doubleSpinBox_05_parameter_beta = QDoubleSpinBox(self.frame_05_engine_parameters)
        self.doubleSpinBox_05_parameter_beta.setObjectName(u"doubleSpinBox_05_parameter_beta")
        self.doubleSpinBox_05_parameter_beta.setMinimumSize(QSize(120, 0))
        self.doubleSpinBox_05_parameter_beta.setDecimals(6)
        self.doubleSpinBox_05_parameter_beta.setMinimum(0.001000000000000)
        self.doubleSpinBox_05_parameter_beta.setSingleStep(0.100000000000000)
        self.doubleSpinBox_05_parameter_beta.setValue(1.600000000000000)

        self.horizontalLayout_25.addWidget(self.doubleSpinBox_05_parameter_beta)

        self.label_05_parameter_delta = QLabel(self.frame_05_engine_parameters)
        self.label_05_parameter_delta.setObjectName(u"label_05_parameter_delta")

        self.horizontalLayout_25.addWidget(self.label_05_parameter_delta)

        self.doubleSpinBox_05_parameter_delta = QDoubleSpinBox(self.frame_05_engine_parameters)
        self.doubleSpinBox_05_parameter_delta.setObjectName(u"doubleSpinBox_05_parameter_delta")
        self.doubleSpinBox_05_parameter_delta.setMinimumSize(QSize(120, 0))
        self.doubleSpinBox_05_parameter_delta.setDecimals(6)
        self.doubleSpinBox_05_parameter_delta.setMinimum(-1000.000000000000000)
        self.doubleSpinBox_05_parameter_delta.setMaximum(1000.000000000000000)
        self.doubleSpinBox_05_parameter_delta.setSingleStep(0.100000000000000)
        self.doubleSpinBox_05_parameter_delta.setValue(1.000000000000000)

        self.horizontalLayout_25.addWidget(self.doubleSpinBox_05_parameter_delta)

        self.label_05_shape_parameters_path = QLabel(self.frame_05_engine_parameters)
        self.label_05_shape_parameters_path.setObjectName(u"label_05_shape_parameters_path")

        self.horizontalLayout_25.addWidget(self.label_05_shape_parameters_path)

        self.lineEdit_05_shape_parameters_path = QLineEdit(self.frame_05_engine_parameters)
        self.lineEdit_05_shape_parameters_path.setObjectName(u"lineEdit_05_shape_parameters_path")
        self.lineEdit_05_shape_parameters_path.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_25.addWidget(self.lineEdit_05_shape_parameters_path)

        self.btn_05_shape_parameters_path = QToolButton(self.frame_05_engine_parameters)
        self.btn_05_shape_parameters_path.setObjectName(u"btn_05_shape_parameters_path")

        self.horizontalLayout_25.addWidget(self.btn_05_shape_parameters_path)


        self.horizontalLayout_5.addWidget(self.frame_05_engine_parameters)


        self.verticalLayout.addWidget(self.box_05_engine_select)

        self.box_06_run_and_export = QGroupBox(self.frame_20)
        self.box_06_run_and_export.setObjectName(u"box_06_run_and_export")
        self.box_06_run_and_export.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.horizontalLayout_4 = QHBoxLayout(self.box_06_run_and_export)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.frame_3 = QFrame(self.box_06_run_and_export)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalLayout_9 = QVBoxLayout(self.frame_3)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.frame_9 = QFrame(self.frame_3)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.Shape.NoFrame)
        self.horizontalLayout_27 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.btn_06_run = QPushButton(self.frame_9)
        self.btn_06_run.setObjectName(u"btn_06_run")

        self.horizontalLayout_27.addWidget(self.btn_06_run)


        self.verticalLayout_9.addWidget(self.frame_9)

        self.frame_10 = QFrame(self.frame_3)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.Shape.NoFrame)
        self.horizontalLayout_30 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.btn_06_save = QPushButton(self.frame_10)
        self.btn_06_save.setObjectName(u"btn_06_save")

        self.horizontalLayout_30.addWidget(self.btn_06_save)


        self.verticalLayout_9.addWidget(self.frame_10)


        self.horizontalLayout_4.addWidget(self.frame_3)

        self.frame_06_run_and_export = QFrame(self.box_06_run_and_export)
        self.frame_06_run_and_export.setObjectName(u"frame_06_run_and_export")
        self.frame_06_run_and_export.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalLayout_19 = QVBoxLayout(self.frame_06_run_and_export)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.horizontalLayout_06_progressbar = QHBoxLayout()
        self.horizontalLayout_06_progressbar.setObjectName(u"horizontalLayout_06_progressbar")
        self.frame_24 = QFrame(self.frame_06_run_and_export)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setFrameShape(QFrame.Shape.NoFrame)
        self.horizontalLayout_28 = QHBoxLayout(self.frame_24)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(-1, 0, 0, 0)
        self.progressBar = QProgressBar(self.frame_24)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)

        self.horizontalLayout_28.addWidget(self.progressBar)


        self.horizontalLayout_06_progressbar.addWidget(self.frame_24)


        self.verticalLayout_19.addLayout(self.horizontalLayout_06_progressbar)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.frame_06_accuracy = QFrame(self.frame_06_run_and_export)
        self.frame_06_accuracy.setObjectName(u"frame_06_accuracy")
        self.frame_06_accuracy.setFrameShape(QFrame.Shape.NoFrame)
        self.horizontalLayout_29 = QHBoxLayout(self.frame_06_accuracy)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(-1, 0, 0, 0)
        self.frame_06_kappa = QFrame(self.frame_06_accuracy)
        self.frame_06_kappa.setObjectName(u"frame_06_kappa")
        self.frame_06_kappa.setFrameShape(QFrame.Shape.NoFrame)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_06_kappa)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_06_kappa = QLabel(self.frame_06_kappa)
        self.label_06_kappa.setObjectName(u"label_06_kappa")

        self.horizontalLayout_15.addWidget(self.label_06_kappa)

        self.lineEdit_06_kappa = QLineEdit(self.frame_06_kappa)
        self.lineEdit_06_kappa.setObjectName(u"lineEdit_06_kappa")

        self.horizontalLayout_15.addWidget(self.lineEdit_06_kappa)


        self.horizontalLayout_29.addWidget(self.frame_06_kappa)

        self.frame_06_oa = QFrame(self.frame_06_accuracy)
        self.frame_06_oa.setObjectName(u"frame_06_oa")
        self.frame_06_oa.setFrameShape(QFrame.Shape.NoFrame)
        self.horizontalLayout_32 = QHBoxLayout(self.frame_06_oa)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.label_06_oa = QLabel(self.frame_06_oa)
        self.label_06_oa.setObjectName(u"label_06_oa")

        self.horizontalLayout_32.addWidget(self.label_06_oa)

        self.lineEdit_06_oa = QLineEdit(self.frame_06_oa)
        self.lineEdit_06_oa.setObjectName(u"lineEdit_06_oa")

        self.horizontalLayout_32.addWidget(self.lineEdit_06_oa)


        self.horizontalLayout_29.addWidget(self.frame_06_oa)

        self.frame_06_fom = QFrame(self.frame_06_accuracy)
        self.frame_06_fom.setObjectName(u"frame_06_fom")
        self.frame_06_fom.setFrameShape(QFrame.Shape.NoFrame)
        self.horizontalLayout_33 = QHBoxLayout(self.frame_06_fom)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.label_06_fom = QLabel(self.frame_06_fom)
        self.label_06_fom.setObjectName(u"label_06_fom")

        self.horizontalLayout_33.addWidget(self.label_06_fom)

        self.lineEdit_06_fom = QLineEdit(self.frame_06_fom)
        self.lineEdit_06_fom.setObjectName(u"lineEdit_06_fom")

        self.horizontalLayout_33.addWidget(self.lineEdit_06_fom)


        self.horizontalLayout_29.addWidget(self.frame_06_fom)


        self.horizontalLayout_7.addWidget(self.frame_06_accuracy)


        self.verticalLayout_19.addLayout(self.horizontalLayout_7)


        self.horizontalLayout_4.addWidget(self.frame_06_run_and_export)


        self.verticalLayout.addWidget(self.box_06_run_and_export)

        self.splitter.addWidget(self.frame_20)
        self.textBrowser = MyTextBrowser(self.splitter)
        self.textBrowser.setObjectName(u"textBrowser")
        self.splitter.addWidget(self.textBrowser)

        self.horizontalLayout_2.addWidget(self.splitter)

        self.strat_Year_Frame = QFrame(self.centralwidget)
        self.strat_Year_Frame.setObjectName(u"strat_Year_Frame")
        self.strat_Year_Frame.setFrameShape(QFrame.Shape.NoFrame)

        self.horizontalLayout_2.addWidget(self.strat_Year_Frame)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1194, 33))
        self.files = QMenu(self.menubar)
        self.files.setObjectName(u"files")
        self.tools = QMenu(self.menubar)
        self.tools.setObjectName(u"tools")
        self.help = QMenu(self.menubar)
        self.help.setObjectName(u"help")
        self.preferences = QMenu(self.menubar)
        self.preferences.setObjectName(u"preferences")
        self.language = QMenu(self.preferences)
        self.language.setObjectName(u"language")
        self.menumodel = QMenu(self.preferences)
        self.menumodel.setObjectName(u"menumodel")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.lineEdit_01_urban_start, self.btn_01_urban_start)
        QWidget.setTabOrder(self.btn_01_urban_start, self.lineEdit_01_urban_constraint)
        QWidget.setTabOrder(self.lineEdit_01_urban_constraint, self.btn_01_urban_constraint)
        QWidget.setTabOrder(self.btn_01_urban_constraint, self.lineEdit_01_urban_Area)
        QWidget.setTabOrder(self.lineEdit_01_urban_Area, self.btn_01_urban_area)
        QWidget.setTabOrder(self.btn_01_urban_area, self.lineEdit_01_urban_probability)
        QWidget.setTabOrder(self.lineEdit_01_urban_probability, self.btn_01_urban_probability)
        QWidget.setTabOrder(self.btn_01_urban_probability, self.lineEdit_01_urban_end)
        QWidget.setTabOrder(self.lineEdit_01_urban_end, self.btn_01_urban_end)
        QWidget.setTabOrder(self.btn_01_urban_end, self.lineEdit_02_modifing_tif)
        QWidget.setTabOrder(self.lineEdit_02_modifing_tif, self.btn_02_modifing_tif)
        QWidget.setTabOrder(self.btn_02_modifing_tif, self.lineEdit_02_modifing_csv)
        QWidget.setTabOrder(self.lineEdit_02_modifing_csv, self.btn_02_modifing_csv)
        QWidget.setTabOrder(self.btn_02_modifing_csv, self.doubleSpinbox_02_modifing_weight)
        QWidget.setTabOrder(self.doubleSpinbox_02_modifing_weight, self.spinbox_03_start_year)
        QWidget.setTabOrder(self.spinbox_03_start_year, self.doubleSpinbox_03_pool_slice)
        QWidget.setTabOrder(self.doubleSpinbox_03_pool_slice, self.spinbox_03_end_year)
        QWidget.setTabOrder(self.spinbox_03_end_year, self.comboBox_03_neibor_type)
        QWidget.setTabOrder(self.comboBox_03_neibor_type, self.lineEdit_04_self_defining_generator)
        QWidget.setTabOrder(self.lineEdit_04_self_defining_generator, self.btn_04_self_defining_generator)
        QWidget.setTabOrder(self.btn_04_self_defining_generator, self.btn_06_run)
        QWidget.setTabOrder(self.btn_06_run, self.btn_06_save)
        QWidget.setTabOrder(self.btn_06_save, self.textBrowser)

        self.menubar.addAction(self.files.menuAction())
        self.menubar.addAction(self.tools.menuAction())
        self.menubar.addAction(self.preferences.menuAction())
        self.menubar.addAction(self.help.menuAction())
        self.files.addAction(self.action_00_open)
        self.files.addAction(self.action_00_save)
        self.files.addSeparator()
        self.files.addAction(self.action_00_exit)
        self.tools.addAction(self.actionge_00_ParsByGa)
        self.tools.addAction(self.action_00_mlcs)
        self.tools.addAction(self.action_00_pst)
        self.help.addAction(self.action_00_user_guid)
        self.help.addSeparator()
        self.help.addAction(self.action_00_version)
        self.help.addAction(self.action_00_about)
        self.help.addAction(self.action_00_MUSE_Toolbox)
        self.preferences.addAction(self.language.menuAction())
        self.preferences.addAction(self.menumodel.menuAction())
        self.preferences.addSeparator()
        self.preferences.addAction(self.action_00_open_paper)
        self.preferences.addAction(self.action_00_open_testdir)
        self.language.addAction(self.action_00_Chinese_Simplified)
        self.language.addAction(self.action_00_English)
        self.menumodel.addAction(self.action_00_simulation)
        self.menumodel.addAction(self.action_00_verification)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Multi-engine Urban Expansion Simulator\uff08MUSE\uff09", None))
        self.actionnewFile.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa", None))
        self.actionopen.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00", None))
        self.actionge_00_ParsByGa.setText(QCoreApplication.translate("MainWindow", u"Parameter Optimization Tool (POT)", None))
        self.action_00_about.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.action_00_Chinese_Simplified.setText(QCoreApplication.translate("MainWindow", u"Chinese(Simplified)", None))
        self.action_00_English.setText(QCoreApplication.translate("MainWindow", u"English", None))
        self.action_00_simulation.setText(QCoreApplication.translate("MainWindow", u"Calibration and validation", None))
        self.action_00_verification.setText(QCoreApplication.translate("MainWindow", u"Scenario simulation", None))
        self.action_00_exit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.action_00_save.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.action_00_open.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.actionpatchInfo.setText(QCoreApplication.translate("MainWindow", u"patchInfo", None))
        self.actionversionInfo.setText(QCoreApplication.translate("MainWindow", u"versionInfo", None))
        self.action_00_patch_info.setText(QCoreApplication.translate("MainWindow", u"patchInfo", None))
        self.action_00_version.setText(QCoreApplication.translate("MainWindow", u"Version", None))
        self.action_00_user_guid.setText(QCoreApplication.translate("MainWindow", u"User Guide", None))
        self.action_00_MUSE_Toolbox.setText(QCoreApplication.translate("MainWindow", u"MUSE ArcGIS Pro Toolbox", None))
        self.action_00_mlcs.setText(QCoreApplication.translate("MainWindow", u"Urban Development Suitability Assessment (UDSA)", None))
        self.action_00_pst.setText(QCoreApplication.translate("MainWindow", u"Patch Size Statistical Analysis (PSSA)", None))
        self.action_00_open_paper.setText(QCoreApplication.translate("MainWindow", u"Open Paper", None))
        self.action_00_open_testdir.setText(QCoreApplication.translate("MainWindow", u"Open TestDir", None))
        self.box_01_data_Input.setTitle(QCoreApplication.translate("MainWindow", u"Input files", None))
        self.label_01_urban_start.setText(QCoreApplication.translate("MainWindow", u"Urban land use map of starting time", None))
        self.lineEdit_01_urban_start.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Initial urban land raster (tif/tiff, values 0 and 1).", None))
        self.btn_01_urban_start.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_01_urban_contraint.setText(QCoreApplication.translate("MainWindow", u"Spatial Constraints", None))
        self.lineEdit_01_urban_constraint.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Constraint factor raster (tif/tiff, values 0 and 1).", None))
        self.btn_01_urban_constraint.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_01_urban_area.setText(QCoreApplication.translate("MainWindow", u"Stepwise demand of urban development", None))
        self.lineEdit_01_urban_Area.setPlaceholderText(QCoreApplication.translate("MainWindow", u"New urban land area demand (csv, 2 columns).", None))
        self.btn_01_urban_area.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_01_urban_probability.setText(QCoreApplication.translate("MainWindow", u"Urban development suitability", None))
        self.lineEdit_01_urban_probability.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Urban suitability probability raster (tif/tiff, values 0-1).", None))
        self.btn_01_urban_probability.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_01_urban_end.setText(QCoreApplication.translate("MainWindow", u"Urban land use map of ending time", None))
        self.lineEdit_01_urban_end.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Final urban land raster (tif/tiff, values 0 and 1).", None))
        self.btn_01_urban_end.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.box_02_modifing.setTitle(QCoreApplication.translate("MainWindow", u"Gaussian-based regulation", None))
        self.label_02_modifing_tif.setText(QCoreApplication.translate("MainWindow", u"City centers", None))
        self.lineEdit_02_modifing_tif.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Urban center point raster (tif/tiff, values 0 and 1).", None))
        self.btn_02_modifing_tif.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_02_modifing_csv.setText(QCoreApplication.translate("MainWindow", u"Gaussian parameters", None))
        self.lineEdit_02_modifing_csv.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Gaussian correction parameters (csv, 4 columns).", None))
        self.btn_02_modifing_csv.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_02_modifing_weight.setText(QCoreApplication.translate("MainWindow", u"Weight for Gaussian function", None))
        self.box_03_model_parameters.setTitle(QCoreApplication.translate("MainWindow", u"Global parameters", None))
        self.label_03_strat_year.setText(QCoreApplication.translate("MainWindow", u"Starting time", None))
        self.label_03_end_Year.setText(QCoreApplication.translate("MainWindow", u"Ending time", None))
        self.label_03_location_uncertainty.setText(QCoreApplication.translate("MainWindow", u"Location uncertainty", None))
        self.label_03_neibor_type.setText(QCoreApplication.translate("MainWindow", u"Type of Neighborhood", None))
        self.comboBox_03_neibor_type.setItemText(0, QCoreApplication.translate("MainWindow", u"4", None))
        self.comboBox_03_neibor_type.setItemText(1, QCoreApplication.translate("MainWindow", u"8", None))

        self.label_03_pool_Slice.setText(QCoreApplication.translate("MainWindow", u"Pruning parameter", None))
        self.checkBox_03_organic_by_step.setText(QCoreApplication.translate("MainWindow", u"Enable Stepwise Organic Growth", None))
        self.lineEdit_03_organic_by_step.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Organic growth step data (csv, 2 columns).", None))
        self.toolButton_03_organic_by_step.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.box_04_patch_size_generator.setTitle(QCoreApplication.translate("MainWindow", u"Patch size generator", None))
        self.comboBox_04_generator_select.setItemText(0, QCoreApplication.translate("MainWindow", u"Lognormal Distribution", None))
        self.comboBox_04_generator_select.setItemText(1, QCoreApplication.translate("MainWindow", u"Power Distribution", None))
        self.comboBox_04_generator_select.setItemText(2, QCoreApplication.translate("MainWindow", u"History patch size", None))

        self.label_04_mean.setText(QCoreApplication.translate("MainWindow", u"Mean", None))
        self.label_04_standard_deviation.setText(QCoreApplication.translate("MainWindow", u"Standard deviation", None))
        self.label_04_scale_constant.setText(QCoreApplication.translate("MainWindow", u"Scale Constant", None))
        self.label_04_power.setText(QCoreApplication.translate("MainWindow", u"Power", None))
        self.lineEdit_04_self_defining_generator.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Patch size data (csv, 2 columns).", None))
        self.btn_04_self_defining_generator.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.box_05_engine_select.setTitle(QCoreApplication.translate("MainWindow", u"Patch generation operator", None))
        self.comboBox_05_engine_select.setItemText(0, QCoreApplication.translate("MainWindow", u"Simple Patch Generation Engine (SPGE)", None))
        self.comboBox_05_engine_select.setItemText(1, QCoreApplication.translate("MainWindow", u"Neighbor Patch Generation Engine (NeiPGE)", None))
        self.comboBox_05_engine_select.setItemText(2, QCoreApplication.translate("MainWindow", u"Distance Patch Generation Engine (DisPGE)", None))
        self.comboBox_05_engine_select.setItemText(3, QCoreApplication.translate("MainWindow", u"Parameterized Patch Generation Engine (PPGE)", None))

        self.label_05_parameter_beta.setText(QCoreApplication.translate("MainWindow", u"Beta ", None))
        self.label_05_parameter_delta.setText(QCoreApplication.translate("MainWindow", u"Delta", None))
        self.label_05_shape_parameters_path.setText(QCoreApplication.translate("MainWindow", u"Shape Parameter Path", None))
        self.lineEdit_05_shape_parameters_path.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Optional input, (csv, 2 columns)", None))
        self.btn_05_shape_parameters_path.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.box_06_run_and_export.setTitle(QCoreApplication.translate("MainWindow", u"Results and performance", None))
        self.btn_06_run.setText(QCoreApplication.translate("MainWindow", u"Run", None))
        self.btn_06_save.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.label_06_kappa.setText(QCoreApplication.translate("MainWindow", u"Kappa\uff1a", None))
        self.label_06_oa.setText(QCoreApplication.translate("MainWindow", u"OA\uff1a", None))
        self.label_06_fom.setText(QCoreApplication.translate("MainWindow", u"Fom\uff1a", None))
        self.textBrowser.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Run Information Output...", None))
        self.files.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.tools.setTitle(QCoreApplication.translate("MainWindow", u"Tool", None))
        self.help.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
        self.preferences.setTitle(QCoreApplication.translate("MainWindow", u"Preference", None))
        self.language.setTitle(QCoreApplication.translate("MainWindow", u"Language", None))
        self.menumodel.setTitle(QCoreApplication.translate("MainWindow", u"Mode", None))
    # retranslateUi

