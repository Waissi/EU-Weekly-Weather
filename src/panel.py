from PySide6.QtCore import *
from PySide6.QtWidgets import *
from graphdisplay import GraphDisplay


class Panel(QWidget):
    def __init__(self):
        super().__init__()

        cities = ["Berlin", "Paris", "Amsterdam", "Athens", "Bucharest", "Bratislava", "Ljubljana", "Prague", "Riga", "Vilnius", "Sofia", "Vienna", "Dublin", "Tallinn", "Lisbon",
                  "Rome", "Madrid", "Stockholm", "Brussels", "Budapest", "Zagreb", "Nicosia", "Copenhagen", "Helsinki", "Luxembourg", "Valleta", "Warsaw"]
        cities.sort()

        self.dataDisplay = GraphDisplay()
        self.listWidget = QListWidget()
        self.listWidget.setSelectionMode(
            QAbstractItemView.SelectionMode.MultiSelection)
        for city in cities:
            self.listWidget.addItem(QListWidgetItem(city))
        self.listWidget.clicked[QModelIndex].connect(
            self.city_selection_callback)

        self.layout = QHBoxLayout(self)
        self.layout.addWidget(self.dataDisplay, 9)
        self.layout.addWidget(self.listWidget, 1)

    def city_selection_callback(self, index: QModelIndex):
        item = self.listWidget.itemFromIndex(index)
        city = item.text()
        self.dataDisplay.update(city)
