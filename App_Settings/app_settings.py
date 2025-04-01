import sys
from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg

from App_Settings.UI.App_Settings import Ui_w_Settings
import core

class AppSettings (qtw.QWidget, Ui_w_Settings):

    settings_close = qtc.Signal()
    settings_save = qtc.Signal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.cb_DevServer.stateChanged.connect(self.dev_settings)
        self.pb_Save.clicked.connect(self.save)
        self.pb_Close.clicked.connect(self.cancel)

        self.le_ServerAddress.setText(core.get("server_address"))
        self.le_ServerPort.setText(core.get("server_port"))
        self.cb_DevServer.setChecked(core.get("dev_settings") == True)

    @qtc.Slot()
    def dev_settings(self, state):
        if state == 2:
            self.le_ServerAddress.setDisabled(True)
            self.le_ServerPort.setDisabled(True)
            self.lb_ServerAddress.setDisabled(True)
            self.lb_ServerPort.setDisabled(True)
        else:
            self.le_ServerAddress.setDisabled(False)
            self.le_ServerPort.setDisabled(False)
            self.lb_ServerAddress.setDisabled(False)
            self.lb_ServerPort.setDisabled(False)

    @qtc.Slot()
    def cancel(self):
        self.settings_close.emit()

    @qtc.Slot()
    def save(self):
        core.save({"key": "server_address", "value": self.le_ServerAddress.text()})
        core.save({"key": "server_port", "value": self.le_ServerPort.text()})
        core.save({"key": "dev_settings", "value": self.cb_DevServer.isChecked()})

        self.settings_save.emit()