# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'aboutus.ui'
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
from PySide6.QtWidgets import (QApplication, QSizePolicy, QTextBrowser, QVBoxLayout,
    QWidget)
import res_rc

class Ui_AboutUs(object):
    def setupUi(self, AboutUs):
        if not AboutUs.objectName():
            AboutUs.setObjectName(u"AboutUs")
        AboutUs.resize(873, 813)
        self.verticalLayout = QVBoxLayout(AboutUs)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.textBrowser = QTextBrowser(AboutUs)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setOpenExternalLinks(True)
        self.textBrowser.setOpenLinks(True)

        self.verticalLayout.addWidget(self.textBrowser)


        self.retranslateUi(AboutUs)

        QMetaObject.connectSlotsByName(AboutUs)
    # setupUi

    def retranslateUi(self, AboutUs):
        AboutUs.setWindowTitle(QCoreApplication.translate("AboutUs", u"About us", None))
        self.textBrowser.setHtml(QCoreApplication.translate("AboutUs", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /><img src=\":/resources/MUSE_LOGO2.svg\" /></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br />MUSE is an open-access land change simulation software designed for urban expansion, utilizing cellular automata modeling. It employs multiple patch generation engines to "
                        "simulate urban development processes at different scales, from cell to patch level, mirroring real-world mechanisms. The software incorporates a variety of parameters and operators to manage multilevel urban morphologies.</p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">At the landscape level, MUSE regulates urban development occurrence using Gaussian functions, shaping macro-level spatiotemporal morphology based on the regularity of physical urban expansion. It considers the Euclidean distance from newly developed urban patches to the nearest city centers, influencing the aggregated or sprawled nature of urban landscapes.</p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">At the class level, MUSE manipulates inter-patch spatial connectivity by categorizing new urban patches into organic and spontaneous types. This "
                        "approach controls the spatiotemporal morphology (contiguous and fragmented) of the urban land class at a meso-level, introducing regularity in the oscillation between diffusion and coalescence phases in urban expansion processes.</p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">At the patch level, MUSE controls the size of newly generated urban patches through statistical distribution, allowing for variation in patch density and landscape fragmentation. Four distinct operators regulate the shapes of new urban patches, providing control over the diversity of urban patches at the micro patch level.</p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Constructed in standard C++ (ISO/IEC 14882:2020), MUSE operates as a Windows-based platform and is available as an ArcGIS Pro plugin. The software comprises seven fundament"
                        "al components: input files, Gaussian-based regulation, patch type operator, global parameter, patch size generator, patch generation operator, and results and performance.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">MUSE Download Links:</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\">\n"
"<li style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">GitHub Repository: <a href=\"https://github.com/LandInsightLab/MUSE\"><span style=\" text-decoration: underline; color:#0000ff;\">https://github.com/LandInsightLab/MUSE</span></a></li>\n"
"<li style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Official Website: <a href=\"https://www.landinsight.com/Download/MUSE\"><span style=\" text-decoration: un"
                        "derline; color:#0000ff;\">https://www.landinsight.com/Download/MUSE</span></a></li></ul>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">MUSE Toolbox Download Links:</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\">\n"
"<li style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">GitHub Repository: <a href=\"https://github.com/LandInsightLab/MUSE_Toolbox\"><span style=\" text-decoration: underline; color:#0000ff;\">https://github.com/LandInsightLab/MUSE_Toolbox</span></a></li>\n"
"<li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Official Website: <a href=\"https://www.landinsight.com/Download/MUSE_Toolbox\"><span style=\" text-decoration: underline; color:#0000ff;\">https://www.landinsight.com/"
                        "Download/MUSE_Toolbox</span></a></li></ul>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; text-decoration: underline; color:#0000ff;\"><br /></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">Developers:</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">          Yang Jianxin</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 2;\">\n"
"<li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Personal Page: <a href=\"https://ggxy.cug.edu.cn/info/1051/2380.htm\"><span style=\" font-weight:700; text-decoration: underline; color:#00aa7f;\">\u6768\u5efa"
                        "\u65b0-\u516c\u5171\u7ba1\u7406\u5b66\u9662 (cug.edu.cn)</span></a></li></ul>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 2;\">\n"
"<li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Email: yangjianxin@cug.edu.cn</li></ul>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px;\"><span style=\" font-weight:700;\">Shi Rui</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 2;\">\n"
"<li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Personal Page: <a href=\"https://github.com/Mr-ShiRui\"><span style=\" font-weight:700; te"
                        "xt-decoration: underline; color:#00aa7f;\">Mr-ShiRui (Rui Shi) \u00b7 GitHub</span></a></li></ul>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 2;\">\n"
"<li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Email: shirui@cug.edu.cn</li></ul>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">          Dr. Wenwu Tang</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 2;\">\n"
"<li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Personal Page: <a href=\"https://pages.charlotte.edu/wenwu"
                        "-tang/\"><span style=\" font-weight:700; text-decoration: underline; color:#00aa7f;\">Dr. Wenwu Tang | Home (charlotte.edu)</span></a></li></ul>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 2;\">\n"
"<li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Email: WenwuTang@uncc.edu</li></ul>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">Research Papers:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px;\"><a href=\"https://www.sciencedirect.com/science/article/abs/pii/S0264275122005959\"><span style=\" text-decoration: underline; color:#0000ff;\">Jianxin Yang, Yang, S., Li, J., Gong, J., Yuan, M., Li, J., Dai, Y., Ye, J. (2023) &quot;A distance-driven urban simulation model (DISUSIM): Accoun"
                        "ting for urban morphology at multiple landscape levels&quot; Published in Cities, 134:104156</span></a></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px;\"><a href=\"https://www.sciencedirect.com/science/article/abs/pii/S0169204622002894\"><span style=\" text-decoration: underline; color:#0000ff;\">Jianxin Yang, Tang, W., Gong, J., Shi, R., Zheng, M., Dai, Y. (2023) &quot;Simulating urban expansion using cellular automata model with spatiotemporally explicit representation of urban demand&quot; Published in Landscape and Urban Planning, 231:104640</span></a></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px; text-decoration: underline; color:#0000ff;\"><br /></p>\n"
"<p style=\""
                        " margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px;\"><a href=\"https://doi.org/10.1080/136588197242329\"><span style=\" text-decoration: underline; color:#0000ff;\">BROOKES, Christopher J .A parameterized region-growing programme for site allocation on raster suitability maps[J].International Journal of Geographical Information Systems, 1997, 11(4):375-396.DOI:10.1080/136588197242329</span></a></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">Address:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px;\"><span style=\" font-family:'CharisSIL-Italic'; font-size:10pt; font-style:italic; color:#000000;\">Department of Land Resource Management, School of Public Administration, China University of Geosciences, Wuhan 430074, China</span></p>\n"
"<p style=\"-qt-parag"
                        "raph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px; font-family:'CharisSIL-Italic'; font-size:10pt; font-style:italic; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px;\"><span style=\" font-family:'CharisSIL-Italic'; font-size:10pt; font-style:italic; color:#000000;\">Key Labs of Law Evaluation of Ministry of Land and Resources of China, 388 Lumo Road, Hongshan District, Wuhan 430074, China</span></p></body></html>", None))
    # retranslateUi

