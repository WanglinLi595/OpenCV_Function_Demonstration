# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'opencv_function.ui'
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
        self.explain_function = QTabWidget(Form)
        self.explain_function.setObjectName(u"explain_function")
        self.explain_function.setGeometry(QRect(0, 40, 1321, 831))
        self.tab_explain = QWidget()
        self.tab_explain.setObjectName(u"tab_explain")
        self.textBrowser = QTextBrowser(self.tab_explain)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(30, 50, 771, 711))
        self.explain_function.addTab(self.tab_explain, "")
        self.show_result = QWidget()
        self.show_result.setObjectName(u"show_result")
        self.horizontalLayout = QHBoxLayout(self.show_result)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.original_table_view = QTableView(self.show_result)
        self.original_table_view.setObjectName(u"original_table_view")

        self.verticalLayout.addWidget(self.original_table_view)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.result_table_view = QTableView(self.show_result)
        self.result_table_view.setObjectName(u"result_table_view")

        self.verticalLayout_2.addWidget(self.result_table_view)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.explain_function.addTab(self.show_result, "")

        self.retranslateUi(Form)

        self.explain_function.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.explain_function.setTabText(self.explain_function.indexOf(self.tab_explain), QCoreApplication.translate("Form", u"\u51fd\u6570\u8bf4\u660e", None))
        self.explain_function.setTabText(self.explain_function.indexOf(self.show_result), QCoreApplication.translate("Form", u"\u6548\u679c\u6f14\u793a", None))
    # retranslateUi

