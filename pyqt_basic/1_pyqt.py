import sys
import os
import PyQt5
from PyQt5.QtGui import *
from PyQt5.QtCore import  *
from PyQt5.QtWidgets import *
from PyQt5 import uic

current_path = os.path.dirname(__file__)
form_class = uic.loadUiType("ui/cal_ui.ui")

class MainDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self, None)
        

app = QApplication(sys.argv)
main_dialog = MainDialog()
main_dialog.show()
app.exec_()

