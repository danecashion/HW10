#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os

from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt 

import time
import RPi.GPIO as GPI0

from PyQt5.uic import loadUi

from BUTTON import Ui_MainWindow

GPI0.setmode(GPI0.BCM)
GPI0.setwarnings(False)

class Window(QMainWindow, Ui_MainWindow):
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowTitle('LED button')  
        self.LED.pressed.connect(lambda: self.on())  
        self.LED.released.connect(lambda: self.off()) 
        GPI0.setup(17, GPI0.IN, pull_up_down=GPI0.PUD_DOWN)
        start_time = time.time()
        elapsed_time = 0.0
        while elapsed_time < 10:
            if GPI0.input(17) == GPI0.HIGH:
                self.indicator.setChecked(True)
                time.sleep(0.1) 
                elapsed_time = time.time() - start_time
        

    
    def on(self):
        GPI0.setup(18, GPI0.OUT)
        GPI0.output(18, GPI0.HIGH)
    
    def off(self):
        GPI0.setup(18, GPI0.OUT)
        GPI0.output(18, GPI0.LOW)

    def short():
        GPI0.setup(17, GPI0.IN, pull_up_down=GPI0.PUD_DOWN)
        start_time = time.time()
        elapsed_time = 0.0
        while elapsed_time < 10:
            if GPI0.input(17) == GPI0.HIGH:
                time.sleep(0.1) 
                elapsed_time = time.time() - start_time

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())