import sys
from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg

import core
from App_Login.UI.App_Login import Ui_dl_Login

class AppLogin (qtw.QDialog, Ui_dl_Login):

    login_success = qtc.Signal()
    login_cancel = qtc.Signal()
    show_register = qtc.Signal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.password_hidden = True

        self.lb_Message.clear()

        self.pb_ShowPassword.clicked.connect(self.show_password)
        self.pb_Cancel.clicked.connect(self.cancel)
        self.pb_Confirm.clicked.connect(self.confirm)
        self.pb_Register.clicked.connect(self.register)

        self.le_UserID.setText(core.get("username"))

    @qtc.Slot()
    def show_password(self):
        if self.password_hidden:
            self.le_Password.setEchoMode(qtw.QLineEdit.EchoMode.Normal)
            self.pb_ShowPassword.setIcon(qtg.QIcon(":/General/Hide_Password.png"))
        else:
            self.le_Password.setEchoMode(qtw.QLineEdit.EchoMode.Password)
            self.pb_ShowPassword.setIcon(qtg.QIcon(":/General/Show_Password.png"))
        self.password_hidden = not self.password_hidden

    @qtc.Slot()
    def confirm(self):
        username = self.le_UserID.text()
        password = self.le_Password.text()

        if not username or not password:
            self.lb_Message.setText("Missing User ID or Password")
        else:
            res = core.login(username, password)
            if res[0]:
                self.login_success.emit()
                self.accept()
            else:
                self.lb_Message.setText(res[1])

    @qtc.Slot()
    def cancel(self):
        self.login_cancel.emit()
        self.close()

    @qtc.Slot()
    def register(self):
        self.show_register.emit()