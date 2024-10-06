from PySide6.QtWidgets import QApplication, QTextBrowser, QMenu
from PySide6.QtGui import QAction
from PySide6.QtCore import Qt



class CustomTextBrowser(QTextBrowser):
    def __init__(self, message):
        super().__init__()
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.show_context_menu)

    def show_context_menu(self, pos):
        menu = QMenu(self)
        
        # Action to copy selected text
        copy_action = QAction('Copy', self)
        copy_action.triggered.connect(self.copy)
        menu.addAction(copy_action)

        # Action to select all text
        select_all_action = QAction('Select All', self)
        select_all_action.triggered.connect(self.selectAll)
        menu.addAction(select_all_action)
        
        # Action to clear all information
        clear_action = QAction('Clear All', self)
        clear_action.triggered.connect(self.clear)
        menu.addAction(clear_action)
        
        menu.exec_(self.mapToGlobal(pos))
        
