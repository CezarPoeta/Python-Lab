from PySide6 import QtCore
from PySide6.QtCore import QCoreApplication
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (QApplication, QMainWindow)
from ui_main import Ui_MainWindow
import sys

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Sistema Financeiro Pessoal")
        appIcon = QIcon(u"")
        self.setWindowIcon(appIcon)

        self.btn_toggle.clicked.connect(self.LeftMenu)

    def LeftMenu(self):
        width = self.F01menu.width()
        if width == 9:
            newWidth = 200
        else:
            newWidth = 9    
        self.animation = QtCore.QPropertyAnimation(self.F01menu, b"maximumWidth")
        self.animation.setDuration(500)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWidth)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()