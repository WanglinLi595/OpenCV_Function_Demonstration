#!/usr/bin/env python
# coding=utf-8
'''
@描述: cv.warpAffine() 效果演示
@版本: V1_0
@作者: LiWanglin
@创建时间: 2020.02.16
@最后编辑人: LiWanglin
@最后编辑时间: 2020.02.17
'''

from PySide2.QtWidgets import QWidget, QHBoxLayout, QTableView, QVBoxLayout
from PySide2.QtCore import Slot
from opencv_function import gui_function_warpaffine
from tools import modify_graphics, show_image_data
import numpy as np
import cv2

class WarpAffine(QWidget):
    '''cv.warpAffine() 函数演示类

    @方法说明: 
        # TODO

    @属性说明: 
        # TODO
    '''

    def __init__(self, parent=None, input_image=None):
        super().__init__(parent)
        self.ui = gui_function_warpaffine.Ui_Form()
        self.ui.setupUi(self)

        self._input_image = input_image

        self.input_image_h, self.input_image_w = input_image.shape

        self._init_widget_and_widget()
        self._init_slot_connect()

        self.original_graphics.scanf_image_data(input_image)
        self.original_graphics.dispaly_image()

        table_view = show_image_data.TableView(self.original_table_view, self.input_image_h,
                            self.input_image_w)
        table_view.add_init_data(self._input_image)

    def _init_widget_and_widget(self):
        '''初始化窗口布局

        @参数说明: 
            无

        @返回值: 
            无

        @注意: 
            无
        '''
        self.original_table_view = QTableView()
        self.result_table_view = QTableView()

        self.original_graphics = modify_graphics.ModifyQGraphicsView()
        self.result_graphics = modify_graphics.ModifyQGraphicsView()


        self.ui.horizontal_layout = QHBoxLayout(self.ui.show_result)
        self.ui.vertical_layout_1 = QVBoxLayout()
        self.ui.vertical_layout_2 = QVBoxLayout()

        self.ui.vertical_layout_1.addWidget(self.original_graphics)
        self.ui.vertical_layout_1.addWidget(self.original_table_view)
        self.ui.vertical_layout_1.setStretch(0,2)
        self.ui.vertical_layout_1.setStretch(1,1)

        self.ui.vertical_layout_2.addWidget(self.result_graphics)
        self.ui.vertical_layout_2.addWidget(self.result_table_view)
        self.ui.vertical_layout_2.setStretch(0,2)
        self.ui.vertical_layout_2.setStretch(1,1)

        self.ui.horizontal_layout.addLayout(self.ui.vertical_layout_1)
        self.ui.horizontal_layout.addLayout(self.ui.vertical_layout_2)

 
    def _init_slot_connect(self):
        '''初始化槽函数连接

        @参数说明: 
            无

        @返回值: 
            无

        @注意: 
            无
        '''  
        self.ui.btn_arg_ok.clicked.connect(self.execution_function) 

    @Slot()
    def execution_function(self):
        '''执行 cv.warpAffine() 函数并显示结果

        @参数说明: 
            无

        @返回值: 
            无

        @注意: 
            无
        '''
        # 从 LineEdit 获得参数，创建矩阵 M
        M = np.float32([[eval(self.ui.le_arg_1.text()), eval(self.ui.le_arg_2.text()), eval(self.ui.le_arg_3.text())],
                        [eval(self.ui.le_arg_4.text()), eval(self.ui.le_arg_5.text()), eval(self.ui.le_arg_6.text())]])
        
        # 执行 cv2.warpAffine() 函数
        result_image_data = cv2.warpAffine(self._input_image, M, (self.input_image_h, self.input_image_w))
        
        # 在 self.result_graphics 显示图片
        self.result_graphics.scanf_image_data(result_image_data)
        self.result_graphics.dispaly_image()

        # 在 self.result_table_view 显示图片数据
        
        table_view = show_image_data.TableView(self.result_table_view, self.input_image_h,
                            self.input_image_w)
        start = cv2.getTickCount()
        table_view.add_init_data(result_image_data)
        end = cv2.getTickCount()
        time = (end - start) / cv2.getTickFrequency()
        print("经历的时间为：", time)



