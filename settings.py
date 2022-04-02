import json
import os
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import catchfox
import sys
import random


class MainWindow(QMainWindow, catchfox.Ui_Form):
    """主界面"""

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)  # 显示UI
        self.setFixedSize(self.width(), self.height())  # 禁用拖拽放大缩小

        self.press = 0
        self.maxStep = 10

        self.remaindle.setText("剩余次数%s" % self.maxStep)
        self.remaindle.setStyleSheet("background:transparent;border-width:0;border-style:outset")
        self.noticele.setStyleSheet("background:transparent;border-width:0;border-style:outset")
        self.onebt.clicked.connect(self.ClickOneBtn)
        self.twobt.clicked.connect(self.ClickTwoBtn)
        self.threebt.clicked.connect(self.ClickThreeBtn)
        self.fourbt.clicked.connect(self.ClickFourBtn)
        self.fivebt.clicked.connect(self.ClickFiveBtn)

        self.FoxInint()

    def ClickOneBtn(self):
        self.press = 1
        result = self.CatchFox()
        if result == 1:
            self.onebt.setStyleSheet("QPushButton{border-image: url(fox.png)}")
            self.noticele.setText("成功！抓到狐狸了！")
            self.remaindle.setText("剩余次数%s" % self.maxStep)
        else:
            self.remaindle.setText("剩余次数%s" % self.maxStep)

    def ClickTwoBtn(self):
        self.press = 2
        result = self.CatchFox()
        if result == 2:
            self.twobt.setStyleSheet("QPushButton{border-image: url(fox.png)}")
            self.noticele.setText("成功！抓到狐狸了！")
            self.remaindle.setText("剩余次数%s" % self.maxStep)
        else:
            self.remaindle.setText("剩余次数%s" % self.maxStep)

    def ClickThreeBtn(self):
        self.press = 3
        result = self.CatchFox()
        if result == 3:
            self.threebt.setStyleSheet("QPushButton{border-image: url(fox.png)}")
            self.noticele.setText("成功！抓到狐狸了！")
            self.remaindle.setText("剩余次数%s" % self.maxStep)
        else:
            self.remaindle.setText("剩余次数%s" % self.maxStep)

    def ClickFourBtn(self):
        self.press = 4
        result = self.CatchFox()
        if result == 4:
            self.fourbt.setStyleSheet("QPushButton{border-image: url(fox.png)}")
            self.noticele.setText("成功！抓到狐狸了！")
            self.remaindle.setText("剩余次数%s" % self.maxStep)
        else:
            self.remaindle.setText("剩余次数%s" % self.maxStep)

    def ClickFiveBtn(self):
        self.press = 5
        result = self.CatchFox()
        if result == 5:
            self.fivebt.setStyleSheet("QPushButton{border-image: url(fox.png)}")
            self.noticele.setText("成功！抓到狐狸了！")
            self.remaindle.setText("剩余次数%s" % self.maxStep)
        else:
            self.remaindle.setText("剩余次数%s" % self.maxStep)

    def FoxInint(self):
        self.positions = [0] * 5  # 共有n个洞口，设有狐狸的为1，没有的为0
        self.oldPos = random.randrange(0, 5)  # 狐狸的随机初始位置
        self.positions[self.oldPos] = 1

    def CatchFox(self):
        if self.positions[self.press] == 1:
            print("成功！抓到狐狸了！")
            self.noticele.setText("成功！抓到狐狸了！")
            self.onebt.setEnabled(False)
            self.twobt.setEnabled(False)
            self.threebt.setEnabled(False)
            self.fourbt.setEnabled(False)
            self.fivebt.setEnabled(False)
            return self.press

        if self.oldPos == 4:  # 在最右边
            self.newPos = self.oldPos - 1
        elif self.oldPos == 0:  # 在最左边
            self.newPos = self.oldPos + 1
        else:
            self.newPos = self.oldPos + random.choice((-1, 1))
        self.positions[self.oldPos], self.positions[self.newPos] = 0, 1

        if self.maxStep == 0:
            self.noticele.setText("您失败了，明天再来吧！")
            self.remaindle.setText("您的机会已经用完了，结束！")
            self.onebt.setEnabled(False)
            self.twobt.setEnabled(False)
            self.threebt.setEnabled(False)
            self.fourbt.setEnabled(False)
            self.fivebt.setEnabled(False)
        else:
            self.maxStep -= 1
        return self.oldPos

    # def CatchFox(self, n, maxStep):
    #     positions = [0] * n  # 共有n个洞口，设有狐狸的为1，没有的为0
    #     oldPos = random.randrange(0, n)  # 狐狸的随机初始位置
    #     positions[oldPos] = 1
    #     while maxStep > 0:  # 抓maxStep次
    #         maxStep -= 1
    #         x = int(input("今天打算打开哪个洞口？（0-{0}）:".format(n - 1)))
    #         if (x < 0) | (x > n):
    #             print("请输入正确的洞口")
    #             x = int(input("今天打算打开哪个洞口？（0-{0}）:".format(n - 1)))
    #         if positions[x] == 1:
    #             print("成功！抓到狐狸了！")
    #             self.press = x
    #             break
    #         else:
    #             print("今天没有抓到狐狸，明天来吧")
    #             self.remaindle.setText("剩余次数%s" % str(maxStep))
    #         if oldPos == n - 1:  # 在最右边
    #             newPos = oldPos - 1
    #         elif oldPos == 0:  # 在最左边
    #             newPos = oldPos + 1
    #         else:
    #             newPos = oldPos + random.choice((-1, 1))
    #         positions[oldPos], positions[newPos] = 0, 1
    #         oldPos = newPos
    #     else:
    #         print("还是没有抓到狐狸，您的机会已经用完了，结束。")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwd = MainWindow()  # 生成地图配置窗口实例
    mainwd.show()
    sys.exit(app.exec_())
