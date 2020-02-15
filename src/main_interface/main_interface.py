#!/usr/bin/env python
# coding=utf-8
'''
@描述: 函数的主界面
@版本: V1_0
@作者: LiWanglin
@创建时间: 2020.02.15
@最后编辑人: LiWanglin
@最后编辑时间: 2020.02.15
'''


from PySide2.QtWidgets import QMainWindow, QFileDialog
from main_interface import  gui_main_interface
from PySide2.QtCore import QCoreApplication, pyqtSlot
from tools import add_tree_item, show_image_data, modify_graphics

class MainInterface(QMainWindow):

    _translate = QCoreApplication.translate         # 起代替作用

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = gui_main_interface.Ui_main_interface()
        self.ui.setupUi(self)
        self.class_name = self.__class__.__name__       # 获取类名
        self.__init_tree_widget()
        

    def __init_tree_widget(self):
        
         # 1. 清空目录树
        self.ui.tree_widget.clear()             # 清空函数树

        # 2. 设置目录树头标签
        text = self._translate("MainInterface", "函数")
        self.ui.tree_widget.setHeaderLabel(text)          # 设置目录树头标签

        # 3. 添加目录树节点
        # 添加顶层节点
        text = "OpenCV函数"
        self.tree_top_item = add_tree_item.add_tree_item(self.ui.tree_widget, add_tree_item.TreeItemType.top_item.value, 
                        self.class_name, text, tree_top=True)

        # 添加组节点
        text = "OpenCV图像处理"
        self.tree_group_item = add_tree_item.add_tree_item(self.tree_top_item, add_tree_item.TreeItemType.group_item.value, 
                        self.class_name, text)

        # 添加函数节点
        text = "图像处理"
        self.get_start_with_image_item = add_tree_item.add_tree_item(self.tree_group_item, add_tree_item.TreeItemType.function_item.value, 
                        self.class_name, text)

    def _init_slot_connect(self):
        '''初始化槽函数连接

        @参数说明: 

        @返回值: 

        @注意: 

        ''' 
        self.ui.act_load_image.triggered.connect(self.load_image)  
        self.ui.btn_roi_ok.clicked.connect(self.make_sure_roi)
        self.ui.tree_widget.itemDoubleClicked.connect(self.get_start_with_image)

    @pyqtSlot()
    def load_image(self):
        # 1. 获取图片数据
        text1 = self._translate("MainInterface", "载入图片")
        text2 = self._translate("MainInterface", "图片文件(*.bmp *.jpg *.png)")
        # 获取文件的绝对路径
        self._file_name_dir = QFileDialog.getOpenFileName(self, text1, ".", text2)[0]
        # 获取图片数据
        self._original_image_data = show_image_data.get_image_data(self._file_name_dir,
                                cv2.IMREAD_UNCHANGED)
        # 获取图片的长和宽
        self._original_image_h, self._original_image_w = self._original_image_data.shape[:2]

        # 2. 在 graphcis_view 里面显示图片
        self._graphcis_view.scanf_image_data(self._original_image_data)
        self._graphcis_view.dispaly_image()

        # 3. 在 table_view 里面显示图片数据
        table_view = display_image_data.TableView(self.ui.table_view, self._original_image_h,
                            self._original_image_w)
        table_view.add_init_data(self._original_image_data)
