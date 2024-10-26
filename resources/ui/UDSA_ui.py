# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UDSA.ui'
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
    QGroupBox, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpinBox,
    QSplitter, QTableWidget, QTableWidgetItem, QToolButton,
    QVBoxLayout, QWidget)

from src.mytextbrowser import MyTextBrowser
import resources.qrc.res_rc

class Ui_UDSA(object):
    def setupUi(self, UDSA):
        if not UDSA.objectName():
            UDSA.setObjectName(u"UDSA")
        UDSA.resize(751, 697)
        UDSA.setStyleSheet(u"")
        self.horizontalLayout_8 = QHBoxLayout(UDSA)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.splitter = QSplitter(UDSA)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Orientation.Horizontal)
        self.splitter.setHandleWidth(5)
        self.frame_2 = QFrame(self.splitter)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"QFrame#frame_4, QFrame#frame_7, QFrame#frame, QFrame#frame_3 {\n"
"    border: none;\n"
"}")
        self.frame_2.setFrameShape(QFrame.Shape.Box)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, -1, -1, 3)
        self.frame_18 = QFrame(self.frame_2)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setAcceptDrops(False)
        self.frame_18.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_18)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.groupBox = QGroupBox(self.frame_18)
        self.groupBox.setObjectName(u"groupBox")
        self.horizontalLayout_14 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(-1, -1, -1, 3)
        self.table_01 = QTableWidget(self.groupBox)
        self.table_01.setObjectName(u"table_01")

        self.horizontalLayout_14.addWidget(self.table_01)

        self.frame_5 = QFrame(self.groupBox)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(60, 0))
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_5)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.button_01_add = QToolButton(self.frame_5)
        self.button_01_add.setObjectName(u"button_01_add")
        self.button_01_add.setMinimumSize(QSize(50, 0))
        self.button_01_add.setMaximumSize(QSize(16777215, 16777215))
        icon = QIcon()
        icon.addFile(u":/svg/add.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.button_01_add.setIcon(icon)
        self.button_01_add.setIconSize(QSize(16, 16))

        self.verticalLayout_8.addWidget(self.button_01_add)

        self.button_01_del = QPushButton(self.frame_5)
        self.button_01_del.setObjectName(u"button_01_del")
        icon1 = QIcon()
        icon1.addFile(u":/svg/del.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.button_01_del.setIcon(icon1)
        self.button_01_del.setIconSize(QSize(13, 13))

        self.verticalLayout_8.addWidget(self.button_01_del)


        self.horizontalLayout_14.addWidget(self.frame_5)


        self.verticalLayout_5.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.frame_18)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.horizontalLayout_16 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(-1, 6, -1, 9)
        self.lineEdit_02_input = QLineEdit(self.groupBox_2)
        self.lineEdit_02_input.setObjectName(u"lineEdit_02_input")

        self.horizontalLayout_16.addWidget(self.lineEdit_02_input)

        self.button_02_input = QToolButton(self.groupBox_2)
        self.button_02_input.setObjectName(u"button_02_input")
        self.button_02_input.setMinimumSize(QSize(60, 0))

        self.horizontalLayout_16.addWidget(self.button_02_input)


        self.verticalLayout_5.addWidget(self.groupBox_2)


        self.verticalLayout_3.addWidget(self.frame_18)

        self.frame_17 = QFrame(self.frame_2)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(-1, -1, -1, 3)
        self.groupBox_3 = QGroupBox(self.frame_17)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_9 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.frame_15 = QFrame(self.groupBox_3)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_15)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(-1, -1, -1, 3)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.frame_4 = QFrame(self.frame_15)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_4)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(-1, 3, -1, 3)
        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")

        self.verticalLayout_11.addWidget(self.label)

        self.label_2 = QLabel(self.frame_4)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_11.addWidget(self.label_2)

        self.label_7 = QLabel(self.frame_4)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_11.addWidget(self.label_7)


        self.horizontalLayout_4.addWidget(self.frame_4)

        self.frame_7 = QFrame(self.frame_15)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(0, 0))
        self.frame_7.setMaximumSize(QSize(16777215, 16777215))
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_7)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.comboBox_03 = QComboBox(self.frame_7)
        self.comboBox_03.addItem("")
        self.comboBox_03.addItem("")
        self.comboBox_03.addItem("")
        self.comboBox_03.addItem("")
        self.comboBox_03.addItem("")
        self.comboBox_03.addItem("")
        self.comboBox_03.setObjectName(u"comboBox_03")
        self.comboBox_03.setMinimumSize(QSize(138, 25))

        self.verticalLayout_10.addWidget(self.comboBox_03)

        self.lineEdit_03_random_samples = QLineEdit(self.frame_7)
        self.lineEdit_03_random_samples.setObjectName(u"lineEdit_03_random_samples")

        self.verticalLayout_10.addWidget(self.lineEdit_03_random_samples)

        self.lineEdit_03_sample_ratio = QLineEdit(self.frame_7)
        self.lineEdit_03_sample_ratio.setObjectName(u"lineEdit_03_sample_ratio")

        self.verticalLayout_10.addWidget(self.lineEdit_03_sample_ratio)


        self.horizontalLayout_4.addWidget(self.frame_7)


        self.verticalLayout_12.addLayout(self.horizontalLayout_4)

        self.frame_6 = QFrame(self.frame_15)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 3, -1, 3)
        self.checkBox_03_cv = QCheckBox(self.frame_6)
        self.checkBox_03_cv.setObjectName(u"checkBox_03_cv")

        self.horizontalLayout_2.addWidget(self.checkBox_03_cv)

        self.spinBox_03_cv = QSpinBox(self.frame_6)
        self.spinBox_03_cv.setObjectName(u"spinBox_03_cv")
        self.spinBox_03_cv.setMaximum(99)
        self.spinBox_03_cv.setValue(5)

        self.horizontalLayout_2.addWidget(self.spinBox_03_cv)


        self.verticalLayout_12.addWidget(self.frame_6)

        self.frame_8 = QFrame(self.frame_15)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(-1, 3, -1, 3)
        self.checkBox_03_thread = QCheckBox(self.frame_8)
        self.checkBox_03_thread.setObjectName(u"checkBox_03_thread")

        self.horizontalLayout_6.addWidget(self.checkBox_03_thread)

        self.spinBox_03_thread = QSpinBox(self.frame_8)
        self.spinBox_03_thread.setObjectName(u"spinBox_03_thread")

        self.horizontalLayout_6.addWidget(self.spinBox_03_thread)


        self.verticalLayout_12.addWidget(self.frame_8)

        self.frame_03_save = QFrame(self.frame_15)
        self.frame_03_save.setObjectName(u"frame_03_save")
        self.frame_03_save.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_03_save.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_03_save)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 3, 9, 3)
        self.checkBox_03_save = QCheckBox(self.frame_03_save)
        self.checkBox_03_save.setObjectName(u"checkBox_03_save")

        self.verticalLayout_2.addWidget(self.checkBox_03_save)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.lineEdit_03_save = QLineEdit(self.frame_03_save)
        self.lineEdit_03_save.setObjectName(u"lineEdit_03_save")

        self.horizontalLayout_5.addWidget(self.lineEdit_03_save)

        self.toolButton_03_save = QToolButton(self.frame_03_save)
        self.toolButton_03_save.setObjectName(u"toolButton_03_save")

        self.horizontalLayout_5.addWidget(self.toolButton_03_save)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)


        self.verticalLayout_12.addWidget(self.frame_03_save)


        self.verticalLayout_9.addWidget(self.frame_15)


        self.horizontalLayout_12.addWidget(self.groupBox_3)

        self.groupBox_4 = QGroupBox(self.frame_17)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, 3, -1, 9)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.frame = QFrame(self.groupBox_4)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_041 = QLabel(self.frame)
        self.label_041.setObjectName(u"label_041")

        self.verticalLayout.addWidget(self.label_041)

        self.label_042 = QLabel(self.frame)
        self.label_042.setObjectName(u"label_042")

        self.verticalLayout.addWidget(self.label_042)

        self.label_043 = QLabel(self.frame)
        self.label_043.setObjectName(u"label_043")

        self.verticalLayout.addWidget(self.label_043)

        self.label_044 = QLabel(self.frame)
        self.label_044.setObjectName(u"label_044")

        self.verticalLayout.addWidget(self.label_044)

        self.label_045 = QLabel(self.frame)
        self.label_045.setObjectName(u"label_045")

        self.verticalLayout.addWidget(self.label_045)


        self.horizontalLayout_3.addWidget(self.frame)

        self.frame_3 = QFrame(self.groupBox_4)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_3)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.lineEdit_041 = QLineEdit(self.frame_3)
        self.lineEdit_041.setObjectName(u"lineEdit_041")

        self.verticalLayout_7.addWidget(self.lineEdit_041)

        self.lineEdit_042 = QLineEdit(self.frame_3)
        self.lineEdit_042.setObjectName(u"lineEdit_042")

        self.verticalLayout_7.addWidget(self.lineEdit_042)

        self.lineEdit_043 = QLineEdit(self.frame_3)
        self.lineEdit_043.setObjectName(u"lineEdit_043")

        self.verticalLayout_7.addWidget(self.lineEdit_043)

        self.lineEdit_044 = QLineEdit(self.frame_3)
        self.lineEdit_044.setObjectName(u"lineEdit_044")

        self.verticalLayout_7.addWidget(self.lineEdit_044)

        self.lineEdit_045 = QLineEdit(self.frame_3)
        self.lineEdit_045.setObjectName(u"lineEdit_045")

        self.verticalLayout_7.addWidget(self.lineEdit_045)


        self.horizontalLayout_3.addWidget(self.frame_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.button_04_fetch = QPushButton(self.groupBox_4)
        self.button_04_fetch.setObjectName(u"button_04_fetch")
        self.button_04_fetch.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_7.addWidget(self.button_04_fetch)

        self.button_04_train = QPushButton(self.groupBox_4)
        self.button_04_train.setObjectName(u"button_04_train")

        self.horizontalLayout_7.addWidget(self.button_04_train)


        self.verticalLayout_4.addLayout(self.horizontalLayout_7)

        self.verticalLayout_4.setStretch(0, 10)
        self.verticalLayout_4.setStretch(1, 3)

        self.horizontalLayout_12.addWidget(self.groupBox_4)

        self.horizontalLayout_12.setStretch(0, 25)
        self.horizontalLayout_12.setStretch(1, 17)

        self.verticalLayout_3.addWidget(self.frame_17)

        self.frame_19 = QFrame(self.frame_2)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_19)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.groupBox_5 = QGroupBox(self.frame_19)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.horizontalLayout = QHBoxLayout(self.groupBox_5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 3, -1, 3)
        self.frame_16 = QFrame(self.groupBox_5)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(-1, 6, -1, 9)
        self.lineEdit_05_save_path = QLineEdit(self.frame_16)
        self.lineEdit_05_save_path.setObjectName(u"lineEdit_05_save_path")

        self.horizontalLayout_10.addWidget(self.lineEdit_05_save_path)

        self.button_05_save = QToolButton(self.frame_16)
        self.button_05_save.setObjectName(u"button_05_save")

        self.horizontalLayout_10.addWidget(self.button_05_save)


        self.horizontalLayout.addWidget(self.frame_16)

        self.button_05_predict = QPushButton(self.groupBox_5)
        self.button_05_predict.setObjectName(u"button_05_predict")
        self.button_05_predict.setMinimumSize(QSize(0, 0))

        self.horizontalLayout.addWidget(self.button_05_predict)


        self.verticalLayout_6.addWidget(self.groupBox_5)


        self.verticalLayout_3.addWidget(self.frame_19)

        self.splitter.addWidget(self.frame_2)
        self.textBrowser_06_output = MyTextBrowser(self.splitter)
        self.textBrowser_06_output.setObjectName(u"textBrowser_06_output")
        self.textBrowser_06_output.setMinimumSize(QSize(138, 0))
        self.textBrowser_06_output.setMaximumSize(QSize(16777215, 16777215))
        self.splitter.addWidget(self.textBrowser_06_output)

        self.horizontalLayout_8.addWidget(self.splitter)


        self.retranslateUi(UDSA)

        QMetaObject.connectSlotsByName(UDSA)
    # setupUi

    def retranslateUi(self, UDSA):
        UDSA.setWindowTitle(QCoreApplication.translate("UDSA", u"Urban Development Suitability Assessment (UDSA) module", None))
        self.groupBox.setTitle(QCoreApplication.translate("UDSA", u"Driver Factors Input", None))
        self.button_01_add.setText("")
        self.button_01_del.setText("")
        self.groupBox_2.setTitle(QCoreApplication.translate("UDSA", u"Label Data Input", None))
        self.lineEdit_02_input.setText("")
        self.button_02_input.setText(QCoreApplication.translate("UDSA", u"...", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("UDSA", u"Training Parameters", None))
        self.label.setText(QCoreApplication.translate("UDSA", u"Model Selection", None))
        self.label_2.setText(QCoreApplication.translate("UDSA", u"Random Samples", None))
        self.label_7.setText(QCoreApplication.translate("UDSA", u"Test Data Ratio", None))
        self.comboBox_03.setItemText(0, QCoreApplication.translate("UDSA", u"XGBoost", None))
        self.comboBox_03.setItemText(1, QCoreApplication.translate("UDSA", u"Random Forest", None))
        self.comboBox_03.setItemText(2, QCoreApplication.translate("UDSA", u"SVM", None))
        self.comboBox_03.setItemText(3, QCoreApplication.translate("UDSA", u"MLP", None))
        self.comboBox_03.setItemText(4, QCoreApplication.translate("UDSA", u"Naive Bayes", None))
        self.comboBox_03.setItemText(5, QCoreApplication.translate("UDSA", u"Logistic Regression", None))

        self.comboBox_03.setCurrentText(QCoreApplication.translate("UDSA", u"XGBoost", None))
        self.lineEdit_03_random_samples.setPlaceholderText(QCoreApplication.translate("UDSA", u"Number of random samples", None))
        self.lineEdit_03_sample_ratio.setText("")
        self.checkBox_03_cv.setText(QCoreApplication.translate("UDSA", u"Cross Validation", None))
        self.checkBox_03_thread.setText(QCoreApplication.translate("UDSA", u"Multithreading", None))
        self.checkBox_03_save.setText(QCoreApplication.translate("UDSA", u"Save Training Data", None))
        self.lineEdit_03_save.setPlaceholderText(QCoreApplication.translate("UDSA", u"Enter save path for training data (csv or txt)", None))
        self.toolButton_03_save.setText(QCoreApplication.translate("UDSA", u"...", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("UDSA", u"Model Parameters", None))
        self.label_041.setText(QCoreApplication.translate("UDSA", u"TextLabel", None))
        self.label_042.setText(QCoreApplication.translate("UDSA", u"TextLabel", None))
        self.label_043.setText(QCoreApplication.translate("UDSA", u"TextLabel", None))
        self.label_044.setText(QCoreApplication.translate("UDSA", u"TextLabel", None))
        self.label_045.setText(QCoreApplication.translate("UDSA", u"TextLabel", None))
        self.button_04_fetch.setText(QCoreApplication.translate("UDSA", u"Fetch and Train", None))
        self.button_04_train.setText(QCoreApplication.translate("UDSA", u"Train", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("UDSA", u"Prediction", None))
        self.lineEdit_05_save_path.setText("")
        self.lineEdit_05_save_path.setPlaceholderText(QCoreApplication.translate("UDSA", u"Enter save path for prediction results (tif or tiff)", None))
        self.button_05_save.setText(QCoreApplication.translate("UDSA", u"...", None))
        self.button_05_predict.setText(QCoreApplication.translate("UDSA", u"Start Prediction", None))
        self.textBrowser_06_output.setHtml(QCoreApplication.translate("UDSA", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.textBrowser_06_output.setPlaceholderText(QCoreApplication.translate("UDSA", u"Run Information Output...", None))
    # retranslateUi

