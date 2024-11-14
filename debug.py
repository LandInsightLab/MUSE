import configparser
from PySide6.QtWidgets import QApplication, QSplashScreen
from PySide6.QtGui import QPixmap
from PySide6.QtCore import QCoreApplication, QDir, QTranslator, QLocale
from src.mainwindow import MainWindow  # Import MainWindow from src

if __name__ == "__main__":    
    app = QApplication([])

    config = configparser.ConfigParser()

    try:
        # Try to read the config.ini file
        config.read('config.ini')

        # Check if 'Settings' section and 'Language' option exist
        if 'Settings' in config and 'Language' in config['Settings']:
            if config['Settings']['Language'] == '1':
                # Create and install the translator
                translator = QTranslator()
                if translator.load("translations/MUSE.zh_CN.qm"):
                    app.installTranslator(translator)
        else:
            print("Warning: The configuration file is missing the 'Settings' section or 'Language' option. Using default settings.")
    
    except FileNotFoundError:
        print("Warning: config.ini file does not exist. Using default settings.")
        # Use default settings
        config['Settings'] = {'Language': '0'}  # default language is '0'

    except Exception as e:
        print(f"An error occurred: {e}")

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