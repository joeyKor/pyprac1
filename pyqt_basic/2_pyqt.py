import sys
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QApplication, QPushButton, QWidget, QPushButton, QMessageBox

class Exam(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        btn = QPushButton("exit", self)
        btn.resize(btn.sizeHint())
        btn.setToolTip('it is tip')
        btn.move(20, 30)
        btn.clicked.connect(QCoreApplication.instance().quit) # end of form

        self.setGeometry(300,300,400,500)
        self.setWindowTitle('first class')
        self.show()

    def closeEvent(self, QCloseEvent):
        ans = QMessageBox.question(self, "End confirm", "Do you want to quit", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if ans == QMessageBox.Yes:
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()
app = QApplication(sys.argv)
w = Exam()
sys.exit(app.exec_())