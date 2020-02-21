# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'function_resize.ui'
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
        Form.resize(1160, 829)
        self.horizontalLayout_4 = QHBoxLayout(Form)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.tabWidget = QTabWidget(Form)
        self.tabWidget.setObjectName(u"tabWidget")
        self.explain_function = QWidget()
        self.explain_function.setObjectName(u"explain_function")
        self.horizontalLayout_5 = QHBoxLayout(self.explain_function)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.textBrowser = QTextBrowser(self.explain_function)
        self.textBrowser.setObjectName(u"textBrowser")

        self.horizontalLayout_5.addWidget(self.textBrowser)

        self.groupBox = QGroupBox(self.explain_function)
        self.groupBox.setObjectName(u"groupBox")
        self.btn_arg_ok = QPushButton(self.groupBox)
        self.btn_arg_ok.setObjectName(u"btn_arg_ok")
        self.btn_arg_ok.setGeometry(QRect(12, 123, 93, 28))
        self.widget = QWidget(self.groupBox)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(12, 27, 204, 26))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.le_fx = QLineEdit(self.widget)
        self.le_fx.setObjectName(u"le_fx")

        self.horizontalLayout.addWidget(self.le_fx)

        self.widget1 = QWidget(self.groupBox)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(12, 60, 204, 26))
        self.horizontalLayout_2 = QHBoxLayout(self.widget1)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.widget1)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.le_fy = QLineEdit(self.widget1)
        self.le_fy.setObjectName(u"le_fy")

        self.horizontalLayout_2.addWidget(self.le_fy)

        self.widget2 = QWidget(self.groupBox)
        self.widget2.setObjectName(u"widget2")
        self.widget2.setGeometry(QRect(12, 93, 216, 23))
        self.horizontalLayout_3 = QHBoxLayout(self.widget2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.widget2)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.cbb_interpolation = QComboBox(self.widget2)
        self.cbb_interpolation.addItem("")
        self.cbb_interpolation.addItem("")
        self.cbb_interpolation.setObjectName(u"cbb_interpolation")

        self.horizontalLayout_3.addWidget(self.cbb_interpolation)


        self.horizontalLayout_5.addWidget(self.groupBox)

        self.tabWidget.addTab(self.explain_function, "")
        self.show_result = QWidget()
        self.show_result.setObjectName(u"show_result")
        self.tabWidget.addTab(self.show_result, "")

        self.horizontalLayout_4.addWidget(self.tabWidget)


        self.retranslateUi(Form)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"\u53c2\u6570\u586b\u5199", None))
        self.btn_arg_ok.setText(QCoreApplication.translate("Form", u"\u786e\u5b9a", None))
        self.label.setText(QCoreApplication.translate("Form", u"fx:", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"fy:", None))
        self.label_3.setText(QCoreApplication.translate("Form", u" interpolation:", None))
        self.cbb_interpolation.setItemText(0, QCoreApplication.translate("Form", u"cv.INTER_NEAREST", None))
        self.cbb_interpolation.setItemText(1, QCoreApplication.translate("Form", u" cv.INTER_LINEAR", None))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.explain_function), QCoreApplication.translate("Form", u"\u51fd\u6570\u8bf4\u660e", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.show_result), QCoreApplication.translate("Form", u"\u51fd\u6570\u6548\u679c", None))
    # retranslateUi

