#!/usr/bin/env python
# coding=utf-8
'''
@描述: cv.inrange() 效果演示
@版本: V1_0
@作者: LiWanglin
@创建时间: 2020.02.19
@最后编辑人: LiWanglin
@最后编辑时间: 2020.02.19
'''

from PySide2.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QTableView
from tools import modify_graphics, show_image_data
from opencv_function import gui_function_inrange
import numpy as np
import cv2 as cv

class InRange(QWidget):
    '''cv.inrange() 函数演示类

    @方法说明: 
        # TODO

    @属性说明: 
        # TODO
    '''
    def __init__(self, parent=None, input_image=None):
        super().__init__(parent)
        self.ui = gui_function_inrange.Ui_Form()
        self.ui.setupUi(self)

        self._input_image = input_image
        self.input_image_h, self.input_image_w = self._input_image.shape[:2]

        self._init_widget_and_widget()
        self._init_slot_connect()

        # 显示图片
        self.original_graphics.scanf_image_data(input_image)
        self.original_graphics.dispaly_image()

        # 显示图片数据
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

    def execution_function(self):
        lower = np.array(eval(self.ui.le_lowerb.text()))
        upper = np.array(eval(self.ui.le_upperb.text()))

        result_image_data = cv.inRange(self._input_image, lower, upper)

        # 在 self.result_graphics 显示图片
        self.result_graphics.scanf_image_data(result_image_data)
        self.result_graphics.dispaly_image()

        # 在 self.result_table_view 显示图片数据
        
        table_view = show_image_data.TableView(self.result_table_view, self.input_image_h,
                            self.input_image_w)
        start = cv.getTickCount()
        table_view.add_init_data(result_image_data)
        end = cv.getTickCount()
        time = (end - start) / cv.getTickFrequency()
        print("经历的时间为：", time)
