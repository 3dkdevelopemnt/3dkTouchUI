# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'win_keyboard3.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(480, 321)
        self.Keyholder = QtWidgets.QStackedWidget(Form)
        self.Keyholder.setGeometry(QtCore.QRect(0, 70, 481, 251))
        self.Keyholder.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    border-right: none;\n"
"border-bottom: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}")
        self.Keyholder.setObjectName("Keyholder")
        self.pagealpha = QtWidgets.QWidget()
        self.pagealpha.setObjectName("pagealpha")
        self.btn1 = QtWidgets.QPushButton(self.pagealpha)
        self.btn1.setGeometry(QtCore.QRect(0, 0, 48, 60))
        self.btn1.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    border-right: none;\n"
"border-bottom: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}")
        self.btn1.setObjectName("btn1")
        self.btn2 = QtWidgets.QPushButton(self.pagealpha)
        self.btn2.setGeometry(QtCore.QRect(48, 0, 48, 60))
        self.btn2.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    border-right: none;\n"
"border-bottom: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}")
        self.btn2.setObjectName("btn2")
        self.btn3 = QtWidgets.QPushButton(self.pagealpha)
        self.btn3.setGeometry(QtCore.QRect(96, 0, 48, 60))
        self.btn3.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    border-right: none;\n"
"border-bottom: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}")
        self.btn3.setObjectName("btn3")
        self.btn4 = QtWidgets.QPushButton(self.pagealpha)
        self.btn4.setGeometry(QtCore.QRect(144, 0, 48, 60))
        self.btn4.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    border-right: none;\n"
"border-bottom: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}")
        self.btn4.setObjectName("btn4")
        self.btn5 = QtWidgets.QPushButton(self.pagealpha)
        self.btn5.setGeometry(QtCore.QRect(192, 0, 48, 60))
        self.btn5.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    border-right: none;\n"
"border-bottom: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}")
        self.btn5.setObjectName("btn5")
        self.btn6 = QtWidgets.QPushButton(self.pagealpha)
        self.btn6.setGeometry(QtCore.QRect(240, 0, 48, 60))
        self.btn6.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    border-right: none;\n"
"border-bottom: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}")
        self.btn6.setObjectName("btn6")
        self.btn7 = QtWidgets.QPushButton(self.pagealpha)
        self.btn7.setGeometry(QtCore.QRect(288, 0, 48, 60))
        self.btn7.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    border-right: none;\n"
"border-bottom: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}")
        self.btn7.setObjectName("btn7")
        self.btn8 = QtWidgets.QPushButton(self.pagealpha)
        self.btn8.setGeometry(QtCore.QRect(336, 0, 48, 60))
        self.btn8.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    border-right: none;\n"
"border-bottom: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}")
        self.btn8.setObjectName("btn8")
        self.btn9 = QtWidgets.QPushButton(self.pagealpha)
        self.btn9.setGeometry(QtCore.QRect(384, 0, 48, 60))
        self.btn9.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    border-right: none;\n"
"border-bottom: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}")
        self.btn9.setObjectName("btn9")
        self.btn10 = QtWidgets.QPushButton(self.pagealpha)
        self.btn10.setGeometry(QtCore.QRect(432, 0, 48, 60))
        self.btn10.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    border-right: none;\n"
"border-bottom: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}")
        self.btn10.setObjectName("btn10")
        self.btn11 = QtWidgets.QPushButton(self.pagealpha)
        self.btn11.setGeometry(QtCore.QRect(0, 60, 48, 60))
        self.btn11.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    border-right: none;\n"
"border-bottom: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}")
        self.btn11.setObjectName("btn11")
        self.btn12 = QtWidgets.QPushButton(self.pagealpha)
        self.btn12.setGeometry(QtCore.QRect(48, 60, 48, 60))
        self.btn12.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    border-right: none;\n"
"border-bottom: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}")
        self.btn12.setObjectName("btn12")
        self.btn13 = QtWidgets.QPushButton(self.pagealpha)
        self.btn13.setGeometry(QtCore.QRect(96, 60, 48, 60))
        self.btn13.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    border-right: none;\n"
"border-bottom: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}")
        self.btn13.setObjectName("btn13")
        self.btn14 = QtWidgets.QPushButton(self.pagealpha)
        self.btn14.setGeometry(QtCore.QRect(144, 60, 48, 60))
        self.btn14.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    border-right: none;\n"
"border-bottom: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}")
        self.btn14.setObjectName("btn14")
        self.btn15 = QtWidgets.QPushButton(self.pagealpha)
        self.btn15.setGeometry(QtCore.QRect(192, 60, 48, 60))
        self.btn15.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    border-right: none;\n"
"border-bottom: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}")
        self.btn15.setObjectName("btn15")
        self.btn16 = QtWidgets.QPushButton(self.pagealpha)
        self.btn16.setGeometry(QtCore.QRect(240, 60, 48, 60))
        self.btn16.setObjectName("btn16")
        self.btn17 = QtWidgets.QPushButton(self.pagealpha)
        self.btn17.setGeometry(QtCore.QRect(288, 60, 48, 60))
        self.btn17.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    border-right: none;\n"
"border-bottom: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}")
        self.btn17.setObjectName("btn17")
        self.btn18 = QtWidgets.QPushButton(self.pagealpha)
        self.btn18.setGeometry(QtCore.QRect(336, 60, 48, 60))
        self.btn18.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    border-right: none;\n"
"border-bottom: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}")
        self.btn18.setObjectName("btn18")
        self.btn19 = QtWidgets.QPushButton(self.pagealpha)
        self.btn19.setGeometry(QtCore.QRect(384, 60, 48, 60))
        self.btn19.setObjectName("btn19")
        self.s_backspace = QtWidgets.QPushButton(self.pagealpha)
        self.s_backspace.setGeometry(QtCore.QRect(432, 60, 48, 60))
        self.s_backspace.setObjectName("s_backspace")
        self.upperalpha = QtWidgets.QPushButton(self.pagealpha)
        self.upperalpha.setGeometry(QtCore.QRect(0, 120, 48, 60))
        self.upperalpha.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    border-right: none;\n"
"border-bottom: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}")
        self.upperalpha.setObjectName("upperalpha")
        self.btn20 = QtWidgets.QPushButton(self.pagealpha)
        self.btn20.setGeometry(QtCore.QRect(48, 120, 48, 60))
        self.btn20.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    border-right: none;\n"
"border-bottom: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}")
        self.btn20.setObjectName("btn20")
        self.btn21 = QtWidgets.QPushButton(self.pagealpha)
        self.btn21.setGeometry(QtCore.QRect(96, 120, 48, 60))
        self.btn21.setObjectName("btn21")
        self.btn22 = QtWidgets.QPushButton(self.pagealpha)
        self.btn22.setGeometry(QtCore.QRect(144, 120, 48, 60))
        self.btn22.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    border-right: none;\n"
"border-bottom: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}")
        self.btn22.setObjectName("btn22")
        self.btn23 = QtWidgets.QPushButton(self.pagealpha)
        self.btn23.setGeometry(QtCore.QRect(192, 120, 48, 60))
        self.btn23.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    border-right: none;\n"
"border-bottom: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}")
        self.btn23.setObjectName("btn23")
        self.btn24 = QtWidgets.QPushButton(self.pagealpha)
        self.btn24.setGeometry(QtCore.QRect(240, 120, 48, 60))
        self.btn24.setObjectName("btn24")
        self.btn25 = QtWidgets.QPushButton(self.pagealpha)
        self.btn25.setGeometry(QtCore.QRect(288, 120, 48, 60))
        self.btn25.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    border-right: none;\n"
"border-bottom: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}")
        self.btn25.setObjectName("btn25")
        self.btn26 = QtWidgets.QPushButton(self.pagealpha)
        self.btn26.setGeometry(QtCore.QRect(336, 120, 48, 60))
        self.btn26.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    border-right: none;\n"
"border-bottom: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}")
        self.btn26.setObjectName("btn26")
        self.alphas_dot = QtWidgets.QPushButton(self.pagealpha)
        self.alphas_dot.setGeometry(QtCore.QRect(384, 120, 48, 60))
        self.alphas_dot.setObjectName("alphas_dot")
        self.alphas_comma = QtWidgets.QPushButton(self.pagealpha)
        self.alphas_comma.setGeometry(QtCore.QRect(432, 120, 48, 60))
        self.alphas_comma.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    border-right: none;\n"
"border-bottom: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}")
        self.alphas_comma.setObjectName("alphas_comma")
        self.numericbutton = QtWidgets.QPushButton(self.pagealpha)
        self.numericbutton.setGeometry(QtCore.QRect(0, 180, 81, 81))
        self.numericbutton.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    border-right: none;\n"
"border-bottom: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}")
        self.numericbutton.setObjectName("numericbutton")
        self.sepecialchar = QtWidgets.QPushButton(self.pagealpha)
        self.sepecialchar.setGeometry(QtCore.QRect(80, 180, 111, 81))
        self.sepecialchar.setObjectName("sepecialchar")
        self.alphas_space = QtWidgets.QPushButton(self.pagealpha)
        self.alphas_space.setGeometry(QtCore.QRect(190, 180, 201, 81))
        self.alphas_space.setObjectName("alphas_space")
        self.alphas_submit = QtWidgets.QPushButton(self.pagealpha)
        self.alphas_submit.setGeometry(QtCore.QRect(390, 180, 91, 81))
        self.alphas_submit.setObjectName("alphas_submit")
        self.Keyholder.addWidget(self.pagealpha)
        self.PageUAlpha = QtWidgets.QWidget()
        self.PageUAlpha.setObjectName("PageUAlpha")
        self.btn27 = QtWidgets.QPushButton(self.PageUAlpha)
        self.btn27.setGeometry(QtCore.QRect(0, 0, 48, 60))
        self.btn27.setObjectName("btn27")
        self.btn28 = QtWidgets.QPushButton(self.PageUAlpha)
        self.btn28.setGeometry(QtCore.QRect(48, 0, 48, 60))
        self.btn28.setObjectName("btn28")
        self.btn29 = QtWidgets.QPushButton(self.PageUAlpha)
        self.btn29.setGeometry(QtCore.QRect(96, 0, 48, 60))
        self.btn29.setObjectName("btn29")
        self.btn30 = QtWidgets.QPushButton(self.PageUAlpha)
        self.btn30.setGeometry(QtCore.QRect(144, 0, 48, 60))
        self.btn30.setObjectName("btn30")
        self.btn31 = QtWidgets.QPushButton(self.PageUAlpha)
        self.btn31.setGeometry(QtCore.QRect(192, 0, 48, 60))
        self.btn31.setObjectName("btn31")
        self.btn32 = QtWidgets.QPushButton(self.PageUAlpha)
        self.btn32.setGeometry(QtCore.QRect(238, 0, 48, 60))
        self.btn32.setObjectName("btn32")
        self.btn33 = QtWidgets.QPushButton(self.PageUAlpha)
        self.btn33.setGeometry(QtCore.QRect(286, 0, 48, 60))
        self.btn33.setObjectName("btn33")
        self.btn34 = QtWidgets.QPushButton(self.PageUAlpha)
        self.btn34.setGeometry(QtCore.QRect(334, 0, 48, 60))
        self.btn34.setObjectName("btn34")
        self.btn35 = QtWidgets.QPushButton(self.PageUAlpha)
        self.btn35.setGeometry(QtCore.QRect(382, 0, 48, 60))
        self.btn35.setObjectName("btn35")
        self.btn36 = QtWidgets.QPushButton(self.PageUAlpha)
        self.btn36.setGeometry(QtCore.QRect(426, 0, 61, 60))
        self.btn36.setObjectName("btn36")
        self.btn37 = QtWidgets.QPushButton(self.PageUAlpha)
        self.btn37.setGeometry(QtCore.QRect(0, 60, 48, 60))
        self.btn37.setObjectName("btn37")
        self.btn38 = QtWidgets.QPushButton(self.PageUAlpha)
        self.btn38.setGeometry(QtCore.QRect(48, 60, 48, 60))
        self.btn38.setObjectName("btn38")
        self.btn39 = QtWidgets.QPushButton(self.PageUAlpha)
        self.btn39.setGeometry(QtCore.QRect(96, 60, 48, 60))
        self.btn39.setObjectName("btn39")
        self.btn40 = QtWidgets.QPushButton(self.PageUAlpha)
        self.btn40.setGeometry(QtCore.QRect(144, 60, 48, 60))
        self.btn40.setObjectName("btn40")
        self.btn41 = QtWidgets.QPushButton(self.PageUAlpha)
        self.btn41.setGeometry(QtCore.QRect(192, 60, 48, 60))
        self.btn41.setObjectName("btn41")
        self.btn42 = QtWidgets.QPushButton(self.PageUAlpha)
        self.btn42.setGeometry(QtCore.QRect(238, 60, 48, 60))
        self.btn42.setObjectName("btn42")
        self.btn43 = QtWidgets.QPushButton(self.PageUAlpha)
        self.btn43.setGeometry(QtCore.QRect(286, 60, 48, 60))
        self.btn43.setObjectName("btn43")
        self.btn44 = QtWidgets.QPushButton(self.PageUAlpha)
        self.btn44.setGeometry(QtCore.QRect(334, 60, 48, 60))
        self.btn44.setObjectName("btn44")
        self.btn45 = QtWidgets.QPushButton(self.PageUAlpha)
        self.btn45.setGeometry(QtCore.QRect(382, 60, 48, 60))
        self.btn45.setObjectName("btn45")
        self.pushButton_56 = QtWidgets.QPushButton(self.PageUAlpha)
        self.pushButton_56.setGeometry(QtCore.QRect(426, 60, 61, 60))
        self.pushButton_56.setObjectName("pushButton_56")
        self.alphau_down = QtWidgets.QPushButton(self.PageUAlpha)
        self.alphau_down.setGeometry(QtCore.QRect(0, 120, 48, 60))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.alphau_down.setFont(font)
        self.alphau_down.setObjectName("alphau_down")
        self.btn46 = QtWidgets.QPushButton(self.PageUAlpha)
        self.btn46.setGeometry(QtCore.QRect(48, 120, 48, 60))
        self.btn46.setObjectName("btn46")
        self.btn47 = QtWidgets.QPushButton(self.PageUAlpha)
        self.btn47.setGeometry(QtCore.QRect(96, 120, 48, 60))
        self.btn47.setObjectName("btn47")
        self.btn48 = QtWidgets.QPushButton(self.PageUAlpha)
        self.btn48.setGeometry(QtCore.QRect(144, 120, 48, 60))
        self.btn48.setObjectName("btn48")
        self.btn49 = QtWidgets.QPushButton(self.PageUAlpha)
        self.btn49.setGeometry(QtCore.QRect(192, 120, 48, 60))
        self.btn49.setObjectName("btn49")
        self.btn50 = QtWidgets.QPushButton(self.PageUAlpha)
        self.btn50.setGeometry(QtCore.QRect(238, 120, 48, 60))
        self.btn50.setObjectName("btn50")
        self.btn51 = QtWidgets.QPushButton(self.PageUAlpha)
        self.btn51.setGeometry(QtCore.QRect(286, 120, 48, 60))
        self.btn51.setObjectName("btn51")
        self.btn52 = QtWidgets.QPushButton(self.PageUAlpha)
        self.btn52.setGeometry(QtCore.QRect(334, 120, 48, 60))
        self.btn52.setObjectName("btn52")
        self.btn53 = QtWidgets.QPushButton(self.PageUAlpha)
        self.btn53.setGeometry(QtCore.QRect(382, 120, 48, 60))
        self.btn53.setObjectName("btn53")
        self.btn54 = QtWidgets.QPushButton(self.PageUAlpha)
        self.btn54.setGeometry(QtCore.QRect(426, 120, 61, 60))
        self.btn54.setObjectName("btn54")
        self.pushButton_67 = QtWidgets.QPushButton(self.PageUAlpha)
        self.pushButton_67.setGeometry(QtCore.QRect(0, 180, 121, 71))
        self.pushButton_67.setObjectName("pushButton_67")
        self.pushButton_68 = QtWidgets.QPushButton(self.PageUAlpha)
        self.pushButton_68.setGeometry(QtCore.QRect(120, 180, 101, 71))
        self.pushButton_68.setObjectName("pushButton_68")
        self.pushButton_69 = QtWidgets.QPushButton(self.PageUAlpha)
        self.pushButton_69.setGeometry(QtCore.QRect(220, 180, 181, 71))
        self.pushButton_69.setObjectName("pushButton_69")
        self.pushButton_70 = QtWidgets.QPushButton(self.PageUAlpha)
        self.pushButton_70.setGeometry(QtCore.QRect(400, 180, 81, 71))
        self.pushButton_70.setObjectName("pushButton_70")
        self.Keyholder.addWidget(self.PageUAlpha)
        self.pagenumerical = QtWidgets.QWidget()
        self.pagenumerical.setObjectName("pagenumerical")
        self.btn55 = QtWidgets.QPushButton(self.pagenumerical)
        self.btn55.setGeometry(QtCore.QRect(0, 0, 96, 60))
        self.btn55.setObjectName("btn55")
        self.btn56 = QtWidgets.QPushButton(self.pagenumerical)
        self.btn56.setGeometry(QtCore.QRect(96, 0, 96, 60))
        self.btn56.setObjectName("btn56")
        self.btn57 = QtWidgets.QPushButton(self.pagenumerical)
        self.btn57.setGeometry(QtCore.QRect(190, 0, 96, 60))
        self.btn57.setObjectName("btn57")
        self.btn65 = QtWidgets.QPushButton(self.pagenumerical)
        self.btn65.setGeometry(QtCore.QRect(286, 0, 96, 60))
        self.btn65.setObjectName("btn65")
        self.pushButton_75 = QtWidgets.QPushButton(self.pagenumerical)
        self.pushButton_75.setGeometry(QtCore.QRect(380, 0, 100, 60))
        self.pushButton_75.setObjectName("pushButton_75")
        self.btn58 = QtWidgets.QPushButton(self.pagenumerical)
        self.btn58.setGeometry(QtCore.QRect(0, 60, 96, 60))
        self.btn58.setObjectName("btn58")
        self.btn59 = QtWidgets.QPushButton(self.pagenumerical)
        self.btn59.setGeometry(QtCore.QRect(96, 60, 96, 60))
        self.btn59.setObjectName("btn59")
        self.btn60 = QtWidgets.QPushButton(self.pagenumerical)
        self.btn60.setGeometry(QtCore.QRect(190, 60, 96, 60))
        self.btn60.setObjectName("btn60")
        self.btn66 = QtWidgets.QPushButton(self.pagenumerical)
        self.btn66.setGeometry(QtCore.QRect(286, 60, 96, 60))
        self.btn66.setObjectName("btn66")
        self.pushButton_80 = QtWidgets.QPushButton(self.pagenumerical)
        self.pushButton_80.setGeometry(QtCore.QRect(380, 60, 100, 60))
        self.pushButton_80.setObjectName("pushButton_80")
        self.btn61 = QtWidgets.QPushButton(self.pagenumerical)
        self.btn61.setGeometry(QtCore.QRect(0, 120, 96, 60))
        self.btn61.setObjectName("btn61")
        self.btn62 = QtWidgets.QPushButton(self.pagenumerical)
        self.btn62.setGeometry(QtCore.QRect(96, 120, 96, 60))
        self.btn62.setObjectName("btn62")
        self.btn63 = QtWidgets.QPushButton(self.pagenumerical)
        self.btn63.setGeometry(QtCore.QRect(190, 120, 96, 60))
        self.btn63.setObjectName("btn63")
        self.btn67 = QtWidgets.QPushButton(self.pagenumerical)
        self.btn67.setGeometry(QtCore.QRect(286, 120, 96, 60))
        self.btn67.setObjectName("btn67")
        self.btn69 = QtWidgets.QPushButton(self.pagenumerical)
        self.btn69.setGeometry(QtCore.QRect(380, 120, 100, 60))
        self.btn69.setObjectName("btn69")
        self.numeric_back = QtWidgets.QPushButton(self.pagenumerical)
        self.numeric_back.setGeometry(QtCore.QRect(0, 180, 96, 71))
        self.numeric_back.setObjectName("numeric_back")
        self.alphas_special = QtWidgets.QPushButton(self.pagenumerical)
        self.alphas_special.setGeometry(QtCore.QRect(96, 180, 96, 71))
        self.alphas_special.setObjectName("alphas_special")
        self.btn64 = QtWidgets.QPushButton(self.pagenumerical)
        self.btn64.setGeometry(QtCore.QRect(190, 180, 96, 71))
        self.btn64.setObjectName("btn64")
        self.btn68 = QtWidgets.QPushButton(self.pagenumerical)
        self.btn68.setGeometry(QtCore.QRect(286, 180, 96, 71))
        self.btn68.setObjectName("btn68")
        self.pushButton_90 = QtWidgets.QPushButton(self.pagenumerical)
        self.pushButton_90.setGeometry(QtCore.QRect(380, 180, 100, 71))
        self.pushButton_90.setObjectName("pushButton_90")
        self.Keyholder.addWidget(self.pagenumerical)
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.btn70 = QtWidgets.QPushButton(self.page)
        self.btn70.setGeometry(QtCore.QRect(0, 0, 48, 60))
        self.btn70.setObjectName("btn70")
        self.btn71 = QtWidgets.QPushButton(self.page)
        self.btn71.setGeometry(QtCore.QRect(48, 0, 48, 60))
        self.btn71.setObjectName("btn71")
        self.btn72 = QtWidgets.QPushButton(self.page)
        self.btn72.setGeometry(QtCore.QRect(96, 0, 48, 60))
        self.btn72.setObjectName("btn72")
        self.btn73 = QtWidgets.QPushButton(self.page)
        self.btn73.setGeometry(QtCore.QRect(144, 0, 48, 60))
        self.btn73.setObjectName("btn73")
        self.btn74 = QtWidgets.QPushButton(self.page)
        self.btn74.setGeometry(QtCore.QRect(192, 0, 48, 60))
        self.btn74.setObjectName("btn74")
        self.btn75 = QtWidgets.QPushButton(self.page)
        self.btn75.setGeometry(QtCore.QRect(240, 0, 48, 60))
        self.btn75.setObjectName("btn75")
        self.btn76 = QtWidgets.QPushButton(self.page)
        self.btn76.setGeometry(QtCore.QRect(288, 0, 48, 60))
        self.btn76.setObjectName("btn76")
        self.btn77 = QtWidgets.QPushButton(self.page)
        self.btn77.setGeometry(QtCore.QRect(336, 0, 48, 60))
        self.btn77.setObjectName("btn77")
        self.btn78 = QtWidgets.QPushButton(self.page)
        self.btn78.setGeometry(QtCore.QRect(384, 0, 48, 60))
        self.btn78.setObjectName("btn78")
        self.btn79 = QtWidgets.QPushButton(self.page)
        self.btn79.setGeometry(QtCore.QRect(432, 0, 48, 60))
        self.btn79.setObjectName("btn79")
        self.btn80 = QtWidgets.QPushButton(self.page)
        self.btn80.setGeometry(QtCore.QRect(0, 60, 48, 60))
        self.btn80.setObjectName("btn80")
        self.btn81 = QtWidgets.QPushButton(self.page)
        self.btn81.setGeometry(QtCore.QRect(48, 60, 48, 60))
        self.btn81.setObjectName("btn81")
        self.btn82 = QtWidgets.QPushButton(self.page)
        self.btn82.setGeometry(QtCore.QRect(96, 60, 48, 60))
        self.btn82.setObjectName("btn82")
        self.btn83 = QtWidgets.QPushButton(self.page)
        self.btn83.setGeometry(QtCore.QRect(144, 60, 48, 60))
        self.btn83.setObjectName("btn83")
        self.btn84 = QtWidgets.QPushButton(self.page)
        self.btn84.setGeometry(QtCore.QRect(192, 60, 48, 60))
        self.btn84.setObjectName("btn84")
        self.btn85 = QtWidgets.QPushButton(self.page)
        self.btn85.setGeometry(QtCore.QRect(240, 60, 48, 60))
        self.btn85.setObjectName("btn85")
        self.btn86 = QtWidgets.QPushButton(self.page)
        self.btn86.setGeometry(QtCore.QRect(288, 60, 48, 60))
        self.btn86.setObjectName("btn86")
        self.btn87 = QtWidgets.QPushButton(self.page)
        self.btn87.setGeometry(QtCore.QRect(336, 60, 48, 60))
        self.btn87.setObjectName("btn87")
        self.pushButton_110 = QtWidgets.QPushButton(self.page)
        self.pushButton_110.setGeometry(QtCore.QRect(384, 60, 101, 60))
        self.pushButton_110.setObjectName("pushButton_110")
        self.btn88 = QtWidgets.QPushButton(self.page)
        self.btn88.setGeometry(QtCore.QRect(0, 120, 48, 60))
        self.btn88.setObjectName("btn88")
        self.btn89 = QtWidgets.QPushButton(self.page)
        self.btn89.setGeometry(QtCore.QRect(48, 120, 48, 60))
        self.btn89.setObjectName("btn89")
        self.btn90 = QtWidgets.QPushButton(self.page)
        self.btn90.setGeometry(QtCore.QRect(96, 120, 48, 60))
        self.btn90.setObjectName("btn90")
        self.btn91 = QtWidgets.QPushButton(self.page)
        self.btn91.setGeometry(QtCore.QRect(144, 120, 48, 60))
        self.btn91.setObjectName("btn91")
        self.btn92 = QtWidgets.QPushButton(self.page)
        self.btn92.setGeometry(QtCore.QRect(192, 120, 48, 60))
        self.btn92.setObjectName("btn92")
        self.btn93 = QtWidgets.QPushButton(self.page)
        self.btn93.setGeometry(QtCore.QRect(240, 120, 48, 60))
        self.btn93.setObjectName("btn93")
        self.btn94 = QtWidgets.QPushButton(self.page)
        self.btn94.setGeometry(QtCore.QRect(288, 120, 48, 60))
        self.btn94.setObjectName("btn94")
        self.btn95 = QtWidgets.QPushButton(self.page)
        self.btn95.setGeometry(QtCore.QRect(336, 120, 48, 60))
        self.btn95.setObjectName("btn95")
        self.btn96 = QtWidgets.QPushButton(self.page)
        self.btn96.setGeometry(QtCore.QRect(384, 120, 48, 60))
        self.btn96.setObjectName("btn96")
        self.btn97 = QtWidgets.QPushButton(self.page)
        self.btn97.setGeometry(QtCore.QRect(432, 120, 48, 60))
        self.btn97.setObjectName("btn97")
        self.pushButton_120 = QtWidgets.QPushButton(self.page)
        self.pushButton_120.setGeometry(QtCore.QRect(0, 180, 93, 71))
        self.pushButton_120.setObjectName("pushButton_120")
        self.pushButton_121 = QtWidgets.QPushButton(self.page)
        self.pushButton_121.setGeometry(QtCore.QRect(90, 180, 101, 71))
        self.pushButton_121.setObjectName("pushButton_121")
        self.btn98 = QtWidgets.QPushButton(self.page)
        self.btn98.setGeometry(QtCore.QRect(190, 180, 51, 71))
        self.btn98.setObjectName("btn98")
        self.btn99 = QtWidgets.QPushButton(self.page)
        self.btn99.setGeometry(QtCore.QRect(240, 180, 49, 71))
        self.btn99.setObjectName("btn99")
        self.pushButton_124 = QtWidgets.QPushButton(self.page)
        self.pushButton_124.setGeometry(QtCore.QRect(290, 180, 94, 71))
        self.pushButton_124.setObjectName("pushButton_124")
        self.pushButton_125 = QtWidgets.QPushButton(self.page)
        self.pushButton_125.setGeometry(QtCore.QRect(384, 180, 96, 71))
        self.pushButton_125.setObjectName("pushButton_125")
        self.Keyholder.addWidget(self.page)
        self.alpha_backward = QtWidgets.QPushButton(Form)
        self.alpha_backward.setGeometry(QtCore.QRect(240, 0, 121, 71))
        self.alpha_backward.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    border-right: none;\n"
"border-bottom: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}")
        self.alpha_backward.setObjectName("alpha_backward")
        self.alpha_forward = QtWidgets.QPushButton(Form)
        self.alpha_forward.setGeometry(QtCore.QRect(360, 0, 121, 71))
        self.alpha_forward.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    border-right: none;\n"
"border-bottom: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}")
        self.alpha_forward.setObjectName("alpha_forward")
        self.keyborad_text = QtWidgets.QTextEdit(Form)
        self.keyborad_text.setGeometry(QtCore.QRect(0, 0, 241, 71))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.keyborad_text.setFont(font)
        self.keyborad_text.setStyleSheet("#keyborad_text{\n"
"background-color:#000;\n"
"color: rgb(255, 255, 255);\n"
"}")
        self.keyborad_text.setObjectName("keyborad_text")

        self.retranslateUi(Form)
        self.Keyholder.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.btn1.setText(_translate("Form", "q"))
        self.btn2.setText(_translate("Form", "w"))
        self.btn3.setText(_translate("Form", "e"))
        self.btn4.setText(_translate("Form", "r"))
        self.btn5.setText(_translate("Form", "t"))
        self.btn6.setText(_translate("Form", "y"))
        self.btn7.setText(_translate("Form", "u"))
        self.btn8.setText(_translate("Form", "i"))
        self.btn9.setText(_translate("Form", "o"))
        self.btn10.setText(_translate("Form", "p"))
        self.btn11.setText(_translate("Form", "a"))
        self.btn12.setText(_translate("Form", "s"))
        self.btn13.setText(_translate("Form", "d"))
        self.btn14.setText(_translate("Form", "f"))
        self.btn15.setText(_translate("Form", "g"))
        self.btn16.setText(_translate("Form", "h"))
        self.btn17.setText(_translate("Form", "j"))
        self.btn18.setText(_translate("Form", "k"))
        self.btn19.setText(_translate("Form", "l"))
        self.s_backspace.setText(_translate("Form", "|<"))
        self.upperalpha.setText(_translate("Form", "^"))
        self.btn20.setText(_translate("Form", "z"))
        self.btn21.setText(_translate("Form", "x"))
        self.btn22.setText(_translate("Form", "c"))
        self.btn23.setText(_translate("Form", "v"))
        self.btn24.setText(_translate("Form", "b"))
        self.btn25.setText(_translate("Form", "n"))
        self.btn26.setText(_translate("Form", "m"))
        self.alphas_dot.setText(_translate("Form", "."))
        self.alphas_comma.setText(_translate("Form", ","))
        self.numericbutton.setText(_translate("Form", "123"))
        self.sepecialchar.setText(_translate("Form", "@#!"))
        self.alphas_space.setText(_translate("Form", "space"))
        self.alphas_submit.setText(_translate("Form", "Done"))
        self.btn27.setText(_translate("Form", "Q"))
        self.btn28.setText(_translate("Form", "W"))
        self.btn29.setText(_translate("Form", "E"))
        self.btn30.setText(_translate("Form", "R"))
        self.btn31.setText(_translate("Form", "T"))
        self.btn32.setText(_translate("Form", "Y"))
        self.btn33.setText(_translate("Form", "U"))
        self.btn34.setText(_translate("Form", "I"))
        self.btn35.setText(_translate("Form", "O"))
        self.btn36.setText(_translate("Form", "P"))
        self.btn37.setText(_translate("Form", "A"))
        self.btn38.setText(_translate("Form", "S"))
        self.btn39.setText(_translate("Form", "D"))
        self.btn40.setText(_translate("Form", "F"))
        self.btn41.setText(_translate("Form", "G"))
        self.btn42.setText(_translate("Form", "H"))
        self.btn43.setText(_translate("Form", "J"))
        self.btn44.setText(_translate("Form", "K"))
        self.btn45.setText(_translate("Form", "L"))
        self.pushButton_56.setText(_translate("Form", "<"))
        self.alphau_down.setText(_translate("Form", "V"))
        self.btn46.setText(_translate("Form", "Z"))
        self.btn47.setText(_translate("Form", "X"))
        self.btn48.setText(_translate("Form", "C"))
        self.btn49.setText(_translate("Form", "V"))
        self.btn50.setText(_translate("Form", "B"))
        self.btn51.setText(_translate("Form", "N"))
        self.btn52.setText(_translate("Form", "M"))
        self.btn53.setText(_translate("Form", "."))
        self.btn54.setText(_translate("Form", ","))
        self.pushButton_67.setText(_translate("Form", "123"))
        self.pushButton_68.setText(_translate("Form", "@#!"))
        self.pushButton_69.setText(_translate("Form", "Space"))
        self.pushButton_70.setText(_translate("Form", "Done"))
        self.btn55.setText(_translate("Form", "1"))
        self.btn56.setText(_translate("Form", "2"))
        self.btn57.setText(_translate("Form", "3"))
        self.btn65.setText(_translate("Form", "."))
        self.pushButton_75.setText(_translate("Form", "|<"))
        self.btn58.setText(_translate("Form", "4"))
        self.btn59.setText(_translate("Form", "5"))
        self.btn60.setText(_translate("Form", "6"))
        self.btn66.setText(_translate("Form", "*"))
        self.pushButton_80.setText(_translate("Form", "Space"))
        self.btn61.setText(_translate("Form", "7"))
        self.btn62.setText(_translate("Form", "8"))
        self.btn63.setText(_translate("Form", "9"))
        self.btn67.setText(_translate("Form", "+"))
        self.btn69.setText(_translate("Form", ","))
        self.numeric_back.setText(_translate("Form", "Back"))
        self.alphas_special.setText(_translate("Form", "@#!"))
        self.btn64.setText(_translate("Form", "0"))
        self.btn68.setText(_translate("Form", "#"))
        self.pushButton_90.setText(_translate("Form", "Done"))
        self.btn70.setText(_translate("Form", "\""))
        self.btn71.setText(_translate("Form", "\'"))
        self.btn72.setText(_translate("Form", ";"))
        self.btn73.setText(_translate("Form", ":"))
        self.btn74.setText(_translate("Form", "("))
        self.btn75.setText(_translate("Form", ")"))
        self.btn76.setText(_translate("Form", "."))
        self.btn77.setText(_translate("Form", ","))
        self.btn78.setText(_translate("Form", "\\"))
        self.btn79.setText(_translate("Form", "/"))
        self.btn80.setText(_translate("Form", "!"))
        self.btn81.setText(_translate("Form", "@"))
        self.btn82.setText(_translate("Form", "#"))
        self.btn83.setText(_translate("Form", "$"))
        self.btn84.setText(_translate("Form", "{"))
        self.btn85.setText(_translate("Form", "}"))
        self.btn86.setText(_translate("Form", "&&"))
        self.btn87.setText(_translate("Form", "*"))
        self.pushButton_110.setText(_translate("Form", "|<"))
        self.btn88.setText(_translate("Form", "-"))
        self.btn89.setText(_translate("Form", "_"))
        self.btn90.setText(_translate("Form", "+"))
        self.btn91.setText(_translate("Form", "="))
        self.btn92.setText(_translate("Form", "<"))
        self.btn93.setText(_translate("Form", ">"))
        self.btn94.setText(_translate("Form", "?"))
        self.btn95.setText(_translate("Form", "%"))
        self.btn96.setText(_translate("Form", "^"))
        self.btn97.setText(_translate("Form", "|"))
        self.pushButton_120.setText(_translate("Form", "Back"))
        self.pushButton_121.setText(_translate("Form", "123"))
        self.btn98.setText(_translate("Form", "["))
        self.btn99.setText(_translate("Form", "]"))
        self.pushButton_124.setText(_translate("Form", "Space"))
        self.pushButton_125.setText(_translate("Form", "Done"))
        self.alpha_backward.setText(_translate("Form", "<"))
        self.alpha_forward.setText(_translate("Form", ">"))
        self.keyborad_text.setPlaceholderText(_translate("Form", "ENTER TEXT....."))

