# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'function_getrotationmatrix2d.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_function_getRotationMatrix2D(object):
    def setupUi(self, function_getRotationMatrix2D):
        if function_getRotationMatrix2D.objectName():
            function_getRotationMatrix2D.setObjectName(u"function_getRotationMatrix2D")
        function_getRotationMatrix2D.resize(1170, 829)
        self.horizontalLayout_4 = QHBoxLayout(function_getRotationMatrix2D)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.textBrowser = QTextBrowser(function_getRotationMatrix2D)
        self.textBrowser.setObjectName(u"textBrowser")

        self.horizontalLayout_4.addWidget(self.textBrowser)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox = QGroupBox(function_getRotationMatrix2D)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.lineEdit = QLineEdit(self.groupBox)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout.addWidget(self.lineEdit)

        self.lineEdit_2 = QLineEdit(self.groupBox)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.horizontalLayout.addWidget(self.lineEdit_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.lineEdit_3 = QLineEdit(self.groupBox)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.horizontalLayout_2.addWidget(self.lineEdit_3)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.lineEdit_4 = QLineEdit(self.groupBox)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.horizontalLayout_3.addWidget(self.lineEdit_4)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.verticalLayout_2.addWidget(self.groupBox)

        self.label_4 = QLabel(function_getRotationMatrix2D)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_2.addWidget(self.label_4)

        self.textBrowser_2 = QTextBrowser(function_getRotationMatrix2D)
        self.textBrowser_2.setObjectName(u"textBrowser_2")

        self.verticalLayout_2.addWidget(self.textBrowser_2)


        self.horizontalLayout_4.addLayout(self.verticalLayout_2)

        self.horizontalLayout_4.setStretch(0, 9)
        self.horizontalLayout_4.setStretch(1, 1)

        self.retranslateUi(function_getRotationMatrix2D)

        QMetaObject.connectSlotsByName(function_getRotationMatrix2D)
    # setupUi

    def retranslateUi(self, function_getRotationMatrix2D):
        function_getRotationMatrix2D.setWindowTitle(QCoreApplication.translate("function_getRotationMatrix2D", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("function_getRotationMatrix2D", u"\u53c2\u6570\u8bf4\u660e", None))
        self.label.setText(QCoreApplication.translate("function_getRotationMatrix2D", u"center\uff1a", None))
        self.label_2.setText(QCoreApplication.translate("function_getRotationMatrix2D", u"angle\uff1a", None))
        self.label_3.setText(QCoreApplication.translate("function_getRotationMatrix2D", u"scale\uff1a", None))
        self.label_4.setText(QCoreApplication.translate("function_getRotationMatrix2D", u"\u8f93\u51fa\u7ed3\u679c", None))
    # retranslateUi

