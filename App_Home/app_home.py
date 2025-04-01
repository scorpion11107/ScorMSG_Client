import sys
from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg

from App_Home.UI.App_Home import Ui_w_Home

class AppHome (qtw.QWidget, Ui_w_Home):
    def __init__(self):
        super().__init__()
        self.setupUi(self)