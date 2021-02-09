# -*- coding: utf-8 -*-
"""
    PyQt5 Widget sample
    
    Simple PyQt5 GUI Widget Example
    Main file to be used with generated pyqt5_loginbox_widget.py,
    generated with pyuic5 from pyqt_loginbox_widget.ui

    $ pyuic5 pyqt5_loginbox_widget.ui -o pyqt5_loginbox_widget.py
    
    Author: Jari Honkanen
"""
from pyqt5_loginbox_widget import Ui_Form

from PyQt5 import QtWidgets as qtw 
from PyQt5 import QtCore as qtc 

class LoginWindow(qtw.QWidget):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.authenticate)

    def authenticate(self):

        username = self.ui.username_edit.text()
        password = self.ui.password_edit.text()

        if username == 'user' and password == 'pass':
            qtw.QMessageBox.information(self, 'Success', "Login Successful")
        else:
            qtw.QMessageBox.warning(self, 'Fail', "Login Unsuccessful")


if __name__ == '__main__':
    app = qtw.QApplication([])

    widget = LoginWindow()
    widget.show()

    app.exec_()