# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'function_cvtcolor.ui'
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


class Ui_Form(object):
    def setupUi(self, Form):
        if Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1211, 816)
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.tabWidget = QTabWidget(Form)
        self.tabWidget.setObjectName(u"tabWidget")
        self.function_explain = QWidget()
        self.function_explain.setObjectName(u"function_explain")
        self.horizontalLayout_2 = QHBoxLayout(self.function_explain)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.textBrowser = QTextBrowser(self.function_explain)
        self.textBrowser.setObjectName(u"textBrowser")

        self.horizontalLayout_2.addWidget(self.textBrowser)

        self.groupBox = QGroupBox(self.function_explain)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.cb_arg = QComboBox(self.groupBox)
        self.cb_arg.addItem("")
        self.cb_arg.addItem("")
        self.cb_arg.setObjectName(u"cb_arg")

        self.verticalLayout.addWidget(self.cb_arg)

        self.btn_arg_ok = QPushButton(self.groupBox)
        self.btn_arg_ok.setObjectName(u"btn_arg_ok")

        self.verticalLayout.addWidget(self.btn_arg_ok)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout_2.addWidget(self.groupBox)

        self.tabWidget.addTab(self.function_explain, "")
        self.show_result = QWidget()
        self.show_result.setObjectName(u"show_result")
        self.tabWidget.addTab(self.show_result, "")

        self.horizontalLayout.addWidget(self.tabWidget)


        self.retranslateUi(Form)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.textBrowser.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'SimSun'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">\u8272\u5f69\u7a7a\u95f4\uff08color space\uff09\u662f\u5bf9\u8272\u5f69\u7684\u7ec4\u7ec7\u65b9\u5f0f\u3002\u501f\u52a9\u8272\u5f69\u7a7a\u95f4\u548c\u9488\u5bf9\u7269\u7406\u8bbe\u5907\u7684\u6d4b\u8bd5\uff0c\u53ef\u4ee5\u5f97\u5230\u8272\u5f69\u7684\u56fa\u5b9a\u6a21\u62df\u548c\u6570\u5b57\u8868\u793a\u3002</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">\u5728 OpenCV \u4e2d\u4f7f\u7528 cv.cvtColor() \u51fd\u6570"
                        "\u6765\u6539\u53d8\u56fe\u7247\u7684\u8272\u5f69\u7a7a\u95f4\u3002</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">cv.cvtColor() \u51fd\u6570\u6709\u4e24\u4e2a\u4e3b\u8981\u53c2\u6570\uff0c\u4f9d\u6b21\u5206\u522b\u662f\uff1ainput_image, flag \u3002\u5176\u4e2d input \u4e3a\u8f93\u5165\u56fe\u7247\uff0c flag \u51b3\u5b9a\u8f6c\u6362\u7684\u7c7b\u578b\u3002</span></p></body></html>", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"\u53c2\u6570\u586b\u5199", None))
        self.label.setText(QCoreApplication.translate("Form", u"flag:", None))
        self.cb_arg.setItemText(0, QCoreApplication.translate("Form", u"cv.COLOR_BGR2GRAY", None))
        self.cb_arg.setItemText(1, QCoreApplication.translate("Form", u"cv.COLOR_BGR2HSV", None))

        self.btn_arg_ok.setText(QCoreApplication.translate("Form", u"\u786e\u5b9a", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.function_explain), QCoreApplication.translate("Form", u"\u51fd\u6570\u8bf4\u660e", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.show_result), QCoreApplication.translate("Form", u"\u51fd\u6570\u6548\u679c", None))
    # retranslateUi

