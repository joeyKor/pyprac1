import sys
from PyQt5.QtWidgets import QAction, QApplication, QMainWindow, QMenu

class Exam(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.statusBar()
        self.statusBar().showMessage("hi. status")

        menu = self.menuBar()
        menu_file = menu.addMenu('File')
        menu_edit = menu.addMenu('Edit')

        file_exit = QAction('Exit', self)
        file_exit.setShortcut('Ctrl+Q')
        file_exit.setStatusTip('End of Application')

        file_new = QMenu('New', self)

        menu_file.addMenu(file_new)
        menu_file.addAction(file_exit)

        self.resize(450, 400)
        self.show()

app = QApplication(sys.argv)
w = Exam()
sys.exit(app.exec_())