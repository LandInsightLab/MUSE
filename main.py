# MIT License
#
# Copyright (c) 2023 LandInsightLab 
# Author: Rui Shi
# Date: October 2024
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
import configparser
from PySide6.QtWidgets import QApplication, QSplashScreen
from PySide6.QtGui import QPixmap
from PySide6.QtCore import QCoreApplication, QDir, QTranslator, QLocale
from src.mainwindow import MainWindow  # Import MainWindow from src

if __name__ == "__main__":
    app = QApplication([])

    # Set the current directory to the application's install directory
    install_dir = QCoreApplication.applicationDirPath()
    QDir.setCurrent(install_dir)

    # Create and install the translator
    translator = QTranslator()
    translation_file = QDir(install_dir).filePath("translations/MUSE.zh_CN.qm")

    config = configparser.ConfigParser()
    try:
        # Try to read the config.ini file
        config.read('config.ini')
        if 'Settings' in config and 'Language' in config['Settings']:
            if config['Settings']['Language'] == '1':
                # Create and install the translator
                translator = QTranslator()
                if translator.load("translations/MUSE.zh_CN.qm"):
                    app.installTranslator(translator)
    
    except FileNotFoundError:
        config['Settings'] = {'Language': '0'}  # default language is '0'

    # Show splash screen
    splash_pix = QPixmap(":/png/loading.png")
    splash = QSplashScreen(splash_pix)
    splash.show()

    # Create and show main window
    window = MainWindow(config)

    splash.finish(window)
    window.show()

    # Run the application
    app.exec()


# if __name__ == "__main__":    
#     app = QApplication([])

#     config = configparser.ConfigParser()

#     try:
#         # Try to read the config.ini file
#         config.read('config.ini')

#         # Check if 'Settings' section and 'Language' option exist
#         if 'Settings' in config and 'Language' in config['Settings']:
#             if config['Settings']['Language'] == '1':
#                 # Create and install the translator
#                 translator = QTranslator()
#                 if translator.load("translations/MUSE.zh_CN.qm"):
#                     app.installTranslator(translator)
#         else:
#             print("Warning: The configuration file is missing the 'Settings' section or 'Language' option. Using default settings.")
    
#     except FileNotFoundError:
#         print("Warning: config.ini file does not exist. Using default settings.")
#         # Use default settings
#         config['Settings'] = {'Language': '0'}  # default language is '0'

#     except Exception as e:
#         print(f"An error occurred: {e}")

#     # Show splash screen
#     splash_pix = QPixmap(":/png/loading.png")
#     splash = QSplashScreen(splash_pix)
#     splash.show()

#     # Create and show main window
#     window = MainWindow(config)

#     splash.finish(window)
#     window.show()

#     # Run the application
#     app.exec()


