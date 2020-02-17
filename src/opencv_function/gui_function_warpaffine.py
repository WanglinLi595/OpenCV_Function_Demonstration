# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'function_warpaffine.ui'
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
        Form.resize(1310, 858)
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.explain_function = QTabWidget(Form)
        self.explain_function.setObjectName(u"explain_function")
        self.tab_explain = QWidget()
        self.tab_explain.setObjectName(u"tab_explain")
        self.text_browser = QTextBrowser(self.tab_explain)
        self.text_browser.setObjectName(u"text_browser")
        self.text_browser.setGeometry(QRect(11, 11, 611, 791))
        self.arg_group_box = QGroupBox(self.tab_explain)
        self.arg_group_box.setObjectName(u"arg_group_box")
        self.arg_group_box.setGeometry(QRect(640, 10, 641, 381))
        self.verticalLayout = QVBoxLayout(self.arg_group_box)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.arg_group_box)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.le_arg_1 = QLineEdit(self.arg_group_box)
        self.le_arg_1.setObjectName(u"le_arg_1")

        self.horizontalLayout_2.addWidget(self.le_arg_1)

        self.le_arg_2 = QLineEdit(self.arg_group_box)
        self.le_arg_2.setObjectName(u"le_arg_2")

        self.horizontalLayout_2.addWidget(self.le_arg_2)

        self.le_arg_3 = QLineEdit(self.arg_group_box)
        self.le_arg_3.setObjectName(u"le_arg_3")

        self.horizontalLayout_2.addWidget(self.le_arg_3)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.le_arg_4 = QLineEdit(self.arg_group_box)
        self.le_arg_4.setObjectName(u"le_arg_4")

        self.horizontalLayout_3.addWidget(self.le_arg_4)

        self.le_arg_5 = QLineEdit(self.arg_group_box)
        self.le_arg_5.setObjectName(u"le_arg_5")

        self.horizontalLayout_3.addWidget(self.le_arg_5)

        self.le_arg_6 = QLineEdit(self.arg_group_box)
        self.le_arg_6.setObjectName(u"le_arg_6")

        self.horizontalLayout_3.addWidget(self.le_arg_6)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.btn_arg_ok = QPushButton(self.arg_group_box)
        self.btn_arg_ok.setObjectName(u"btn_arg_ok")

        self.verticalLayout.addWidget(self.btn_arg_ok)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 3)
        self.verticalLayout.setStretch(2, 3)
        self.verticalLayout.setStretch(3, 1)
        self.explain_function.addTab(self.tab_explain, "")
        self.show_result = QWidget()
        self.show_result.setObjectName(u"show_result")
        self.explain_function.addTab(self.show_result, "")

        self.horizontalLayout.addWidget(self.explain_function)


        self.retranslateUi(Form)

        self.explain_function.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.text_browser.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'SimSun'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u51fd\u6570\u8bf4\u660e\uff1a</p></body></html>", None))
        self.arg_group_box.setTitle(QCoreApplication.translate("Form", u"\u53c2\u6570\u586b\u5199", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u53c2\u6570 M", None))
        self.btn_arg_ok.setText(QCoreApplication.translate("Form", u"\u786e\u5b9a", None))
        self.explain_function.setTabText(self.explain_function.indexOf(self.tab_explain), QCoreApplication.translate("Form", u"\u51fd\u6570\u8bf4\u660e", None))
        self.explain_function.setTabText(self.explain_function.indexOf(self.show_result), QCoreApplication.translate("Form", u"\u6548\u679c\u6f14\u793a", None))
    # retranslateUi

