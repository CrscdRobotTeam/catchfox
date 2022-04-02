#!/user/bin/env python3
# -*- coding: utf-8 -*-
import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import QSize,Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


ICON_WIDTH = 50
ICON_HEIGHT = 30
LEFTWIDGET_HEIGHT = 60
BUTTON_HEIGHT = 54
BUTTON_WIDTH = 54

'''切换栏'''


class LeftWidget(QWidget):
    def __init__(self, parent=None):
        super(LeftWidget, self).__init__(parent)

        # self.setWindowFlags(Qt.FramelessWindowHint)
        # 垂直布局按照从上到下的顺序进行添加按钮部件。

        mainLayout = QVBoxLayout()
        self.m_pButtonHome = QToolButton(self)
        self.m_pButtonHosiery = QToolButton(self)

        self.m_pButtonHome.setText('首页')
        self.m_pButtonHome.setIcon(QIcon('fox.png'))
        # 图片下显示首页
        self.m_pButtonHome.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.m_pButtonHome.setIconSize(QSize(ICON_WIDTH, ICON_HEIGHT))
        self.m_pButtonHome.setFixedWidth(BUTTON_WIDTH)
        self.m_pButtonHome.setFixedHeight(BUTTON_HEIGHT)

        self.m_pButtonHosiery.setText('历史')
        self.m_pButtonHosiery.setIcon(QIcon('fox.png'))
        # 图片下显示历史
        self.m_pButtonHosiery.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.m_pButtonHosiery.setIconSize(QSize(ICON_WIDTH, ICON_HEIGHT))
        self.m_pButtonHosiery.setFixedWidth(BUTTON_WIDTH)
        self.m_pButtonHosiery.setFixedHeight(BUTTON_HEIGHT)

        mainLayout.addWidget(self.m_pButtonHome)
        mainLayout.addWidget(self.m_pButtonHosiery)

        # 事件
        self.m_pButtonHome.clicked.connect(self.onHomeClick)
        self.m_pButtonHosiery.clicked.connect(self.onHosieryClick)

        # 设置主窗口
        self.setLayout(mainLayout)

        # 设置间距
        mainLayout.setSpacing(0)

        # 主窗口居中
        self.resize(150, 200)

    def onHomeClick(self):
        print('主界面点击')

    def onHosieryClick(self):
        print('历史记录点击')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = LeftWidget()
    w.show()
    sys.exit(app.exec_())

