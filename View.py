import sys
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from Vue1_ui import *
from Vue2_ui import *
from Vue3_ui import *
from Vue4_ui import *
from Vue5_ui import *


# from Contrl import Controller

class Vue1(QMainWindow, Ui_Login_state):
    Signal_Vue1 = pyqtSignal(str, str)

    def __init__(self):
        super(Vue1, self).__init__()
        self.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint | QtCore.Qt.WindowCloseButtonHint)
        #self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setupUi(self)
        self.pwdtxt.setEchoMode(QLineEdit.Password)
        self.setFocusPolicy(QtCore.Qt.StrongFocus)
        # 把按键连接起来
        self.login.clicked.connect(self.vue1_signal_emit)
        # self.ctrl = Controller()
        # self.Signal_Vue1.connect(self.ctrl.p)

    def vue1_signal_emit(self):
        self.Signal_Vue1.emit(self.account.text(), self.pwdtxt.text())
        # self.close()

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Enter or event.key() == QtCore.Qt.Key_Return:
            self.vue1_signal_emit()


class Vue2(QMainWindow, Ui_workpg):
    Signal_Vue2_search = pyqtSignal(str)
    Signal_Vue2_next = pyqtSignal()
    Signal_Vue2_back = pyqtSignal()

    def __init__(self):
        super(Vue2, self).__init__()
        self.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint | QtCore.Qt.WindowCloseButtonHint)
        self.setupUi(self)
        self.taskTable.setStyleSheet("background:  rgb(230, 230, 230)")
        self.nextbtn.setEnabled(False)
        self.searchBtn.clicked.connect(self.vue2_signal_emit)
        self.nextbtn.clicked.connect(self.vue2_signal_next_emit)
        self.back1Btn.clicked.connect(self.vue2_signal_back_emit)
        self.flag_searched = False
        #self.nextbtn.installEventFilter(self)

    def vue2_signal_emit(self):
        self.Signal_Vue2_search.emit(self.SAPID.text())

    def vue2_signal_next_emit(self):
        self.Signal_Vue2_next.emit()

    def vue2_signal_back_emit(self):
        self.Signal_Vue2_back.emit()

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Enter or event.key() == QtCore.Qt.Key_Return:
            if self.flag_searched == False:
                self.vue2_signal_emit()
            else:
                self.vue2_signal_next_emit()


    # def eventFilter(self, obj, event):
    #     if obj == self.searchBtn:
    #         if event.type() == QEvent.KeyPress:
    #             keyEvent = QKeyEvent(event)
    #             if keyEvent.key() == QtCore.Qt.Key_Enter or keyEvent.key() == QtCore.Qt.Key_Return:
    #                 self.vue2_signal_search_emit()
    #                 return True
    #     return False


class Vue3(QMainWindow, Ui_Prodinfo):
    Signal_Vue3_confirm = pyqtSignal(str, str, str, str, str)
    Signal_Vue3_back = pyqtSignal()

    def __init__(self):
        super(Vue3, self).__init__()
        self.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint | QtCore.Qt.WindowCloseButtonHint)
        self.setupUi(self)
        self.com_num.setEnabled(False)
        self.SAP.setEnabled(False)
        self.confirmBtn.clicked.connect(self.vue3_signal_emit)
        self.back2Btn.clicked.connect(self.vue3_signal_back_emit)

    def vue3_signal_emit(self):
        self.Signal_Vue3_confirm.emit(self.SAP.text(), self.ProductName.text(), self.OPSsteps.text(),
                                      self.Operator.text(), self.com_num.text())

    def vue3_signal_back_emit(self):
        self.Signal_Vue3_back.emit()

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Enter or event.key() == QtCore.Qt.Key_Return:
            self.vue3_signal_emit()


class Vue4(QMainWindow, Ui_MainWindow):
    Signal_vue4_start = pyqtSignal()
    Signal_vue4_reset = pyqtSignal()
    Signal_vue4_back = pyqtSignal()

    def __init__(self):
        super(Vue4, self).__init__()
        self.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint | QtCore.Qt.WindowCloseButtonHint)
        self.setupUi(self)
        self.startBtn.clicked.connect(self.vue4_signal_start_emit)
        self.resetBtn.clicked.connect(self.vue4_signal_reset_emit)
        self.back3Btn.clicked.connect(self.vue4_signal_back_emit)

    def vue4_signal_start_emit(self):
        self.Signal_vue4_start.emit()

    def vue4_signal_reset_emit(self):
        self.Signal_vue4_reset.emit()

    def vue4_signal_back_emit(self):
        self.Signal_vue4_back.emit()

    def keyPressEvent(self, event):
        if (event.key() == QtCore.Qt.Key_Enter or event.key() == QtCore.Qt.Key_Return) and self.startBtn.isEnabled():
            self.vue4_signal_start_emit()

class Vue5(QMainWindow, Ui_newProdInfo):
    Signal_Vue5_confirm = pyqtSignal(str)

    def __init__(self):
        super(Vue5, self).__init__()
        self.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint | QtCore.Qt.WindowCloseButtonHint)
        self.setupUi(self)
        self.seriesNum.setFocus()
        self.confirmBtn.clicked.connect(self.vue5_signal_emit)

    def vue5_signal_emit(self):
        self.Signal_Vue5_confirm.emit(self.seriesNum.text())

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Enter or event.key() == QtCore.Qt.Key_Return:
            self.vue5_signal_emit()




# if __name__ == "__main__":
#     App = QApplication(sys.argv)
#     first_layerForm = Vue1()
#     first_layerForm.show()
#
#     sys.exit(App.exec_())
