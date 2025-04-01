# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'App_Home.ui'
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
    QScrollArea, QSizePolicy, QTabWidget, QVBoxLayout,
    QWidget)

class Ui_w_Home(object):
    def setupUi(self, w_Home):
        if not w_Home.objectName():
            w_Home.setObjectName(u"w_Home")
        w_Home.resize(746, 704)
        self.gridLayout = QGridLayout(w_Home)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tabWidget = QTabWidget(w_Home)
        self.tabWidget.setObjectName(u"tabWidget")
        self.t_DM = QWidget()
        self.t_DM.setObjectName(u"t_DM")
        self.gridLayout_2 = QGridLayout(self.t_DM)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.groupBox = QGroupBox(self.t_DM)
        self.groupBox.setObjectName(u"groupBox")
        self.formLayout = QFormLayout(self.groupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.scrollArea = QScrollArea(self.groupBox)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 54, 601))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.scrollArea)

        self.scrollArea_2 = QScrollArea(self.groupBox)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 620, 601))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.scrollArea_2)


        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)

        self.tabWidget.addTab(self.t_DM, "")
        self.t_Groups = QWidget()
        self.t_Groups.setObjectName(u"t_Groups")
        self.gridLayout_3 = QGridLayout(self.t_Groups)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.groupBox_2 = QGroupBox(self.t_Groups)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.formLayout_2 = QFormLayout(self.groupBox_2)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.scrollArea_3 = QScrollArea(self.groupBox_2)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 54, 601))
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.scrollArea_3)

        self.scrollArea_4 = QScrollArea(self.groupBox_2)
        self.scrollArea_4.setObjectName(u"scrollArea_4")
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 620, 601))
        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_4)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.scrollArea_4)


        self.gridLayout_3.addWidget(self.groupBox_2, 0, 0, 1, 1)

        self.tabWidget.addTab(self.t_Groups, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 1, 1, 1)


        self.retranslateUi(w_Home)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(w_Home)
    # setupUi

    def retranslateUi(self, w_Home):
        w_Home.setWindowTitle(QCoreApplication.translate("w_Home", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("w_Home", u"Direct messages", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.t_DM), QCoreApplication.translate("w_Home", u"DM", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("w_Home", u"Group messages", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.t_Groups), QCoreApplication.translate("w_Home", u"Groups", None))
    # retranslateUi

