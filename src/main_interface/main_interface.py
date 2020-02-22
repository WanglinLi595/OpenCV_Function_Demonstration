#!/usr/bin/env python
# coding=utf-8
'''
@描述: 函数的主界面
@版本: V1_0
@作者: LiWanglin
@创建时间: 2020.02.15
@最后编辑人: LiWanglin
@最后编辑时间: 2020.02.22
'''

import cv2
from PySide2.QtWidgets import QMainWindow, QFileDialog, QHBoxLayout
from main_interface import gui_main_interface
from PySide2.QtCore import QCoreApplication, Slot, Qt
from tools import add_tree_item, show_image_data, modify_graphics, widget_set
from opencv_function import function_warpaffine, function_cvtcolor, function_inrange, function_resize

class MainInterface(QMainWindow):
    '''主界面类，用来组织所有的功能
        
    @属性说明: 
    # TODO

    @方法说明: 
    # TODO
    '''    

    _translate = QCoreApplication.translate         # 起代替作用

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = gui_main_interface.Ui_main_interface()
        self.ui.setupUi(self)
        self.class_name = self.__class__.__name__       # 获取类名

        self._graphics_view = modify_graphics.ModifyQGraphicsView()

        self.__init_layout()
        self.__init_tree_widget()
        self._init_slot_connect()

    def __init_layout(self):
        '''初始化布局

        @参数说明: 
            无
        @返回值: 
            无
        @注意: 
            无
        '''    
        self.ui.horizontalLayout = QHBoxLayout()

        self.ui.horizontalLayout.addWidget(self._graphics_view)
        self.ui.horizontalLayout.addWidget(self.ui.table_view)
        self.ui.horizontalLayout.addWidget(self.ui.tree_widget)

        self.ui.horizontalLayout.setStretch(0,4)
        self.ui.horizontalLayout.setStretch(1,4)
        self.ui.horizontalLayout.setStretch(2,1)
        
        self.ui.centralwidget.setLayout(self.ui.horizontalLayout)    

    def __init_tree_widget(self):
        '''初始化目录树

        @参数说明: 
            无

        @返回值: 
            无

        @注意: 
            无
        '''
        
        # 清空目录树
        self.ui.tree_widget.clear()             # 清空函数树

        # 设置目录树头标签
        text = self._translate("MainInterface", "函数")
        self.ui.tree_widget.setHeaderLabel(text)          # 设置目录树头标签

        # 添加顶层节点
        text = "OpenCV函数"
        self.tree_top_item = add_tree_item.add_tree_item(self.ui.tree_widget, add_tree_item.TreeItemType.top_item.value, 
                        self.class_name, text, tree_top=True)

        # 添加组节点
        text = "OpenCV图像处理"
        self.tree_group_item = add_tree_item.add_tree_item(self.tree_top_item, add_tree_item.TreeItemType.group_item.value, 
                        self.class_name, text)

        # 添加函数节点
        text = "cv.cvtColor()"
        self.get_start_with_image_item = add_tree_item.add_tree_item(self.tree_group_item, add_tree_item.TreeItemType.function_item.value, 
                        self.class_name, text)

        text = "cv.inRange()"
        self.get_start_with_image_item = add_tree_item.add_tree_item(self.tree_group_item, add_tree_item.TreeItemType.function_item.value, 
                        self.class_name, text)

        text = "cv.resize()"
        self.get_start_with_image_item = add_tree_item.add_tree_item(self.tree_group_item, add_tree_item.TreeItemType.function_item.value, 
                        self.class_name, text)


        text = "cv.warpAffine()"
        self.get_start_with_image_item = add_tree_item.add_tree_item(self.tree_group_item, add_tree_item.TreeItemType.function_item.value, 
                        self.class_name, text)


    def _init_slot_connect(self):
        '''初始化槽函数连接

        @参数说明: 
            无

        @返回值: 
            无

        @注意: 
            无
        ''' 
     
        self.ui.act_load_image.triggered.connect(self.load_image)
        self.ui.tree_widget.itemDoubleClicked.connect(self.function_opencv)
        self.ui.act_exit.triggered.connect(self.close)

    @Slot()
    def load_image(self):
        '''槽函数，获取图片信息，显示图片并显示图片数据

        @参数说明: 
            无

        @返回值: 
            无

        @注意: 
            无
        '''

        text1 = self._translate("MainInterface", "载入图片")
        text2 = self._translate("MainInterface", "图片文件(*.bmp *.jpg *.png)")
        # 获取文件的绝对路径
        self._file_name_dir = QFileDialog.getOpenFileName(self, text1, ".", text2)[0]
        # 获取图片数据
        self._original_image_data = cv2.imread(self._file_name_dir, cv2.IMREAD_UNCHANGED)
        # 获取图片的长和宽
        self._original_image_h, self._original_image_w = self._original_image_data.shape[:2]

        # 在 graphics_widget 里面显示图片
        self._graphics_view.scanf_image_data(self._original_image_data)
        self._graphics_view.dispaly_image()

        # 在 table_view 里面显示图片数据
        table_view = show_image_data.TableView(self.ui.table_view, self._original_image_h,
                            self._original_image_w)
        table_view.add_init_data(self._original_image_data)

    def function_opencv(self, current_item):
        '''槽函数，执行点击之后的函数

        @参数说明: 
            无

        @返回值: 
            无

        @注意: 
            无
        '''
        # 获取点击的选项的文字
        item_str = current_item.text(0)

        # 进行匹配，来执行不同的函数
        if item_str == "cv.cvtColor()":
            cvt_color = function_cvtcolor.CvtColor(parent=self, input_image=self._original_image_data)
            widget_set.widget_set(cvt_color, "cv.cvtColor()")       # 窗口初始化设置

        elif item_str == "cv.inRange()":
            in_range = function_inrange.InRange(parent=self, input_image=self._original_image_data)
            widget_set.widget_set(in_range , "cv.inRange()")


        elif item_str == "cv.warpAffine()":
            warp_affine = function_warpaffine.WarpAffine(parent=self, input_image=self._original_image_data)
            widget_set.widget_set(warp_affine, "cv.warpAffine()")
        
        elif item_str == "cv.resize()":
            resize = function_resize.Resize(parent=self, input_image=self._original_image_data)
            widget_set.widget_set(resize, "cv.resize()")
            