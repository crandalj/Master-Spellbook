import sys

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QMainWindow, QApplication
from MasterSpellbookUI import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(QMainWindow, self).__init__(parent)
        self.setupUi(self)

if __name__ == '__main__':

    app = QApplication(sys.argv)

    form = MainWindow()
    form.show()

    sys.exit(app.exec_())
