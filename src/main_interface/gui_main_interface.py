# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_interface.ui'
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


class Ui_main_interface(object):
    def setupUi(self, main_interface):
        if main_interface.objectName():
            main_interface.setObjectName(u"main_interface")
        main_interface.resize(1228, 834)
        self.act_load_image = QAction(main_interface)
        self.act_load_image.setObjectName(u"act_load_image")
        self.act_exit = QAction(main_interface)
        self.act_exit.setObjectName(u"act_exit")
        self.centralwidget = QWidget(main_interface)
        self.centralwidget.setObjectName(u"centralwidget")
        self.table_view = QTableView(self.centralwidget)
        self.table_view.setObjectName(u"table_view")
        self.table_view.setGeometry(QRect(140, 20, 256, 192))
        self.tree_widget = QTreeWidget(self.centralwidget)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1");
        self.tree_widget.setHeaderItem(__qtreewidgetitem)
        self.tree_widget.setObjectName(u"tree_widget")
        self.tree_widget.setGeometry(QRect(618, 11, 256, 192))
        main_interface.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(main_interface)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1228, 26))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu_2 = QMenu(self.menubar)
        self.menu_2.setObjectName(u"menu_2")
        main_interface.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(main_interface)
        self.statusbar.setObjectName(u"statusbar")
        main_interface.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menu.addAction(self.act_load_image)
        self.menu.addAction(self.act_exit)

        self.retranslateUi(main_interface)

        QMetaObject.connectSlotsByName(main_interface)
    # setupUi

    def retranslateUi(self, main_interface):
        main_interface.setWindowTitle(QCoreApplication.translate("main_interface", u"MainWindow", None))
        self.act_load_image.setText(QCoreApplication.translate("main_interface", u"\u8f7d\u5165\u56fe\u7247", None))
        self.act_exit.setText(QCoreApplication.translate("main_interface", u"\u9000\u51fa", None))
#if QT_CONFIG(tooltip)
        self.act_exit.setToolTip(QCoreApplication.translate("main_interface", u"\u9000\u51fa\u7a0b\u5e8f", None))
#endif // QT_CONFIG(tooltip)
        self.menu.setTitle(QCoreApplication.translate("main_interface", u"\u6587\u4ef6", None))
        self.menu_2.setTitle(QCoreApplication.translate("main_interface", u"\u5173\u4e8e", None))
    # retranslateUi

