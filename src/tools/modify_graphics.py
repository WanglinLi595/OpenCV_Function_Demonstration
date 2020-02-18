#!/usr/bin/env python
# coding=utf-8
'''
@描述: 显示图片
@版本: V1_0
@作者: LiWanglin
@创建时间: 2020.02.16
@最后编辑人: LiWanglin
@最后编辑时间: 2020.02.18
'''


import cv2

from PySide2.QtWidgets import QGraphicsPixmapItem, QGraphicsScene, QGraphicsView
from PySide2.QtGui import QImage, QPixmap
from PySide2.QtCore import QPoint, Qt, Signal


class ModifyQGraphicsView(QGraphicsView):
    """改进 QGraphicsView 类

    由于 QGraphicsView 类没有与 mouseMoveEvent() 相关的信号，因而无法定义槽函数于此事件关联。为此，
    从 QGraphicsView 类集成定义一个类 QGraphicsView 类，实现鼠标移动事件函数 mouseMoveEvent() 的处理，
    并把事件转换为自定义信号，这样就可以在程序里面设计槽函数响应这些鼠标事件。

    @属性说明：
        mouse_move：定义一个鼠标移动信号

    @方法说明：
        mouseMoveEvent()：鼠标移动事件

    """
    def __init__(self, parent=None, image_data = None):
        super().__init__(parent)

        self._image_data = image_data

        if self._image_data is not None:
            # 获取图片信息
            self._image_shape = len(self._image_data.shape)
            self._image_h, self._image_w = self._image_data.shape[:2]

        mouse_move = Signal(QPoint)     # 定义一个鼠标移动信号
        mouse_clicked = Signal(QPoint)  # 定义一个鼠标点击信号

    def mouseMoveEvent(self, event): 
        '''鼠标移动事件

        鼠标移动事件

        @参数说明: 
            point：当前鼠标所在的坐标点

        @返回值: 
            无

        @注意: 
            无
        '''  
        point = event.pos()          
        self.mouse_move.emit(point)    #发射信号
        super().mouseMoveEvent(event)

    def mousePressEvent(self, event):
        '''鼠标点击事件

        鼠标点击事件

        @参数说明: 
            point：当前鼠标所在的坐标点

        @返回值: 
            无

        @注意: 
            无
        '''  
        if(event.button() == Qt.LeftButton):
            point = event.pos()
            self.mouse_clicked.emit(point)      #发射信号     
        super().mousePressEvent(event)

    def scanf_image_data(self, image_data):
        ''' 获得图片数据，并获取图片属性

        @参数说明: 
            image_data ：图片数据

        @返回值: 
            无

        @注意: 
            无
        '''
        self._image_data = image_data

        # 获取图片信息
        self._image_shape = len(self._image_data.shape)
        self._image_h, self._image_w = self._image_data.shape[:2]

    def dispaly_image(self):
        '''在 ModifyQGraphicsView 显示一张图片

        在 ModifyQGraphicsView 显示一张图片       

        @参数说明: 
            无

        @返回值: 
            无

        @注意: 
            无
        '''

        # 根据图片的维度，进行不同的处理
        if self._image_shape is 2:
            # 如果是二维灰度图片，读取方式为QImage.Format_Grayscale8
            temp_q_image = QImage(self._image_data, self._image_h ,
                        self._image_w, QImage.Format_Grayscale8)
        elif self._image_shape is 3:
            # 由于QImage读取方式为RGB，但 opencv 读取图片形式为BGR，所以要进行色彩转换
            temp_q_image = cv2.cvtColor(self._image_data, cv2.COLOR_BGR2RGB)

            # 如果是三维灰度图片，读取方式为QImage.Format_RGB888
            temp_q_image = QImage(temp_q_image, self._image_h, self._image_w, 
                            QImage.Format_RGB888)
        else:
            return None
        
        # 2. 像素映射
        temp_q_image_pix = QPixmap.fromImage(temp_q_image)               # 将给定图像转换为像素映射

        # 3. 在graphics_view中显示图片
        temp_item = QGraphicsPixmapItem(temp_q_image_pix)
        temp_q_sece = QGraphicsScene()
        temp_q_sece.addItem(temp_item)  
        self.setScene(temp_q_sece)
        temp_q_sece.clearSelection()