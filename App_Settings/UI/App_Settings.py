# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'App_Settings.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFormLayout, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QWidget)
import Icons_rc

class Ui_w_Settings(object):
    def setupUi(self, w_Settings):
        if not w_Settings.objectName():
            w_Settings.setObjectName(u"w_Settings")
        w_Settings.resize(725, 582)
        self.gridLayout = QGridLayout(w_Settings)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.pb_Close = QPushButton(w_Settings)
        self.pb_Close.setObjectName(u"pb_Close")
        icon = QIcon()
        icon.addFile(u":/General/Cancel.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pb_Close.setIcon(icon)

        self.gridLayout.addWidget(self.pb_Close, 1, 1, 1, 1)

        self.pb_Save = QPushButton(w_Settings)
        self.pb_Save.setObjectName(u"pb_Save")
        icon1 = QIcon()
        icon1.addFile(u":/General/Save.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pb_Save.setIcon(icon1)

        self.gridLayout.addWidget(self.pb_Save, 1, 2, 1, 1)

        self.groupBox_5 = QGroupBox(w_Settings)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.horizontalLayout = QHBoxLayout(self.groupBox_5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.scrollArea = QScrollArea(self.groupBox_5)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 685, 496))
        self.gridLayout_2 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 1, 0, 1, 1)

        self.groupBox = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox.setObjectName(u"groupBox")
        self.formLayout_2 = QFormLayout(self.groupBox)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.le_ServerAddress = QLineEdit(self.groupBox)
        self.le_ServerAddress.setObjectName(u"le_ServerAddress")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.le_ServerAddress)

        self.lb_ServerAddress = QLabel(self.groupBox)
        self.lb_ServerAddress.setObjectName(u"lb_ServerAddress")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.lb_ServerAddress)

        self.lb_ServerPort = QLabel(self.groupBox)
        self.lb_ServerPort.setObjectName(u"lb_ServerPort")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.lb_ServerPort)

        self.le_ServerPort = QLineEdit(self.groupBox)
        self.le_ServerPort.setObjectName(u"le_ServerPort")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.le_ServerPort)

        self.cb_DevServer = QCheckBox(self.groupBox)
        self.cb_DevServer.setObjectName(u"cb_DevServer")
        self.cb_DevServer.setChecked(False)
        self.cb_DevServer.setTristate(False)

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.cb_DevServer)


        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout.addWidget(self.scrollArea)


        self.gridLayout.addWidget(self.groupBox_5, 0, 0, 1, 3)


        self.retranslateUi(w_Settings)

        self.pb_Save.setDefault(True)


        QMetaObject.connectSlotsByName(w_Settings)
    # setupUi

    def retranslateUi(self, w_Settings):
        w_Settings.setWindowTitle(QCoreApplication.translate("w_Settings", u"Form", None))
        self.pb_Close.setText(QCoreApplication.translate("w_Settings", u"Close", None))
        self.pb_Save.setText(QCoreApplication.translate("w_Settings", u"Save", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("w_Settings", u"Settings", None))
        self.groupBox.setTitle(QCoreApplication.translate("w_Settings", u"Network", None))
        self.lb_ServerAddress.setText(QCoreApplication.translate("w_Settings", u"Server address:", None))
        self.lb_ServerPort.setText(QCoreApplication.translate("w_Settings", u"Server port:", None))
        self.cb_DevServer.setText(QCoreApplication.translate("w_Settings", u"Use '127.0.0.1.4443'", None))
    # retranslateUi

