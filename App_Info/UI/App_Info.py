# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'App_Info.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QGridLayout, QGroupBox,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QWidget)
import Icons_rc

class Ui_w_AccountInfo(object):
    def setupUi(self, w_AccountInfo):
        if not w_AccountInfo.objectName():
            w_AccountInfo.setObjectName(u"w_AccountInfo")
        w_AccountInfo.resize(707, 671)
        self.gridLayout = QGridLayout(w_AccountInfo)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pb_Close = QPushButton(w_AccountInfo)
        self.pb_Close.setObjectName(u"pb_Close")
        icon = QIcon()
        icon.addFile(u":/General/Cancel.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pb_Close.setIcon(icon)

        self.gridLayout.addWidget(self.pb_Close, 1, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.groupBox = QGroupBox(w_AccountInfo)
        self.groupBox.setObjectName(u"groupBox")
        self.formLayout = QFormLayout(self.groupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.lb_UserID_Descriptor = QLabel(self.groupBox)
        self.lb_UserID_Descriptor.setObjectName(u"lb_UserID_Descriptor")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.lb_UserID_Descriptor)

        self.lb_UserID = QLabel(self.groupBox)
        self.lb_UserID.setObjectName(u"lb_UserID")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lb_UserID)

        self.lb_CreationDate_Descriptor = QLabel(self.groupBox)
        self.lb_CreationDate_Descriptor.setObjectName(u"lb_CreationDate_Descriptor")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.lb_CreationDate_Descriptor)

        self.lb_CreationDate = QLabel(self.groupBox)
        self.lb_CreationDate.setObjectName(u"lb_CreationDate")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lb_CreationDate)


        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 2)


        self.retranslateUi(w_AccountInfo)

        QMetaObject.connectSlotsByName(w_AccountInfo)
    # setupUi

    def retranslateUi(self, w_AccountInfo):
        w_AccountInfo.setWindowTitle(QCoreApplication.translate("w_AccountInfo", u"Form", None))
        self.pb_Close.setText(QCoreApplication.translate("w_AccountInfo", u"Close", None))
        self.groupBox.setTitle(QCoreApplication.translate("w_AccountInfo", u"Account", None))
        self.lb_UserID_Descriptor.setText(QCoreApplication.translate("w_AccountInfo", u"User ID:", None))
        self.lb_UserID.setText(QCoreApplication.translate("w_AccountInfo", u"TextLabel", None))
        self.lb_CreationDate_Descriptor.setText(QCoreApplication.translate("w_AccountInfo", u"Account creation date:", None))
        self.lb_CreationDate.setText(QCoreApplication.translate("w_AccountInfo", u"TextLabel", None))
    # retranslateUi

