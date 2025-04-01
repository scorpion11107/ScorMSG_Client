import sys
from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg

from App_Info.UI.App_Info import Ui_w_AccountInfo
import connector

class AppInfo (qtw.QWidget, Ui_w_AccountInfo):

    info_close = qtc.Signal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pb_Close.clicked.connect(self.close)

        response = connector.get_user_info()
        if response["status"] == "success":
            data = response["data"][0]
            self.lb_UserID.setText(data[0])
            self.lb_CreationDate.setText(data[1])

    @qtc.Slot()
    def close(self):
        self.info_close.emit()