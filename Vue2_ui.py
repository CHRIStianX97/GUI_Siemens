# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Vue2_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_workpg(object):
    def setupUi(self, workpg):
        workpg.setObjectName("workpg")
        workpg.resize(879, 597)
        workpg.setStyleSheet("QMainWindow{\n"
"    color: blue\n"
"    }")
        self.centralwidget = QtWidgets.QWidget(workpg)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 80, 51, 31))
        self.label.setStyleSheet("")
        self.label.setObjectName("label")
        self.SAPID = QtWidgets.QLineEdit(self.centralwidget)
        self.SAPID.setEnabled(True)
        self.SAPID.setGeometry(QtCore.QRect(70, 80, 671, 31))
        self.SAPID.setStyleSheet("border: 2px solid grey")
        self.SAPID.setObjectName("SAPID")
        self.searchBtn = QtWidgets.QPushButton(self.centralwidget)
        self.searchBtn.setGeometry(QtCore.QRect(760, 80, 91, 31))
        self.searchBtn.setStyleSheet("")
        self.searchBtn.setObjectName("searchBtn")
        self.taskTable = QtWidgets.QTableWidget(self.centralwidget)
        self.taskTable.setEnabled(True)
        self.taskTable.setGeometry(QtCore.QRect(40, 140, 806, 351))
        self.taskTable.setMinimumSize(QtCore.QSize(806, 0))
        self.taskTable.setStyleSheet("border: 2px solid grey")
        self.taskTable.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.taskTable.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.taskTable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.taskTable.setRowCount(10)
        self.taskTable.setObjectName("taskTable")
        self.taskTable.setColumnCount(3)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.taskTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.taskTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.taskTable.setHorizontalHeaderItem(2, item)
        self.taskTable.horizontalHeader().setVisible(True)
        self.taskTable.horizontalHeader().setCascadingSectionResizes(True)
        self.taskTable.horizontalHeader().setDefaultSectionSize(273)
        self.taskTable.horizontalHeader().setHighlightSections(True)
        self.taskTable.horizontalHeader().setMinimumSectionSize(50)
        self.taskTable.verticalHeader().setVisible(False)
        self.nextbtn = QtWidgets.QPushButton(self.centralwidget)
        self.nextbtn.setGeometry(QtCore.QRect(470, 510, 101, 61))
        self.nextbtn.setBaseSize(QtCore.QSize(10, 10))
        self.nextbtn.setStyleSheet("\n"
"")
        self.nextbtn.setIconSize(QtCore.QSize(10, 10))
        self.nextbtn.setAutoDefault(False)
        self.nextbtn.setObjectName("nextbtn")
        self.back1Btn = QtWidgets.QPushButton(self.centralwidget)
        self.back1Btn.setGeometry(QtCore.QRect(240, 510, 101, 61))
        self.back1Btn.setBaseSize(QtCore.QSize(10, 10))
        self.back1Btn.setStyleSheet("")
        self.back1Btn.setIconSize(QtCore.QSize(10, 10))
        self.back1Btn.setAutoDefault(False)
        self.back1Btn.setObjectName("back1Btn")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 311, 71))
        self.widget.setStyleSheet("QWidget{\n"
"background-image:url(C:/Users/Christian/Desktop/素材/logo);\n"
"background-repeat:no-repeat;\n"
"back\n"
"}")
        self.widget.setObjectName("widget")
        workpg.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(workpg)
        self.statusbar.setObjectName("statusbar")
        workpg.setStatusBar(self.statusbar)

        self.retranslateUi(workpg)
        QtCore.QMetaObject.connectSlotsByName(workpg)

    def retranslateUi(self, workpg):
        _translate = QtCore.QCoreApplication.translate
        workpg.setWindowTitle(_translate("workpg", "MainWindow"))
        self.label.setText(_translate("workpg", "SAPNo："))
        self.searchBtn.setText(_translate("workpg", "搜索"))
        self.taskTable.setSortingEnabled(True)
        item = self.taskTable.horizontalHeaderItem(0)
        item.setText(_translate("workpg", "SAP号"))
        item = self.taskTable.horizontalHeaderItem(1)
        item.setText(_translate("workpg", "产品描述"))
        item = self.taskTable.horizontalHeaderItem(2)
        item.setText(_translate("workpg", "测试步骤"))
        self.nextbtn.setText(_translate("workpg", "下一步"))
        self.back1Btn.setText(_translate("workpg", "上一步"))
