import sys

from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg

from App_Register.UI.App_Register import Ui_dl_Register

class AppRegister (qtw.QDialog, Ui_dl_Register):

    register_success = qtc.Signal()
    register_cancel = qtc.Signal()
    show_login = qtc.Signal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.password_hidden = True

        self.lb_Message.clear()

        self.pb_ShowPassword.clicked.connect(self.show_password)
        self.pb_Cancel.clicked.connect(self.close)
        self.pb_Confirm.clicked.connect(self.register)
        self.pb_Login.clicked.connect(self.login)

        self.show()

    @qtc.Slot()
    def show_password(self):
        if self.password_hidden:
            self.le_Password.setEchoMode(qtw.QLineEdit.EchoMode.Normal)
            self.le_ConfirmPassword.setEchoMode(qtw.QLineEdit.EchoMode.Normal)
            self.pb_ShowPassword.setIcon(qtg.QIcon(":/General/Hide_Password.png"))
            self.password_hidden = False
        else:
            self.le_Password.setEchoMode(qtw.QLineEdit.EchoMode.Password)
            self.le_ConfirmPassword.setEchoMode(qtw.QLineEdit.EchoMode.Password)
            self.pb_ShowPassword.setIcon(qtg.QIcon(":/General/Show_Password.png"))
            self.password_hidden = True

    @qtc.Slot()
    def register(self):
        import core

        userid = self.le_UserID.text()
        password = self.le_Password.text()
        confirm_password = self.le_ConfirmPassword.text()

        if not userid or not password or not confirm_password:
            self.lb_Message.setText("Missing User ID, Password or Password confirmation")
        elif password != confirm_password:
            self.lb_Message.setText("Passwords do not match")
        else:
            res = core.register(userid, password)
            if res[0]:
                self.register_success.emit()
                self.close()
            else:
                self.lb_Message.setText(res[1])

    @qtc.Slot()
    def login(self):
        self.show_login.emit()