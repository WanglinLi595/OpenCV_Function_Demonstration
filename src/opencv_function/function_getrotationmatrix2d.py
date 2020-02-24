#!/usr/bin/env python
# coding=utf-8
'''
@描述: getRotationMatrix2D() 效果演示
@版本: V1_0
@作者: LiWanglin
@创建时间: 2020.02.23
@最后编辑人: LiWanglin
@最后编辑时间: 2020.02.24
'''

import cv2 as cv
from PySide2.QtWidgets import QWidget
from PySide2.QtCore import Slot
from opencv_function import gui_function_getrotationmatrix2d

class GetRotationMatrix2D(QWidget):
    '''

    @方法说明: 


    @属性说明: 

    '''

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = gui_function_getrotationmatrix2d.Ui_function_getRotationMatrix2D()
        self.ui.setupUi(self)
        self._init_slot_connect()

    def _init_slot_connect(self):
        '''初始化信号与槽的连接

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
        '''槽函数

        @参数说明: 


        @返回值: 


        @注意: 

        '''
        # 从控件中获取输入参数    
        center_x = eval(self.ui.le_x.text())
        center_y = eval(self.ui.le_y.text())

        angle = eval(self.ui.le_angle.text())
        scale = eval(self.ui.le_scale.text())

        # 执行 cv.getRotationMatrix2D() 函数
        matrix = cv.getRotationMatrix2D((center_x, center_y), angle, scale)

        # 输出结果
        matrix_str = str(matrix)
        self.ui.tb_result.setText(matrix_str)



