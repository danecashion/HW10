#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os

from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt 

import time
import RPi.GPI0 as GPI0

from PyQt5.uic import loadUi, QtCore

from BUTTON import Ui_MainWindow

GPI0.setmode(GPI0.BCM)
GPI0.setwarnings(False)

class Window(QMainWindow, Ui_MainWindow):
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowTitle('LED button')  
        QtCore.QObject.connect(self.LED,QtCore.SIGNAL("clocked()"), self.function)   
    
    def function():
        GPI0.setup(18, GPI0.OUT)
        GPI0.output(18, GPI0.HIGH)
        time.sleep(2)
        GPI0.output(18, GPI0.LOW)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())