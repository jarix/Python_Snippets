# -*- coding: utf-8 -*-
"""
    PyQt5 101
    
    Simple PyQt5 GUI Example
    
    Author: Jari Honkanen
"""

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(200, 200, 480, 480)
        self.setWindowTitle("Hello PyQt5")
        self.initUI()

    def initUI(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Hello, There!")
        self.label.move(50,50)

        self.button1 = QtWidgets.QPushButton(self)
        self.button1.setText("Click Me!")
        self.button1.clicked.connect(self.clicked)

    def clicked(self):
        self.button1.setText("Clicked!")
        self.label.setText("You pressed the button!")
        self.label.adjustSize()
        print("Button pressed")


def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())

window()