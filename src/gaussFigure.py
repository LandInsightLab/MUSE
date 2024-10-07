from resources.ui.gaussFigure_ui import Ui_GaussFigureWidget

from PySide6 import QtWidgets
from PySide6.QtWidgets import QWidget, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class GaussFigure(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_GaussFigureWidget()
        self.ui.setupUi(self)  
        self.plot_layout = QVBoxLayout()
    
    def update_widget_with_plot(self, fig):
        # Create a FigureCanvas from the figure
        canvas = FigureCanvas(fig)

        # Clear existing layout and add the canvas to the widget
        layout = QtWidgets.QVBoxLayout()
        self.setLayout(layout)
        layout.addWidget(canvas)

        # Draw the figure
        canvas.draw()