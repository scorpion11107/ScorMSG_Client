import sys
from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg

import core
from App_Main.UI.App_Main import Ui_mw_Main

class AppMain (qtw.QMainWindow, Ui_mw_Main):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.home_widget = qtw.QWidget()
        self.settings_widget = qtw.QWidget()
        self.info_widget = qtw.QWidget()
        self.login_form = qtw.QDialog()
        self.register_form = qtw.QDialog()

        self.ma_Close.triggered.connect(self.close)

        self.ma_Info.triggered.connect(self.show_info)
        self.ma_Settings.triggered.connect(self.show_settings)
        self.ma_Logout.triggered.connect(self.logout)

        if not core.get("connected"):
            self.show_login()
        else:
            self.launch()

    def show_login(self):
        from App_Login.app_login import AppLogin

        self.login_form = AppLogin()
        self.login_form.login_success.connect(self.launch)
        self.login_form.login_cancel.connect(self.close)
        self.login_form.show_register.connect(self.show_register)
        self.login_form.rejected.connect(self.close)

        self.register_form.accept()

        self.login_form.show()

    def show_register(self):
        from App_Register.app_register import AppRegister

        self.register_form = AppRegister()
        self.register_form.register_success.connect(self.show_login)
        self.register_form.register_cancel.connect(self.close)
        self.register_form.show_login.connect(self.show_login)
        self.register_form.rejected.connect(self.close)

        self.login_form.accept()

        self.register_form.show()

    @qtc.Slot()
    def show_info(self):
        from App_Info.app_info import AppInfo

        if core.get("connected"):
            self.info_widget = AppInfo()
            self.info_widget.info_close.connect(self.info_close)

            res = self.info_widget.update_data()
            if res[0]:
                self.setCentralWidget(self.info_widget)
            else:
                self.status(res[1])
        else:
            self.status("No account logged in")

    @qtc.Slot()
    def info_close(self):
        self.show_home()

    @qtc.Slot()
    def show_settings(self):
        from App_Settings.app_settings import AppSettings

        self.settings_widget = AppSettings()
        self.settings_widget.settings_close.connect(self.settings_cancel)
        self.settings_widget.settings_save.connect(self.settings_save)

        self.setCentralWidget(self.settings_widget)

    @qtc.Slot()
    def logout(self):
        if core.get("connected"):
            res = core.logout()

            if res[0]:
                self.close()
            else:
                self.status(res[1])
        else:
            self.status("No account logged in")

    @qtc.Slot()
    def settings_save(self):
        self.status("Settings saved")
        self.show_home()

    @qtc.Slot()
    def settings_cancel(self):
        self.show_home()

    def show_home(self):
        from App_Home.app_home import AppHome

        self.home_widget = AppHome()
        self.setCentralWidget(self.home_widget)

    def launch(self):
        self.show_home()
        self.show()

    def status(self, text):
        self.statusbar.showMessage(text, 3000)