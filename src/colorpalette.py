from PySide6.QtGui import *
import random


def generate_random_color() -> QColor:
    return QColor(random.randint(0, 255), random.randint(
        0, 255), random.randint(0, 255))
