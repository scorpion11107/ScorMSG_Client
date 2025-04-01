# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'App_Login.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QGroupBox,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QWidget)
import Icons_rc

class Ui_dl_Login(object):
    def setupUi(self, dl_Login):
        if not dl_Login.objectName():
            dl_Login.setObjectName(u"dl_Login")
        dl_Login.setWindowModality(Qt.WindowModality.WindowModal)
        dl_Login.resize(500, 200)
        icon = QIcon()
        icon.addFile(u":/General/App_Icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        dl_Login.setWindowIcon(icon)
        self.gridLayout = QGridLayout(dl_Login)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 3, 1, 1, 1)

        self.pb_Confirm = QPushButton(dl_Login)
        self.pb_Confirm.setObjectName(u"pb_Confirm")
        icon1 = QIcon()
        icon1.addFile(u":/General/Check.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pb_Confirm.setIcon(icon1)

        self.gridLayout.addWidget(self.pb_Confirm, 3, 4, 1, 1)

        self.pb_Cancel = QPushButton(dl_Login)
        self.pb_Cancel.setObjectName(u"pb_Cancel")
        icon2 = QIcon()
        icon2.addFile(u":/General/Cancel.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pb_Cancel.setIcon(icon2)

        self.gridLayout.addWidget(self.pb_Cancel, 3, 3, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 1, 1, 1, 4)

        self.pb_Register = QPushButton(dl_Login)
        self.pb_Register.setObjectName(u"pb_Register")
        icon3 = QIcon()
        icon3.addFile(u":/General/Register.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pb_Register.setIcon(icon3)

        self.gridLayout.addWidget(self.pb_Register, 3, 0, 1, 1)

        self.lb_Message = QLabel(dl_Login)
        self.lb_Message.setObjectName(u"lb_Message")

        self.gridLayout.addWidget(self.lb_Message, 2, 0, 1, 5)

        self.groupBox = QGroupBox(dl_Login)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.le_Password = QLineEdit(self.groupBox)
        self.le_Password.setObjectName(u"le_Password")
        self.le_Password.setEchoMode(QLineEdit.EchoMode.Password)

        self.gridLayout_2.addWidget(self.le_Password, 1, 1, 1, 1)

        self.lb_UserID = QLabel(self.groupBox)
        self.lb_UserID.setObjectName(u"lb_UserID")

        self.gridLayout_2.addWidget(self.lb_UserID, 0, 0, 1, 1)

        self.lb_Password = QLabel(self.groupBox)
        self.lb_Password.setObjectName(u"lb_Password")

        self.gridLayout_2.addWidget(self.lb_Password, 1, 0, 1, 1)

        self.pb_ShowPassword = QPushButton(self.groupBox)
        self.pb_ShowPassword.setObjectName(u"pb_ShowPassword")
        icon4 = QIcon()
        icon4.addFile(u":/General/Show_Password.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pb_ShowPassword.setIcon(icon4)

        self.gridLayout_2.addWidget(self.pb_ShowPassword, 1, 2, 1, 1)

        self.le_UserID = QLineEdit(self.groupBox)
        self.le_UserID.setObjectName(u"le_UserID")

        self.gridLayout_2.addWidget(self.le_UserID, 0, 1, 1, 2)


        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 5)

        QWidget.setTabOrder(self.le_UserID, self.le_Password)
        QWidget.setTabOrder(self.le_Password, self.pb_ShowPassword)
        QWidget.setTabOrder(self.pb_ShowPassword, self.pb_Cancel)

        self.retranslateUi(dl_Login)

        self.pb_Confirm.setDefault(True)


        QMetaObject.connectSlotsByName(dl_Login)
    # setupUi

    def retranslateUi(self, dl_Login):
        dl_Login.setWindowTitle(QCoreApplication.translate("dl_Login", u"ScorMSG  -  Login", None))
        self.pb_Confirm.setText(QCoreApplication.translate("dl_Login", u"Confirm", None))
        self.pb_Cancel.setText(QCoreApplication.translate("dl_Login", u"Cancel", None))
        self.pb_Register.setText(QCoreApplication.translate("dl_Login", u"Register", None))
        self.lb_Message.setText(QCoreApplication.translate("dl_Login", u"Message", None))
        self.groupBox.setTitle(QCoreApplication.translate("dl_Login", u"Login", None))
        self.lb_UserID.setText(QCoreApplication.translate("dl_Login", u"User ID", None))
        self.lb_Password.setText(QCoreApplication.translate("dl_Login", u"Password", None))
        self.pb_ShowPassword.setText("")
    # retranslateUi

