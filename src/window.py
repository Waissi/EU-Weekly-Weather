from PySide6.QtWidgets import *
from PySide6.QtCharts import *
from panel import Panel


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("EU Weekly Weather")
        self.setFixedSize(1200, 800)
        self.show()
        self.setCentralWidget(Panel())
