# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'headlineAPP.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_APP(object):
    def setupUi(self, APP):
        if not APP.objectName():
            APP.setObjectName(u"APP")
        APP.resize(377, 641)
        self.button = QPushButton(APP)
        self.button.setObjectName(u"button")
        self.button.setGeometry(QRect(270, 600, 93, 28))
        self.label = QLabel(APP)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(140, 10, 101, 31))
        self.listWidget = QListWidget(APP)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(60, 70, 261, 521))
        self.formLayoutWidget = QWidget(APP)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(60, 40, 261, 31))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.formLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.comboBox = QComboBox(self.formLayoutWidget)
        self.comboBox.setObjectName(u"comboBox")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.comboBox)


        self.retranslateUi(APP)

        QMetaObject.connectSlotsByName(APP)
    # setupUi

    def retranslateUi(self, APP):
        APP.setWindowTitle(QCoreApplication.translate("APP", u"Dialog", None))
        self.button.setText(QCoreApplication.translate("APP", u"\u83b7\u53d6\u6700\u65b0", None))
        self.label.setText(QCoreApplication.translate("APP", u"\u5fae\u535a\u70ed\u641c\u699c", None))
        self.label_2.setText(QCoreApplication.translate("APP", u"\u5386\u53f2\u67e5\u8be2", None))
    # retranslateUi

