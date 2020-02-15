#!/usr/bin/env python
# coding=utf-8
'''
@描述: 用来添加目录树
@版本: V1_0
@作者: LiWanglin
@创建时间: 2020.02.15
@最后编辑人: LiWanglin
@最后编辑时间: 2020.02.15
'''

from PySide2.QtWidgets import QTreeWidgetItem
from PySide2.QtCore import QCoreApplication
from enum import Enum

class TreeItemType(Enum):
    """节点类型枚举

    定义节点类型枚举，为了便于后面的目录树的修改

    @属性说明：
        top_item: 顶层节点
        group_item: 组节点
        function_item：函数节点

    @方法说明：
        无
    """
    top_item = 1001             # 顶层节点
    group_item = 1002           # 组节点
    function_item = 1003        # 函数节点


def add_tree_item(item_parent, tree_value, tree_class_text, tree_text, tree_col_num=0, tree_top=False):
    '''在目录树上添加节点

    在目录树上添加节点

    @参数说明: 
        item_parent：此节点的父节点
        tree_value：节点相对应的值
        tree_class_text：
        tree_text：设置节点文字
        tree_col_num：节点的行号
        tree_top：是否为首节点

    @返回值: 
        tree_item：返回此节点

    @注意: 
        无
    '''
    tree_item = QTreeWidgetItem(tree_value)     # 创建 QTreeWidgetItem 类
    text = QCoreApplication.translate(tree_class_text, tree_text)
    tree_item.setText(tree_col_num, text)        # 设置节点文字
    # 首节点判定
    if(tree_top==False):
        item_parent.addChild(tree_item)
    else:
        item_parent.addTopLevelItem(tree_item)
    return tree_item
