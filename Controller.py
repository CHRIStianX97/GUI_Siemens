import ctypes
import inspect
import threading
from datetime import datetime
import time

import serial
import re
from PyQt5.Qt import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from Model import *
from View import Vue1, Vue2, Vue3, Vue4, Vue5


class Thread(QThread):
    Signal_one_step_result = pyqtSignal(bool)
    Signal_result = pyqtSignal(list, list)

    def __init__(self,data):
        super().__init__()
        self.dataSelected = data

    # def __del__(self):
    #     self.wait()

    def run(self):
        self.one_test()

    def one_test(self):
        #self.Vue4.startBtn.setEnabled(False)
        # ret, ser = port_open("/dev/ttyUSB0")
        # if not ret:
        #     raise ValueError("port打开失败")
        # # make sure it is single step
        # single_step(ser)
        # # Only test single step right now
        # start = time.time()
        # operating_flag = True
        # result_list = list()
        # step_list = list()
        # index = 0
        # for i in self.dataSelected:
        #     # 3000,5,0.5,2,HHLLL3000OO
        #     steps = i[-1]
        #     step = steps.split(",")
        #     # ACW_test(voltage, uplimit, downlimit,testtime,channel,ser)
        #     ACW_test(step[0], step[1], step[2], step[3], step[4], ser)
        #     ehi_cmd = "TEST\n"
        #     ret_val = ser.write(ehi_cmd.encode())
        #     time.sleep(0.1)
        #     time.sleep(step[2] + 2 + 2)  # The true time is test time + ERU + ERD
        #     if not ret_val:
        #         raise ValueError("EHI transmission failed")
        #     result = get_test_result(ser, dw_time=float(step[2] + 2 + 2))  # The true time is test time + ERU + ERD
        #     result_list.append(result)
        #     step_list.append(steps)
        #     result_list.append(";")
        #     step_list.append(";")
        #     if "PASS" not in result:
        #         self.Signal_one_step_result.emit(False)
        #         #operating_flag = False
        #         self.angui_test_status = 0
        #         self.Vue4.testing_data.setItem(index, 8, QTableWidgetItem("失败"))
        #         a = self.Vue4.testing_data.item(index, 8)
        #         a.setBackground(QBrush(QColor(255, 0, 0)))
        #     elif "PASS" in result:
        #         self.Signal_one_step_result.emit(True)
        #         self.angui_test_status = 1
        #         self.Vue4.testing_data.setItem(index, 8, QTableWidgetItem("通过"))
        #         a = self.Vue4.testing_data.item(index, 8)
        #         a.setBackground(QBrush(QColor(0, 255, 0)))
        #     index += 1
        #
        # self.steps_tested = index
        # self.elapsed = time.time() - start
        # self.Vue4.testUsedTime.setText(str(self.elapsed))
        # self.tested += 1
        # if operating_flag:
        #     self.passed += 1
        # else:
        #     self.failed += 1
        # self.store_result(result_list, step_list)
        # self.status_update(2)
        # # update the status bar
        # # self.figure_num(operating_flag)
        # # self.test_progress()
        # # update the number etc
        # self.update_progress()
        # update the other status
        time.sleep(2)
        self.Signal_one_step_result.emit(True)
        # self.Vue4.startBtn.setEnabled(True)
        # self.Vue5.show()

class Controller:
    signal_2_3 = pyqtSignal(list, str)
    signal_data_emit = pyqtSignal(list)

    def __init__(self):
        super(Controller, self).__init__()
        # self.init()
        self.SAPNo = ""
        self.prodID = ""
        self.prodNum = ""
        self.operator = ""
        self.com = "/dev/ttyUSB0"
        self.data = None
        #self.thread_test = Thread()
        self.Vue1 = Vue1()
        self.Vue2 = Vue2()
        self.Vue3 = Vue3()
        self.Vue4 = Vue4()
        self.Vue5 = Vue5()
        self.dataBase = Model(server="10.193.3.234", user="BSCE_TE_SCALE", pwd="Ss123456", db="BSCE_TE_SafetyTester")
        # self.signal.connect(self.Vue3.set_info_state)
        self.Vue1.Signal_Vue1.connect(self.get_userinfo)
        self.Vue2.Signal_Vue2_search.connect(self.search)
        self.Vue2.Signal_Vue2_next.connect(self.vue2to3)
        self.Vue2.Signal_Vue2_back.connect(self.vue2to1)
        self.Vue3.Signal_Vue3_confirm.connect(self.vue3to4)
        self.Vue3.Signal_Vue3_back.connect(self.vue3to2)
        self.Vue4.Signal_vue4_start.connect(self.start)
        self.Vue4.Signal_vue4_reset.connect(self.reset)
        self.Vue4.Signal_vue4_back.connect(self.vue4to3)
        self.Vue5.Signal_Vue5_confirm.connect(self.vue5to4)

        # self.thread_test.Signal_one_step_result.connect()
        # self.thread_test.Signal_result.connect()

    # 拿到user的信息
    def get_userinfo(self, user, pwd):
        self.user = user
        self.pwd = pwd
        if len(self.pwd) != 0 and len(self.user) != 0:
            # self.checkinfo()
            self.Vue1.close()
            self.Vue2.show()

    # def keyPressEvent(self, event):
    #     #不知道为什么这个enter比qtcore里面的enter值少一
    #     #Windows下，Qt.Key_Return(字母键盘回车) + 1 == Qt.Key_Enter(数字小键盘回车)
    #     if event.key() == QtCore.Qt.Key_Enter or event.key() == QtCore.Qt.Key_Return:
    #         self.validation()

    # 判断是admin还是一般user
    # def checkinfo(self):
    #     try:
    #         f = open('/home/pi/BSCE_TE/SafetyTester/admin.txt','r')
    #     except:
    #         print(1)
    #         raise ValueError("The admin file does not exist")
    #
    #     admin = list()
    #     for x in f:
    #         x = x.rstrip("\n")
    #         splt = x.split(",")
    #         admin.append(splt[1])
    #
    #     self.admin = admin

    # if str(self.user) == admin[0] and str(self.pwd == admin[1]):
    #     #界面转为管理员模式
    #     self.adminpage()
    #
    # else:
    #     #界面转为操作员模式
    #    self.workerpage()

    # validate the info collected
    # def validation(self, user, pwd):
    #     # self.get_userinfo()
    #     self.Vue1.close()
    #     print(2)
    # if self.info_collected:
    #     self.checkinfo()
    # self.Vue1.close()

    # 操作员界面跳转
    # def workerpage(self):
    # 先关闭登录界面
    # self.Vue1.close()
    # self.workerpg = Vue2()
    # self.workerpg.show()

    # #admin界面跳转
    # def adminpage(self):
    #     self.Vue1.close()
    #     self.adminpg = adminApp()
    #     self.adminpg.show()

    # get SAPNo from operator and get all data with the SAPNo from database
    def get_sapno_information(self, SAPNo):
        info = list()
        # self.SAPno = int(self.SAPID.text())
        self.SAPNo = SAPNo
        # print(self.SAPNo)
        # sql = "SELECT * FROM dbo.Safety_TestItem ORDER by SAP_NUMBER"
        # self.data = self.dataBase.execute_sql(sql)
        # for i in self.data:
        #     # print(i[3])
        #     if str(i[3]) == self.SAPNo:
        #         info.append(i)
        # return info

    # 查询SAPnos,查询完毕之后要把SAPno和订单号那些传送到下一个界面
    def search(self, SAPNo):
        if len(SAPNo) != 0:
            self.Vue2.nextbtn.setEnabled(True)
            self.Vue2.flag_searched = True
            self.Vue2.nextbtn.setFocus()
            self.get_sapno_information(SAPNo)

            # self.dataSelected = self.get_sapno_information(SAPNo)
            # try:
            #     # only allows one sap number to be passed
            #     self.Vue2.taskTable.clearContents()
            #     # 拿到要搜索的SAP值
            #     self.info = self.get_sapno_information(SAPNo)
            #     if self.info:
            #         self.row = 0
            #         for i in range(0, len(self.info)):
            #             self.shuxing = self.info[i][6]
            #             self.value = self.info[i][10]
            #             self.Vue2.taskTable.setItem(self.row, 0, QTableWidgetItem(str(self.SAPNo)))
            #             self.Vue2.taskTable.setItem(self.row, 1, QTableWidgetItem(self.shuxing))
            #             self.Vue2.taskTable.setItem(self.row, 2, QTableWidgetItem(self.value))
            #             self.row += 1
            #         self.Vue2.nextbtn.setEnabled(True)
            #         self.Vue2.nextbtn.setFocus()
            #     else:
            #         #self.message_show()
            #         print("ERROR")
            # except:
            #     #self.message_show()
            #     print("ERROR")

    # message box
    # def message_show(self):
    #     self.messagebox = messageApp()
    #     self.messagebox.show()

    # Vue2 swiches to Vue3 with the translation of information
    def set_up_vue3(self):
        self.Vue3.ProductName.setText(self.prodID)
        self.Vue3.OPSsteps.setText(self.prodNum)
        self.Vue3.SAP.setText(str(self.SAPNo))
        self.Vue3.Operator.setText(self.operator)
        self.Vue3.com_num.setText(self.com)

    def vue2to3(self):
        self.Vue2.close()
        # self.signal_2_3.emit(self.data, self.SAPNo)
        self.set_up_vue3()
        self.Vue3.switch = True
        self.Vue3.show()

    def vue2to1(self):
        self.Vue2.close()
        # self.Vue1.swich = True
        self.Vue1.show()
        self.Vue1.account.selectAll()
        self.Vue1.account.setFocus()

    def set_up_vue4(self, SAPNo, ProductID, ProductNum, Operator, com):
        self.prodID = ProductID
        self.prodNum = ProductNum
        self.operator = Operator
        self.orderinfo()
        self.operatorinfo()
        self.current_time()

    def vue3to4(self, SAPNo, ProductID, ProductNum, Operator, com):
        if len(Operator) != 0:
            self.Vue3.close()
            self.set_up_vue4(SAPNo, ProductID, ProductNum, Operator, com)
            self.Vue4.show()


    def vue3to2(self):
        self.Vue3.close()
        self.Vue2.show()
        self.Vue2.SAPID.selectAll()
        self.Vue2.SAPID.setFocus()

    def vue4to3(self):
        self.Vue4.close()
        self.Vue3.show()
        self.Vue3.Operator.selectAll()
        self.Vue3.Operator.setFocus()

    def vue5to4(self, serialNum):
        self.serialNum = serialNum
        self.Vue4.IDnum.setText(self.serialNum)
        # self.signal_data_emit.emit(self.dataSelected)
        # self.thread = Thread()
        # self.thread_test = threading.Thread(target=self.AnGui_operate, args=(1,))
        # self.thread_test.setDaemon(True)
        # self.thread_test.start()
        # self.progress_bar()
        self.thread = Thread(None)
        #self.thread.Signal_one_step_result.connect(self.progress_change)
        self.thread.start()
        self.progress_bar()
        self.Vue5.close()
        self.Vue4.startBtn.setEnabled(False)
        # self.AnGui_operate()

    def progress_bar(self):
        self.timer = QTimer(self.Vue4.progressBar)
        self.Vue4.progressBar.setValue(0)
        self.Vue4.progressBar.setMaximum(100)
        self.timer.timeout.connect(self.progress_change)
        self.timer.start(1000)

    def progress_change(self):
        # while self.thread_test.is_alive():
        #     self.Vue4.progressBar.setValue(self.Vue4.progressBar.value() + 1)
        # self.Vue4.progressBar.setValue(100)
        # self.timer.stop()
        if  self.thread.isFinished():
           # self.Vue4.progressBar.setValue(100)
            self.timer.stop()
            self.Vue4.startBtn.setEnabled(True)
            self.Vue5.show()
            self.Vue5.seriesNum.selectAll()
            self.Vue5.seriesNum.setFocus()
        self.Vue4.progressBar.setValue(self.Vue4.progressBar.value() + 50)

    # Vue4
    #
    def check_status(self):
        ret, ser = self.port_open(self.com)
        if not ret:
            raise ValueError("port打开失败")
        # flag = ACW_basic(ser, "BBBB", 1)
        # if not flag:
        # raise ValueError("建立Testcase失败")
        self.single_step(ser)
        self.ACW_check(100, 10, 0, 1, 'OOOO', ser)
        ehi_cmd = "TEST\n"
        ret_val = ser.write(ehi_cmd.encode())
        time.sleep(0.1)
        if not ret_val:
            raise ValueError("EHI transimission failed")
        try:
            result = self.get_test_result(ser, dw_time=float(1))
            return True
        except:
            return False

    def get_communication_status(self):
        status = self.check_status()
        if status:
            self.Vue4.communication_status.setText("串口通讯正常")
            self.Vue4.communication_status.setStyleSheet("color: green")
            self.Vue4.communication_status.setStyleSheet("background: rgb(0, 255, 0)")
            self.Vue4.startBtn.setEnabled(True)
        else:
            self.Vue4.communication_status.setText("串口通讯失败")
            self.Vue4.communication_status.setStyleSheet("color: red")
            self.Vue4.communication_status.setStyleSheet("background: red")
            self.Vue4.startBtn.setEnabled(False)
        return status

    # update the testing status
    def update_testing_status(self, process_flag):
        if process_flag == 1:
            self.testing_status = "进行中"
            self.Vue4.testingStatus.setStyleSheet("color: black")
            self.Vue4.testingStatus.setStyleSheet("background: yellow")
        elif process_flag == 2:
            if self.angui_test_status:
                self.testing_status = "通过"
                self.Vue4.testingStatus.setStyleSheet("color: black")
                self.Vue4.testingStatus.setStyleSheet("background: rgb(0, 255, 0)")
            else:
                self.testing_status = "失败"
                self.Vue4.testingStatus.setStyleSheet("color: black")
                self.Vue4.testingStatus.setStyleSheet("background: red")
        else:
            self.testing_status = "未开始"
            self.Vue4.testingStatus.setStyleSheet("color: black")
        self.Vue4.testingStatus.setText(str(self.testing_status))

    # update basic info
    # 当前时间
    def current_time(self):
        self.time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        self.Vue4.timeBox.setText(self.time)

    # 操作员信息
    def operatorinfo(self):
        self.Vue4.User_name.setText(self.operator)

    # 基本信息
    def basicinfo(self):
        for i in self.data:
            if i[3] == self.SAPNo:
                self.Vue4.Product_No.setText(i[3])
                self.Vue4.Product_Type.setText(i[6])
                break
        self.Vue4.testedNum.setText(str(self.tested))
        self.Vue4.passedNum.setText(str(self.passed))
        self.Vue4.failedNum.setText(str(self.failed))
        self.Vue4.update_testing_status(self.process_flag)

    # 订单信息
    def orderinfo(self):
        self.Vue4.OrderID.setText(self.prodID)
        self.Vue4.OrderNum.setText(self.prodNum)
        self.Vue4.SAP_Num.setText(self.SAPNo)

    def update_info(self):
        self.orderinfo()
        self.operatorinfo()
        self.current_time()

    # update the number of passes and the status
    def update_progress(self):
        self.Vue4.testedNum.setText(str(self.tested))
        self.Vue4.passedNum.setText(str(self.passed))
        self.Vue4.failedNum.setText(str(self.failed))
        self.update_testing_status(self.process_flag)

    def status_update(self, flag):
        self.process_flag = flag
        self.update_testing_status(flag)
        self.hint = flag
        self.test_hint()

    # startbtn
    def start(self):
        # for i in range(0, self.table_item_no):
        #     self.Vue4.testing_data.setItem(i, 8, QTableWidgetItem("进行中"))
        #     a = self.Vue4.testing_data.item(i, 8)
        #     a.setBackground(QBrush(QColor(255, 255, 0)))
        #     self.Vue4.testing_data.setStyleSheet("color: black")
        # # check whether the tested order number is over(over has to start a new one)
        # self.status_update(1)
        # # if we have info already, we can directly start this
        # # self.test_progress()
        self.Vue5.show()

        # after gained the information, the related instuctions will be passed into the AnGui Analyzer
        # need a function here to execute the test

    def AnGui_operate(self,a):
        self.Vue4.startBtn.setEnabled(False)
        ret, ser = self.port_open(self.com)
        if not ret:
            raise ValueError("port打开失败")
        # make sure it is single step
        self.single_step(ser)
        # Only test single step right now
        start = time.time()
        operating_flag = True
        result_list = list()
        step_list = list()
        index = 0
        for i in self.dataSelected:
            # 3000,5,0.5,2,HHLLL3000OO
            steps = i[-1]
            step = steps.split(",")
            # ACW_test(voltage, uplimit, downlimit,testtime,channel,ser)
            self.ACW_test(step[0], step[1], step[2], step[3], step[4], ser)
            ehi_cmd = "TEST\n"
            ret_val = ser.write(ehi_cmd.encode())
            time.sleep(0.1)
            time.sleep(step[2] + 2 + 2)  # The true time is test time + ERU + ERD
            if not ret_val:
                raise ValueError("EHI transmission failed")
            result = self.get_test_result(ser, dw_time=float(step[2] + 2 + 2))  # The true time is test time + ERU + ERD
            result_list.append(result)
            step_list.append(steps)
            result_list.append(";")
            step_list.append(";")
            if "PASS" not in result and (index) < self.table_item_no:
                operating_flag = False
                self.angui_test_status = 0
                self.Vue4.testing_data.setItem(index, 8, QTableWidgetItem("失败"))
                a = self.Vue4.testing_data.item(index, 8)
                a.setBackground(QBrush(QColor(255, 0, 0)))
            elif "PASS" in result and (index) < self.table_item_no:
                self.angui_test_status = 1
                self.Vue4.testing_data.setItem(index, 8, QTableWidgetItem("通过"))
                a = self.Vue4.testing_data.item(index, 8)
                a.setBackground(QBrush(QColor(0, 255, 0)))
            index += 1

        self.steps_tested = index
        self.elapsed = time.time() - start
        self.Vue4.testUsedTime.setText(str(self.elapsed))
        self.tested += 1
        if operating_flag:
            self.passed += 1
        else:
            self.failed += 1
        self.store_result(result_list, step_list)
        self.status_update(2)
        # update the status bar
        # self.figure_num(operating_flag)
        # self.test_progress()
        # update the number etc
        self.update_progress()
        # update the other status
        time.sleep(2)
        self.Vue4.startBtn.setEnabled(True)
        self.Vue5.show()

    def store_result(self, result, steps):
        steps = ''.join(steps)
        result = ''.join(result)
        if "PASS" in result:
            status = "PASS"
        else:
            status = "FAIL"
        dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        data_import = "insert into dbo.TestData(ORDER_ID, ORDER_NUMBER, SAP_NUMBER, OPERATOR, EXECUTION_TIME, START_DATE_TIME,PRODUCTION_STATUS, TEST_DATA,TEST_RESULT,SERIES_NUM) values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (
            self.prodID, self.prodNum, self.SAPNo, self.operator, str(self.elapsed), dt, status,
            steps,
            result, self.serialNum)
        # print(data_import)
        self.dataBase.execute_sql(data_import)
        return

    # update the number of passes and number of fails
    # def figure_num(self, flag):
    #     if flag:
    #         status = 1
    #     else:
    #         status = 2
    #     if self.tested == 31:
    #         index = self.tested % 30
    #         self.testing_status_list = [0] * 30
    #         self.testing_status_list[0] = status
    #     else:
    #         index = self.tested % 30 - 1
    #         self.testing_status_list[index] = status

    # 在press start之后跳出来的小框
    # 要求scan号,and will fill the corresponding values
    def scanSAP(self):
        pass

    # 终止
    def reset(self):
        # # reset everystatus bar and demos
        # self.status_update(0)
        # self.tested = 0
        # self.passed = 0
        # self.failed = 0
        # self.Vue4.testUsedTime.setText("")
        # # self.testing_status_list = [0] * 30
        # # self.test_progress()
        # self.get_communication_status()
        # for i in range(0, self.steps_tested):
        #     self.Vue4.testing_data.setItem(i, 8, QTableWidgetItem("未开始"))
        # self.Vue4.testing_data.clearContents()
        # self.steps_tested = 0
        # self.table_item_no = 0
        # self.product_table()
        # # sending he reset signal to the AnGui analyzer
        #stop_thread(self.thread_test)
        return

    # 退出
    # def exit(self):
    # Close all the ongoing process
    # self.close()

    # 测试统计,0 means has not start yet, 1 means started and pass, 2 means started and failed
    # def test_progress(self):
    #     #print(self.testing_status_list)
    #     #add a flag here to show the red status when a product fails
    #     for x in range(0,len(self.testing_status_list)):
    #         if self.testing_status_list[x] == 0:
    #             self.draw_blank(x+1)
    #         elif self.testing_status_list[x] == 1:
    #             self.draw_green(x+1)
    #         elif self.testing_status_list[x] == 2:
    #             self.draw_red(x+1)

    # test result
    def test_hint(self):
        '''
        get three different test status,a dn give the hints accordingly
        0: has not started
        1: started but not finished
        2: finished, display the result
        :return:
        '''
        if self.hint == 0:
            self.Vue4.test_hints.setText("确定产品信息无误之后点击开始来进行检测")
            self.Vue4.test_hints.setStyleSheet(("color: rgb(0, 0, 0);"))
            self.Vue4.test_hints.setFontPointSize(40)
        elif self.hint == 1:
            self.Vue4.test_hints.setText("产品正在进行检测中，如需关闭进程请先点停止然后再退出")
            self.Vue4.test_hints.setStyleSheet(("color: rgb(0, 0, 255);"))
            self.Vue4.test_hints.setFontPointSize(40)
        elif self.hint == 2:
            self.Vue4.test_hints.setText("产品已检测完，此订单号通过%s个，失败%s个" % (str(self.passed), str(self.failed)))
            self.Vue4.test_hints.setStyleSheet(("color: rgb(124, 0, 124);"))
            self.Vue4.test_hints.setFontPointSize(40)

    # 产品表
    def product_table(self):
        if (self.table_item_no + len(self.dataSelected)) > 10:
            self.Vue4.testing_data.clearContents()
            self.table_item_no = 0
        for i in range(0, len(self.dataSelected)):
            info = self.dataSelected[i]
            steps = info[-1]
            single_step = steps.split(",")
            self.Vue4.testing_data.setItem(self.table_item_no, 0, QTableWidgetItem((info[3])))
            self.Vue4.testing_data.setItem(self.table_item_no, 1, QTableWidgetItem(info[-1]))
            self.Vue4.testing_data.setItem(self.table_item_no, 2, QTableWidgetItem("安规测试仪测试"))
            self.Vue4.testing_data.setItem(self.table_item_no, 3, QTableWidgetItem("ACW测试"))
            self.Vue4.testing_data.setItem(self.table_item_no, 4, QTableWidgetItem(single_step[0]))
            self.Vue4.testing_data.setItem(self.table_item_no, 5, QTableWidgetItem(single_step[3]))
            self.Vue4.testing_data.setItem(self.table_item_no, 6,
                                           QTableWidgetItem(single_step[1] + ' ~ ' + single_step[2]))
            self.Vue4.testing_data.setItem(self.table_item_no, 7, QTableWidgetItem(single_step[4]))
            self.Vue4.testing_data.setItem(self.table_item_no, 8, QTableWidgetItem("未开始"))
            a = self.Vue4.testing_data.item(self.table_item_no, 8)
            a.setBackground(QBrush(QColor(255, 255, 255)))
            self.table_item_no += 1

# open the corresponding port
def port_open(portx, bbr=9600, time=None):
    ret = False
    ser = None
    # to see any errors
    try:
        ser = serial.Serial(portx, bbr, bytesize=8, timeout=0)
        if (ser.is_open):
            ret = True

    except Exception:
        print("Exception happened")
        ret = False

    # to see whether or not it opened successfully
    return ret, ser

# check the connection and function
def ACW_check(voltage, uplimit, downlimit, testtime, channel, ser):

    ser.write("FN 1,TempTest\n".encode())
    # command transition needs time
    time.sleep(0.1)

    ret_val = ser.write("SAA\n".encode())
    time.sleep(0.1)

    if not ret_val:
        raise ValueError("SAA transimission failed")

    dw_cmd = "EV " + str(voltage) + "\n"
    ser.write(dw_cmd.encode())
    time.sleep(0.1)

    dw_cmd = "EHT " + str(uplimit) + "\n"
    ser.write(dw_cmd.encode())
    time.sleep(0.1)

    dw_cmd = "ELT " + str(downlimit) + "\n"
    ser.write(dw_cmd.encode())
    time.sleep(0.1)

    dw_cmd = "ERU " + "0.1\n"
    ser.write(dw_cmd.encode())
    time.sleep(0.1)

    dw_cmd = "EDW " + str(testtime) + "\n"
    ser.write(dw_cmd.encode())
    time.sleep(0.1)

    dw_cmd = "ERD " + "0\n"
    ser.write(dw_cmd.encode())
    time.sleep(0.1)

    dw_cmd = "ES " + str(channel) + "OOOOOOOO\n"
    ser.write(dw_cmd.encode())
    time.sleep(0.1)

# specified the test data
def ACW_test(voltage, uplimit, downlimit, testtime, channel, ser):

    ser.write("FN 1,TempTest\n".encode())
    # command transition needs time
    time.sleep(0.1)

    ret_val = ser.write("SAA\n".encode())
    time.sleep(0.1)

    if not ret_val:
        raise ValueError("SAA transimission failed")

    dw_cmd = "EV " + str(voltage) + "\n"
    ser.write(dw_cmd.encode())
    time.sleep(0.1)

    dw_cmd = "EHT " + str(uplimit) + "\n"
    ser.write(dw_cmd.encode())
    time.sleep(0.1)

    dw_cmd = "ELT " + str(downlimit) + "\n"
    ser.write(dw_cmd.encode())
    time.sleep(0.1)

    dw_cmd = "ERU " + "2\n"
    ser.write(dw_cmd.encode())
    time.sleep(0.1)

    dw_cmd = "EDW " + str(testtime) + "\n"
    ser.write(dw_cmd.encode())
    time.sleep(0.1)

    dw_cmd = "ERD " + "2\n"
    ser.write(dw_cmd.encode())
    time.sleep(0.1)

    dw_cmd = "ES " + str(channel) + "OOOOOOOO\n"
    ser.write(dw_cmd.encode())
    time.sleep(0.1)

def get_test_result(ser, dw_time):

    # time.sleep(dw_time + 0.1)
    search_cmd = "TD?\n"
    ser.write(search_cmd.encode())
    time.sleep(0.1)
    str = ""
    index = 0
    while True:
        if ser.in_waiting and index < 30:
            time.sleep(2)
            str = ser.read(ser.in_waiting).decode()
            if (str == "exit"):
                break
            else:
                pass
        else:
            break

    filter = re.search(r'[\w]+[,][\w]+[,][^\t\n]+[,][\w|\.]+[,][\w|\.]+[,][\w|\.]+[,][\w|\.]+', str)
    str = filter.group()
    ser.write(("RESET\n").encode())
    time.sleep(0.1)
    return str

# make sure the analyzer's mode is single step mode
def single_step(ser):
    time.sleep(0.15)
    single_cmd = "SSI 1\n"
    ret_val = ser.write(single_cmd.encode())
    time.sleep(0.1)
    # print(ret_val.decode())
    return

# def _async_raise(tid, exctype):
#     """raises the exception, performs cleanup if needed"""
#     tid = ctypes.c_long(tid)
#     if not inspect.isclass(exctype):
#         exctype = type(exctype)
#     res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))
#     if res == 0:
#         raise ValueError("invalid thread id")
#     elif res != 1:
#         # """if it returns a number greater than one, you're in trouble,
#         # and you should call it again with exc=NULL to revert the effect"""
#         ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
#         raise SystemError("PyThreadState_SetAsyncExc failed")
# def stop_thread(thread):
#     if thread.isAlive():
#         _async_raise(thread.ident, SystemExit)

if __name__ == "__main__":
    App = QApplication(sys.argv)
    ctrl = Controller()
    ctrl.Vue1.show()
    # App = QApplication(sys.argv)
    # ctrl.Vue1.show()
    sys.exit(App.exec_())
