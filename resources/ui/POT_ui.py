# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'POT.ui'
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
    QGridLayout, QHBoxLayout, QLabel, QLayout,
    QPushButton, QSizePolicy, QSpinBox, QSplitter,
    QVBoxLayout, QWidget)

from src.mytextbrowser import MyTextBrowser

class Ui_POT(object):
    def setupUi(self, POT):
        if not POT.objectName():
            POT.setObjectName(u"POT")
        POT.resize(561, 242)
        POT.setMinimumSize(QSize(0, 0))
        POT.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_5 = QVBoxLayout(POT)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.splitter = QSplitter(POT)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Orientation.Vertical)
        self.frame_3 = QFrame(self.splitter)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 0))
        self.frame_3.setMaximumSize(QSize(16777215, 152))
        self.frame_3.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_3)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(self.frame_3)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.comboBox_00_algorithms = QComboBox(self.frame)
        self.comboBox_00_algorithms.setObjectName(u"comboBox_00_algorithms")

        self.verticalLayout_3.addWidget(self.comboBox_00_algorithms)


        self.verticalLayout_2.addWidget(self.frame)

        self.frame_2 = QFrame(self.frame_3)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.frame_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.spinBox_01_pop_size = QSpinBox(self.frame_2)
        self.spinBox_01_pop_size.setObjectName(u"spinBox_01_pop_size")
        self.spinBox_01_pop_size.setMaximum(100000)
        self.spinBox_01_pop_size.setSingleStep(5)
        self.spinBox_01_pop_size.setValue(10)

        self.gridLayout.addWidget(self.spinBox_01_pop_size, 0, 1, 1, 1)

        self.spinBox_01_thread_count = QSpinBox(self.frame_2)
        self.spinBox_01_thread_count.setObjectName(u"spinBox_01_thread_count")
        self.spinBox_01_thread_count.setMinimum(1)

        self.gridLayout.addWidget(self.spinBox_01_thread_count, 2, 1, 1, 1)

        self.spinBox__01_n_gen = QSpinBox(self.frame_2)
        self.spinBox__01_n_gen.setObjectName(u"spinBox__01_n_gen")
        self.spinBox__01_n_gen.setMaximum(10000)
        self.spinBox__01_n_gen.setValue(3)

        self.gridLayout.addWidget(self.spinBox__01_n_gen, 1, 1, 1, 1)

        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.frame_2)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.checkBox_02_pruning_par = QCheckBox(self.frame_4)
        self.checkBox_02_pruning_par.setObjectName(u"checkBox_02_pruning_par")
        self.checkBox_02_pruning_par.setChecked(True)
        self.checkBox_02_pruning_par.setTristate(False)

        self.verticalLayout_4.addWidget(self.checkBox_02_pruning_par)

        self.checkBox__02_organic = QCheckBox(self.frame_4)
        self.checkBox__02_organic.setObjectName(u"checkBox__02_organic")
        self.checkBox__02_organic.setChecked(True)
        self.checkBox__02_organic.setTristate(False)

        self.verticalLayout_4.addWidget(self.checkBox__02_organic)

        self.checkBox_02_weight_of_gauss = QCheckBox(self.frame_4)
        self.checkBox_02_weight_of_gauss.setObjectName(u"checkBox_02_weight_of_gauss")

        self.verticalLayout_4.addWidget(self.checkBox_02_weight_of_gauss)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.checkBox_02_beta = QCheckBox(self.frame_4)
        self.checkBox_02_beta.setObjectName(u"checkBox_02_beta")

        self.horizontalLayout_2.addWidget(self.checkBox_02_beta)

        self.checkBox_02_delta = QCheckBox(self.frame_4)
        self.checkBox_02_delta.setObjectName(u"checkBox_02_delta")

        self.horizontalLayout_2.addWidget(self.checkBox_02_delta)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)


        self.verticalLayout.addWidget(self.frame_4)

        self.btn_04_run = QPushButton(self.frame_3)
        self.btn_04_run.setObjectName(u"btn_04_run")

        self.verticalLayout.addWidget(self.btn_04_run)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.splitter.addWidget(self.frame_3)
        self.textBrowser = MyTextBrowser(self.splitter)
        self.textBrowser.setObjectName(u"textBrowser")
        self.splitter.addWidget(self.textBrowser)

        self.verticalLayout_5.addWidget(self.splitter)


        self.retranslateUi(POT)

        QMetaObject.connectSlotsByName(POT)
    # setupUi

    def retranslateUi(self, POT):
        POT.setWindowTitle(QCoreApplication.translate("POT", u"Parameter Optimization Tool (POT) module", None))
        self.label.setText(QCoreApplication.translate("POT", u"Population size", None))
        self.label_3.setText(QCoreApplication.translate("POT", u"Thread Count", None))
        self.label_2.setText(QCoreApplication.translate("POT", u"Number of generations", None))
        self.checkBox_02_pruning_par.setText(QCoreApplication.translate("POT", u"Pruning parameter", None))
        self.checkBox__02_organic.setText(QCoreApplication.translate("POT", u"Proportion of organic patch", None))
        self.checkBox_02_weight_of_gauss.setText(QCoreApplication.translate("POT", u"Weight for Gaussian function", None))
        self.checkBox_02_beta.setText(QCoreApplication.translate("POT", u"Beta", None))
        self.checkBox_02_delta.setText(QCoreApplication.translate("POT", u"Delta", None))
        self.btn_04_run.setText(QCoreApplication.translate("POT", u"Run", None))
    # retranslateUi

