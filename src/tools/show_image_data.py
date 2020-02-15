#!/usr/bin/env python
# coding=utf-8
'''
@描述: 在 table widget 显示图片数据
@版本: V1_0
@作者: LiWanglin
@创建时间: 2020.02.15
@最后编辑人: LiWanglin
@最后编辑时间: 2020.02.15
'''

from PySide2.QtWidgets import QAbstractItemView, QHeaderView
from PySide2.QtGui import QStandardItemModel, QStandardItem
from PySide2.QtCore import Qt, QItemSelectionModel

class TableView():
    # 设置tab_view的行数列数
    def __init__(self, table_view, table_col, table_row):
        self.table_view = table_view
        self.table_col = table_col
        self.table_row = table_row

        self.item_model = QStandardItemModel(self.table_col, self.table_row, table_view)
        self.select_model = QItemSelectionModel(self.item_model)
        self.table_view.setModel(self.item_model)             #数据模型
        self.table_view.setSelectionModel(self.select_model)  # 选择模型
        one_more = QAbstractItemView.ExtendedSelection      # 选择模式
        self.table_view.setSelectionMode(one_more)       # 可多选
        item_or_row = QAbstractItemView.SelectItems         # 项选则模式
        self.table_view.setSelectionBehavior(item_or_row)    # 单元格选择
        self.table_view.setAlternatingRowColors(True)        # 设置交替行颜色
        # 根据数据调节单元格大小
        self.table_view.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
    
    def add_init_data(self, data):
        '''添加数据到 table_view

        @参数说明: 
            data ：要显示的数据

        @返回值: 
            无

        @注意: 
            无
        '''   
        self._data = data

        for i in range(self.table_col):
            for j in range(self.table_row): 
                temp_date = QStandardItem(str(self._data[i, j]))
                # 设置单元格居中
                temp_date.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                self.item_model.setItem(i, j, temp_date)    # 在单元格中添加数据

    def add_modify_date(self, data):
        '''添加修改后的数据

        @参数说明: 
            data ：要显示的数据

        @返回值: 
            无

        @注意: 
            无
        '''      
        for i in range(self.table_col):
            for j in range(self.table_row):   
                if data[i, j] is not self._data[i ,j]:
                    temp_date = QStandardItem(str(data[i, j]))
                    # 设置单元格居中
                    temp_date.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                    self.item_model.setItem(i, j, temp_date)    # 在单元格中添加数据
        self._data = data