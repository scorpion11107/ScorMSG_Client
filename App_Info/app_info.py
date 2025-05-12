import sys
from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg

from App_Info.UI.App_Info import Ui_w_AccountInfo
import core

class AppInfo (qtw.QWidget, Ui_w_AccountInfo):

    info_close = qtc.Signal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def update_data(self):
        res = core.get_user_info()
        if res[0]:
            data = res[1]
        else:
            data = ["N/A", "N/A"]

        self.pb_Close.clicked.connect(self.info_close.emit)
        self.lb_UserID.setText(data[0])
        self.lb_CreationDate.setText(data[1])

        return res