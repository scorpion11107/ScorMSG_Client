# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'App_Main.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QStatusBar, QWidget)
import Icons_rc

class Ui_mw_Main(object):
    def setupUi(self, mw_Main):
        if not mw_Main.objectName():
            mw_Main.setObjectName(u"mw_Main")
        mw_Main.resize(1227, 688)
        icon = QIcon()
        icon.addFile(u":/General/App_Icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        mw_Main.setWindowIcon(icon)
        self.ma_Close = QAction(mw_Main)
        self.ma_Close.setObjectName(u"ma_Close")
        icon1 = QIcon()
        icon1.addFile(u":/General/Cancel.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.ma_Close.setIcon(icon1)
        self.ma_Login = QAction(mw_Main)
        self.ma_Login.setObjectName(u"ma_Login")
        icon2 = QIcon()
        icon2.addFile(u":/General/Login.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.ma_Login.setIcon(icon2)
        self.ma_Register = QAction(mw_Main)
        self.ma_Register.setObjectName(u"ma_Register")
        icon3 = QIcon()
        icon3.addFile(u":/General/Register.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.ma_Register.setIcon(icon3)
        self.ma_Info = QAction(mw_Main)
        self.ma_Info.setObjectName(u"ma_Info")
        icon4 = QIcon()
        icon4.addFile(u":/General/Account.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.ma_Info.setIcon(icon4)
        self.ma_Settings = QAction(mw_Main)
        self.ma_Settings.setObjectName(u"ma_Settings")
        icon5 = QIcon()
        icon5.addFile(u":/General/Settings.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.ma_Settings.setIcon(icon5)
        self.ma_Logout = QAction(mw_Main)
        self.ma_Logout.setObjectName(u"ma_Logout")
        icon6 = QIcon()
        icon6.addFile(u":/General/Logout.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.ma_Logout.setIcon(icon6)
        self.centralwidget = QWidget(mw_Main)
        self.centralwidget.setObjectName(u"centralwidget")
        mw_Main.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(mw_Main)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1227, 33))
        self.mn_File = QMenu(self.menubar)
        self.mn_File.setObjectName(u"mn_File")
        self.mn_Account = QMenu(self.menubar)
        self.mn_Account.setObjectName(u"mn_Account")
        mw_Main.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(mw_Main)
        self.statusbar.setObjectName(u"statusbar")
        mw_Main.setStatusBar(self.statusbar)

        self.menubar.addAction(self.mn_File.menuAction())
        self.menubar.addAction(self.mn_Account.menuAction())
        self.mn_File.addAction(self.ma_Close)
        self.mn_Account.addAction(self.ma_Info)
        self.mn_Account.addAction(self.ma_Settings)
        self.mn_Account.addSeparator()
        self.mn_Account.addAction(self.ma_Logout)

        self.retranslateUi(mw_Main)

        QMetaObject.connectSlotsByName(mw_Main)
    # setupUi

    def retranslateUi(self, mw_Main):
        mw_Main.setWindowTitle(QCoreApplication.translate("mw_Main", u"ScorMSG", None))
        self.ma_Close.setText(QCoreApplication.translate("mw_Main", u"Close", None))
        self.ma_Login.setText(QCoreApplication.translate("mw_Main", u"Login", None))
        self.ma_Register.setText(QCoreApplication.translate("mw_Main", u"Register", None))
        self.ma_Info.setText(QCoreApplication.translate("mw_Main", u"Info", None))
        self.ma_Settings.setText(QCoreApplication.translate("mw_Main", u"Settings", None))
        self.ma_Logout.setText(QCoreApplication.translate("mw_Main", u"Logout", None))
        self.mn_File.setTitle(QCoreApplication.translate("mw_Main", u"File", None))
        self.mn_Account.setTitle(QCoreApplication.translate("mw_Main", u"Account", None))
    # retranslateUi

