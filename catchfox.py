# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'catchfox.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(691, 196)
        self.onebt = QtWidgets.QPushButton(Form)
        self.onebt.setGeometry(QtCore.QRect(20, 70, 121, 91))
        self.onebt.setText("")
        self.onebt.setObjectName("onebt")
        self.twobt = QtWidgets.QPushButton(Form)
        self.twobt.setGeometry(QtCore.QRect(150, 70, 121, 91))
        self.twobt.setText("")
        self.twobt.setObjectName("twobt")
        self.threebt = QtWidgets.QPushButton(Form)
        self.threebt.setGeometry(QtCore.QRect(280, 70, 121, 91))
        self.threebt.setText("")
        self.threebt.setObjectName("threebt")
        self.fourbt = QtWidgets.QPushButton(Form)
        self.fourbt.setGeometry(QtCore.QRect(410, 70, 121, 91))
        self.fourbt.setText("")
        self.fourbt.setObjectName("fourbt")
        self.fivebt = QtWidgets.QPushButton(Form)
        self.fivebt.setGeometry(QtCore.QRect(540, 70, 121, 91))
        self.fivebt.setText("")
        self.fivebt.setObjectName("fivebt")
        self.remaindle = QtWidgets.QLineEdit(Form)
        self.remaindle.setGeometry(QtCore.QRect(20, 20, 121, 20))
        self.remaindle.setObjectName("remaindle")
        self.noticele = QtWidgets.QLineEdit(Form)
        self.noticele.setGeometry(QtCore.QRect(412, 20, 251, 20))
        self.noticele.setObjectName("noticele")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.remaindle.setText(_translate("Form", "剩余次数："))
        self.noticele.setText(_translate("Form", "恭喜抓到了狐狸！"))
