import sys
from PySide6 import QtWidgets
from window import Window

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = Window()
    sys.exit(app.exec())
