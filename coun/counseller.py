from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtCore import QTimer
import urllib.request as req, sys, time
from coun import Ui_MainWindow

class Example(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

    def btn_clicked(self):
        content = self.lineEdit.text()
        cal_select = self.calendarWidget.selectedDate()
        self.label.setText(cal_select.toString())

app = QApplication([])
ex = Example()
sys.exit(app.exec_())