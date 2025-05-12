# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'App_Home.ui'
##
## Created by: Qt User Interface Compiler version 6.8.3
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QGridLayout, QListWidget,
    QListWidgetItem, QScrollArea, QSizePolicy, QWidget)

class Ui_w_Home(object):
    def setupUi(self, w_Home):
        if not w_Home.objectName():
            w_Home.setObjectName(u"w_Home")
        w_Home.resize(746, 704)
        self.formLayout = QFormLayout(w_Home)
        self.formLayout.setObjectName(u"formLayout")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.listWidget = QListWidget(w_Home)
        self.listWidget.setObjectName(u"listWidget")

        self.gridLayout_2.addWidget(self.listWidget, 0, 0, 1, 1)


        self.formLayout.setLayout(0, QFormLayout.LabelRole, self.gridLayout_2)

        self.scrollArea = QScrollArea(w_Home)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 462, 684))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.scrollArea)


        self.retranslateUi(w_Home)

        QMetaObject.connectSlotsByName(w_Home)
    # setupUi

    def retranslateUi(self, w_Home):
        w_Home.setWindowTitle(QCoreApplication.translate("w_Home", u"Form", None))
    # retranslateUi

