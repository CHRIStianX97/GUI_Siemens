# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Vue3_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Prodinfo(object):
    def setupUi(self, Prodinfo):
        Prodinfo.setObjectName("Prodinfo")
        Prodinfo.resize(531, 570)
        Prodinfo.setStyleSheet("QWidget#Prodinfo{\n"
"background-image:url(C:/Users/Christian/Desktop/素材/logo);\n"
"background-repeat:no-repeat;\n"
"back\n"
"}")
        self.label = QtWidgets.QLabel(Prodinfo)
        self.label.setGeometry(QtCore.QRect(40, 140, 91, 41))
        self.label.setStyleSheet("color:rgb(0, 139, 149)")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Prodinfo)
        self.label_2.setGeometry(QtCore.QRect(40, 200, 91, 41))
        self.label_2.setStyleSheet("color:rgb(0, 139, 149)")
        self.label_2.setObjectName("label_2")
        self.ProductName = QtWidgets.QLineEdit(Prodinfo)
        self.ProductName.setEnabled(True)
        self.ProductName.setGeometry(QtCore.QRect(150, 140, 291, 31))
        self.ProductName.setStyleSheet("border: 2px solid grey")
        self.ProductName.setReadOnly(False)
        self.ProductName.setObjectName("ProductName")
        self.OPSsteps = QtWidgets.QLineEdit(Prodinfo)
        self.OPSsteps.setEnabled(True)
        self.OPSsteps.setGeometry(QtCore.QRect(150, 200, 291, 31))
        self.OPSsteps.setStyleSheet("border: 2px solid grey")
        self.OPSsteps.setReadOnly(False)
        self.OPSsteps.setObjectName("OPSsteps")
        self.confirmBtn = QtWidgets.QPushButton(Prodinfo)
        self.confirmBtn.setGeometry(QtCore.QRect(350, 470, 81, 31))
        self.confirmBtn.setStyleSheet("")
        self.confirmBtn.setObjectName("confirmBtn")
        self.label_3 = QtWidgets.QLabel(Prodinfo)
        self.label_3.setGeometry(QtCore.QRect(40, 260, 81, 31))
        self.label_3.setStyleSheet("color:rgb(0, 139, 149)")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Prodinfo)
        self.label_4.setGeometry(QtCore.QRect(40, 320, 101, 31))
        self.label_4.setStyleSheet("color:rgb(0, 139, 149)")
        self.label_4.setObjectName("label_4")
        self.Operator = QtWidgets.QLineEdit(Prodinfo)
        self.Operator.setGeometry(QtCore.QRect(150, 320, 291, 31))
        self.Operator.setStyleSheet("border: 2px solid grey")
        self.Operator.setObjectName("Operator")
        self.SAP = QtWidgets.QLineEdit(Prodinfo)
        self.SAP.setGeometry(QtCore.QRect(150, 260, 291, 31))
        self.SAP.setStyleSheet("border: 2px solid grey")
        self.SAP.setObjectName("SAP")
        self.label_5 = QtWidgets.QLabel(Prodinfo)
        self.label_5.setGeometry(QtCore.QRect(40, 90, 51, 16))
        self.label_5.setStyleSheet("color:rgb(0, 139, 149)")
        self.label_5.setObjectName("label_5")
        self.com_num = QtWidgets.QLineEdit(Prodinfo)
        self.com_num.setGeometry(QtCore.QRect(150, 80, 291, 31))
        self.com_num.setStyleSheet("border: 2px solid grey")
        self.com_num.setObjectName("com_num")
        self.back2Btn = QtWidgets.QPushButton(Prodinfo)
        self.back2Btn.setGeometry(QtCore.QRect(140, 470, 81, 31))
        self.back2Btn.setStyleSheet("")
        self.back2Btn.setObjectName("back2Btn")

        self.retranslateUi(Prodinfo)
        QtCore.QMetaObject.connectSlotsByName(Prodinfo)
        Prodinfo.setTabOrder(self.com_num, self.ProductName)
        Prodinfo.setTabOrder(self.ProductName, self.OPSsteps)
        Prodinfo.setTabOrder(self.OPSsteps, self.SAP)
        Prodinfo.setTabOrder(self.SAP, self.Operator)
        Prodinfo.setTabOrder(self.Operator, self.confirmBtn)

    def retranslateUi(self, Prodinfo):
        _translate = QtCore.QCoreApplication.translate
        Prodinfo.setWindowTitle(_translate("Prodinfo", "Form"))
        self.label.setText(_translate("Prodinfo", "订单ID："))
        self.label_2.setText(_translate("Prodinfo", "产品数量："))
        self.confirmBtn.setText(_translate("Prodinfo", "确认"))
        self.label_3.setText(_translate("Prodinfo", "SAP No："))
        self.label_4.setText(_translate("Prodinfo", "操作员："))
        self.label_5.setText(_translate("Prodinfo", "串口端："))
        self.back2Btn.setText(_translate("Prodinfo", "上一步"))