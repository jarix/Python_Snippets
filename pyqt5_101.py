# -*- coding: utf-8 -*-
"""
    PyQt5 101
    
    Simple PyQt5 GUI Example
    
    Author: Jari Honkanen
"""

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    #win.setGeometry(xpos, ypos, width, height)
    win.setGeometry(200, 200, 480, 480)
    win.setWindowTitle("Hello PyQt5")

    label = QtWidgets.QLabel(win)
    label.setText("Hello, There!")
    label.move(50,50)

    win.show()
    sys.exit(app.exec_())

window()