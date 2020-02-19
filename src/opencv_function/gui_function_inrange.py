# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'function_inrange.ui'
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
        Form.resize(1153, 825)
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

        self.le_lowerb = QLineEdit(self.groupBox)
        self.le_lowerb.setObjectName(u"le_lowerb")

        self.verticalLayout.addWidget(self.le_lowerb)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.le_upperb = QLineEdit(self.groupBox)
        self.le_upperb.setObjectName(u"le_upperb")

        self.verticalLayout.addWidget(self.le_upperb)

        self.btn_arg_ok = QPushButton(self.groupBox)
        self.btn_arg_ok.setObjectName(u"btn_arg_ok")

        self.verticalLayout.addWidget(self.btn_arg_ok)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout_2.addWidget(self.groupBox)

        self.horizontalLayout_2.setStretch(0, 4)
        self.horizontalLayout_2.setStretch(1, 1)
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
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"\u53c2\u6570\u586b\u5199", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u4e0b\u9650\uff1a", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u4e0a\u9650\uff1a", None))
        self.btn_arg_ok.setText(QCoreApplication.translate("Form", u"\u786e\u5b9a", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.function_explain), QCoreApplication.translate("Form", u"\u51fd\u6570\u8bf4\u660e", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.show_result), QCoreApplication.translate("Form", u"\u51fd\u6570\u6548\u679c", None))
    # retranslateUi

