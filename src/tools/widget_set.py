#!/usr/bin/env python
# coding=utf-8
'''
@描述: 创建窗口设置
@版本: V1_0
@作者: LiWanglin
@创建时间: 2020.02.19
@最后编辑人: LiWanglin
@最后编辑时间: 2020.02.19
'''

from PySide2.QtCore import Qt

def widget_set(widget, widget_name=""):
    widget.setAttribute(Qt.WA_DeleteOnClose)             # 窗口关闭时自动删除
    # setWindowFlag()用于设置窗口标志，，参数Qt.Window表明这是一个窗口，通常
    # 具有窗口的边框，标题栏，而不管他是否有父窗口
    widget.setWindowFlag(Qt.Window, True)
    # 设置窗口透明度，取值0-1， 1表示完全不透明， 0表示完全透明
    widget.setWindowOpacity(1)
    # setWindowModality()用于设置窗口的模态形式，参数Qt.ApplicationModal
    # 阻止所有窗口的输入
    widget.setWindowModality(Qt.ApplicationModal)
    # 设置窗口标题栏
    widget.setWindowTitle(widget_name)
    # 显示窗口
    widget.show()
