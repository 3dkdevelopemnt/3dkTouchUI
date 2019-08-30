# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main_UI.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(550, 359)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 551, 361))
        self.stackedWidget.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.0281146, y2:1, stop:0.110184 rgba(47, 130, 255, 255), stop:0.459098 rgba(43, 156, 255, 255), stop:0.979967 rgba(136, 168, 255, 255));")
        self.stackedWidget.setObjectName("stackedWidget")
        self.SplashScreen = QtWidgets.QWidget()
        self.SplashScreen.setObjectName("SplashScreen")
        self.widget = QtWidgets.QWidget(self.SplashScreen)
        self.widget.setGeometry(QtCore.QRect(-10, 0, 561, 361))
        self.widget.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(168, 168, 168, 255), stop:1 rgba(220, 220, 220, 255));")
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(20, 50, 241, 181))
        self.label.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("C:/Users/Jithu P G/Downloads/graph-background.png"))
        self.label.setScaledContents(False)
        self.label.setObjectName("label")
        self.stackedWidget.addWidget(self.SplashScreen)
        self.MainWindow_2 = QtWidgets.QWidget()
        self.MainWindow_2.setObjectName("MainWindow_2")
        self.bed_label = QtWidgets.QLabel(self.MainWindow_2)
        self.bed_label.setGeometry(QtCore.QRect(200, 30, 71, 71))
        self.bed_label.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.bed_label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bed_label.setText("")
        self.bed_label.setPixmap(QtGui.QPixmap("../Julia2018AdvancedTouchUI/octoprint_Julia2018AdvancedTouchUI/templates/img/bed.png"))
        self.bed_label.setScaledContents(True)
        self.bed_label.setObjectName("bed_label")
        self.bedprogressbar = QtWidgets.QProgressBar(self.MainWindow_2)
        self.bedprogressbar.setGeometry(QtCore.QRect(300, 30, 21, 81))
        self.bedprogressbar.setStyleSheet("#bedprogressbar{\n"
"\n"
"border-radius:5px;\n"
"background-color:#FFF;\n"
"text-align:center\n"
"}\n"
"#bedprogressbar::chunk{\n"
"background-color: rgb(255, 162, 0);\n"
"border-radius:5px;\n"
"}")
        self.bedprogressbar.setProperty("value", 24)
        self.bedprogressbar.setOrientation(QtCore.Qt.Vertical)
        self.bedprogressbar.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.bedprogressbar.setObjectName("bedprogressbar")
        self.Nozile_label = QtWidgets.QLabel(self.MainWindow_2)
        self.Nozile_label.setGeometry(QtCore.QRect(430, 40, 71, 61))
        self.Nozile_label.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.Nozile_label.setText("")
        self.Nozile_label.setPixmap(QtGui.QPixmap("../Julia2018AdvancedTouchUI/octoprint_Julia2018AdvancedTouchUI/templates/img/Nozzle.png"))
        self.Nozile_label.setScaledContents(True)
        self.Nozile_label.setObjectName("Nozile_label")
        self.ntempprogress = QtWidgets.QProgressBar(self.MainWindow_2)
        self.ntempprogress.setGeometry(QtCore.QRect(400, 30, 21, 81))
        self.ntempprogress.setStyleSheet("#ntempprogress{\n"
"\n"
"border-radius:5px;\n"
"background-color:#FFF;\n"
"text-align:center\n"
"}\n"
"#ntempprogress::chunk{\n"
"background-color: rgb(255, 162, 0);\n"
"border-radius:5px;\n"
"}")
        self.ntempprogress.setProperty("value", 24)
        self.ntempprogress.setOrientation(QtCore.Qt.Vertical)
        self.ntempprogress.setObjectName("ntempprogress")
        self.jobprogress = QtWidgets.QProgressBar(self.MainWindow_2)
        self.jobprogress.setGeometry(QtCore.QRect(150, 130, 321, 23))
        self.jobprogress.setStyleSheet("#jobprogress{\n"
"\n"
"border-radius:10px;\n"
"background-color:#FFF;\n"
"text-align:center\n"
"}\n"
"#jobprogress::chunk{\n"
"background-color: rgb(76, 255, 73);\n"
"\n"
"border-radius: 8px;\n"
"}")
        self.jobprogress.setProperty("value", 24)
        self.jobprogress.setObjectName("jobprogress")
        self.label_4 = QtWidgets.QLabel(self.MainWindow_2)
        self.label_4.setGeometry(QtCore.QRect(150, 180, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color:#FFF;")
        self.label_4.setObjectName("label_4")
        self.selectedfile = QtWidgets.QLabel(self.MainWindow_2)
        self.selectedfile.setGeometry(QtCore.QRect(270, 180, 241, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.selectedfile.setFont(font)
        self.selectedfile.setStyleSheet("#selectedfile{\n"
"background-color:rgba(225,225,225,0);\n"
"color:#FFF;\n"
"}")
        self.selectedfile.setObjectName("selectedfile")
        self.label_5 = QtWidgets.QLabel(self.MainWindow_2)
        self.label_5.setGeometry(QtCore.QRect(150, 210, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color:#FFF;")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.MainWindow_2)
        self.label_6.setGeometry(QtCore.QRect(150, 240, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color:#FFF;")
        self.label_6.setObjectName("label_6")
        self.logo = QtWidgets.QLabel(self.MainWindow_2)
        self.logo.setGeometry(QtCore.QRect(-50, 50, 241, 181))
        self.logo.setStyleSheet("#logo{\n"
"background-color:rgba(225,225,225,0);\n"
"\n"
"}")
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("C:/Users/Jithu P G/Downloads/graph-background.png"))
        self.logo.setScaledContents(True)
        self.logo.setWordWrap(False)
        self.logo.setObjectName("logo")
        self.printtime = QtWidgets.QLabel(self.MainWindow_2)
        self.printtime.setGeometry(QtCore.QRect(270, 210, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.printtime.setFont(font)
        self.printtime.setStyleSheet("#printtime{\n"
"background-color:rgba(225,225,225,0);\n"
"color:#FFF;\n"
"}")
        self.printtime.setObjectName("printtime")
        self.timeleft = QtWidgets.QLabel(self.MainWindow_2)
        self.timeleft.setGeometry(QtCore.QRect(270, 240, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.timeleft.setFont(font)
        self.timeleft.setStyleSheet("#timeleft{\n"
"background-color:rgba(225,225,225,0);\n"
"color:#FFF;\n"
"}")
        self.timeleft.setObjectName("timeleft")
        self.testbutton = QtWidgets.QPushButton(self.MainWindow_2)
        self.testbutton.setGeometry(QtCore.QRect(30, 270, 91, 71))
        self.testbutton.setStyleSheet("#testbutton{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:8px;\n"
"}")
        self.testbutton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Julia2018AdvancedTouchUI/octoprint_Julia2018AdvancedTouchUI/templates/img/menu.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.testbutton.setIcon(icon)
        self.testbutton.setIconSize(QtCore.QSize(40, 40))
        self.testbutton.setObjectName("testbutton")
        self.setting = QtWidgets.QPushButton(self.MainWindow_2)
        self.setting.setGeometry(QtCore.QRect(140, 270, 91, 71))
        self.setting.setStyleSheet("#setting{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:8px;\n"
"}")
        self.setting.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../Julia2018AdvancedTouchUI/octoprint_Julia2018AdvancedTouchUI/templates/img/settings.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setting.setIcon(icon1)
        self.setting.setIconSize(QtCore.QSize(40, 40))
        self.setting.setObjectName("setting")
        self.play_pause_button = QtWidgets.QPushButton(self.MainWindow_2)
        self.play_pause_button.setGeometry(QtCore.QRect(250, 270, 91, 71))
        self.play_pause_button.setStyleSheet("#play_pause_button{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 8px;\n"
"}")
        self.play_pause_button.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../Julia2018AdvancedTouchUI/octoprint_Julia2018AdvancedTouchUI/templates/img/play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.play_pause_button.setIcon(icon2)
        self.play_pause_button.setIconSize(QtCore.QSize(40, 40))
        self.play_pause_button.setObjectName("play_pause_button")
        self.stop = QtWidgets.QPushButton(self.MainWindow_2)
        self.stop.setGeometry(QtCore.QRect(360, 270, 91, 71))
        self.stop.setStyleSheet("#stop{\n"
"background-color:rgb(255,255,255);\n"
"border-radius:8px;\n"
"}")
        self.stop.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../Julia2018AdvancedTouchUI/octoprint_Julia2018AdvancedTouchUI/templates/img/stop.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.stop.setIcon(icon3)
        self.stop.setIconSize(QtCore.QSize(40, 40))
        self.stop.setObjectName("stop")
        self.stackedWidget.addWidget(self.MainWindow_2)
        self.Menupage = QtWidgets.QWidget()
        self.Menupage.setObjectName("Menupage")
        self.print_button = QtWidgets.QToolButton(self.Menupage)
        self.print_button.setGeometry(QtCore.QRect(0, 0, 191, 171))
        self.print_button.setStyleSheet("#print_button{\n"
"border-color: rgb(255, 184, 42);\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.print_button.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../Julia2018AdvancedTouchUI/octoprint_Julia2018AdvancedTouchUI/templates/img/printer.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.print_button.setIcon(icon4)
        self.print_button.setIconSize(QtCore.QSize(120, 120))
        self.print_button.setObjectName("print_button")
        self.control_button = QtWidgets.QToolButton(self.Menupage)
        self.control_button.setGeometry(QtCore.QRect(190, 0, 181, 171))
        self.control_button.setStyleSheet("#control_button{\n"
"background-color:rgb(255,255,255);\n"
"}")
        self.control_button.setText("")
        self.control_button.setIcon(icon1)
        self.control_button.setIconSize(QtCore.QSize(120, 120))
        self.control_button.setObjectName("control_button")
        self.calibrate_button = QtWidgets.QToolButton(self.Menupage)
        self.calibrate_button.setGeometry(QtCore.QRect(370, 0, 181, 171))
        self.calibrate_button.setStyleSheet("#calibrate_button{\n"
"background-color:rgb(255,255,255);\n"
"\n"
"}")
        self.calibrate_button.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("../Julia2018AdvancedTouchUI/octoprint_Julia2018AdvancedTouchUI/templates/img/reload.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.calibrate_button.setIcon(icon5)
        self.calibrate_button.setIconSize(QtCore.QSize(120, 120))
        self.calibrate_button.setObjectName("calibrate_button")
        self.cart_button = QtWidgets.QToolButton(self.Menupage)
        self.cart_button.setGeometry(QtCore.QRect(0, 170, 191, 191))
        self.cart_button.setStyleSheet("#cart_button{\n"
"background-color:rgb(255,255,255);\n"
"}")
        self.cart_button.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("../Julia2018AdvancedTouchUI/octoprint_Julia2018AdvancedTouchUI/templates/img/cart.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cart_button.setIcon(icon6)
        self.cart_button.setIconSize(QtCore.QSize(120, 120))
        self.cart_button.setObjectName("cart_button")
        self.settings_button = QtWidgets.QToolButton(self.Menupage)
        self.settings_button.setGeometry(QtCore.QRect(190, 170, 181, 191))
        self.settings_button.setStyleSheet("#settings_button{\n"
"background-color:rgb(255,255,255);\n"
"}\n"
"")
        self.settings_button.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("../Julia2018AdvancedTouchUI/octoprint_Julia2018AdvancedTouchUI/templates/img/settings-1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.settings_button.setIcon(icon7)
        self.settings_button.setIconSize(QtCore.QSize(120, 120))
        self.settings_button.setObjectName("settings_button")
        self.Mback_button = QtWidgets.QToolButton(self.Menupage)
        self.Mback_button.setGeometry(QtCore.QRect(370, 170, 181, 191))
        self.Mback_button.setStyleSheet("#Mback_button{\n"
"background-color: rgb(255,255,255);\n"
"}")
        self.Mback_button.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("../Julia2018AdvancedTouchUI/octoprint_Julia2018AdvancedTouchUI/templates/img/back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Mback_button.setIcon(icon8)
        self.Mback_button.setIconSize(QtCore.QSize(120, 120))
        self.Mback_button.setObjectName("Mback_button")
        self.stackedWidget.addWidget(self.Menupage)
        self.WifiSettingPage = QtWidgets.QWidget()
        self.WifiSettingPage.setObjectName("WifiSettingPage")
        self.SSidlabel = QtWidgets.QLabel(self.WifiSettingPage)
        self.SSidlabel.setGeometry(QtCore.QRect(30, 60, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.SSidlabel.setFont(font)
        self.SSidlabel.setStyleSheet("#SSidlabel{\n"
"background-color:rgba(255,255,255,0);\n"
"color:#FFF;\n"
"\n"
"}")
        self.SSidlabel.setObjectName("SSidlabel")
        self.wifidonebutton = QtWidgets.QPushButton(self.WifiSettingPage)
        self.wifidonebutton.setGeometry(QtCore.QRect(100, 250, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.wifidonebutton.setFont(font)
        self.wifidonebutton.setStyleSheet("#wifidonebutton{\n"
"background-color:rgb(255,255,255);\n"
"border-radius:5px;\n"
"}")
        self.wifidonebutton.setObjectName("wifidonebutton")
        self.wificancelbutton = QtWidgets.QPushButton(self.WifiSettingPage)
        self.wificancelbutton.setGeometry(QtCore.QRect(290, 250, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.wificancelbutton.setFont(font)
        self.wificancelbutton.setStyleSheet("#wificancelbutton{\n"
"background-color:rgb(255,255,255);\n"
"border-radius:5px;\n"
"}")
        self.wificancelbutton.setObjectName("wificancelbutton")
        self.ssidtext = QtWidgets.QLineEdit(self.WifiSettingPage)
        self.ssidtext.setGeometry(QtCore.QRect(170, 50, 331, 41))
        self.ssidtext.setStyleSheet("#ssidtext{\n"
"background-color:rgb(255,255,255);\n"
"border-radius:5px;\n"
"}\n"
"")
        self.ssidtext.setObjectName("ssidtext")
        self.PasswordLabel = QtWidgets.QLabel(self.WifiSettingPage)
        self.PasswordLabel.setGeometry(QtCore.QRect(30, 110, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.PasswordLabel.setFont(font)
        self.PasswordLabel.setStyleSheet("#PasswordLabel{\n"
"background-color:rgba(255,255,255,0);\n"
"color :#FFF;\n"
"}\n"
"")
        self.PasswordLabel.setObjectName("PasswordLabel")
        self.wifipassword = QtWidgets.QLineEdit(self.WifiSettingPage)
        self.wifipassword.setGeometry(QtCore.QRect(170, 110, 331, 41))
        self.wifipassword.setStyleSheet("#wifipassword{\n"
"background-color:rgb(255,255,255);\n"
"border-radius:5px;\n"
"}")
        self.wifipassword.setObjectName("wifipassword")
        self.stackedWidget.addWidget(self.WifiSettingPage)
        self.select_file = QtWidgets.QWidget()
        self.select_file.setObjectName("select_file")
        self.v_scroll_up = QtWidgets.QToolButton(self.select_file)
        self.v_scroll_up.setGeometry(QtCore.QRect(410, 0, 141, 91))
        self.v_scroll_up.setStyleSheet("#v_scroll_up{\n"
"\n"
"background-color:rgb(255,255,255);\n"
"border:1px solid black;\n"
"\n"
"\n"
"}\n"
"")
        self.v_scroll_up.setObjectName("v_scroll_up")
        self.file_select = QtWidgets.QToolButton(self.select_file)
        self.file_select.setGeometry(QtCore.QRect(410, 91, 141, 91))
        self.file_select.setStyleSheet("#file_select{\n"
"background-color: rgb(255, 255, 255);\n"
"border:1px solid black;\n"
"}\n"
"")
        self.file_select.setObjectName("file_select")
        self.v_scroll_down = QtWidgets.QToolButton(self.select_file)
        self.v_scroll_down.setGeometry(QtCore.QRect(410, 180, 141, 101))
        self.v_scroll_down.setStyleSheet("#v_scroll_down{\n"
"background-color:rgb(255,255,255);\n"
"border:1px solid black;\n"
"}\n"
"")
        self.v_scroll_down.setObjectName("v_scroll_down")
        self.print_list_back = QtWidgets.QToolButton(self.select_file)
        self.print_list_back.setGeometry(QtCore.QRect(410, 280, 141, 81))
        self.print_list_back.setStyleSheet("#print_list_back{\n"
"background-color:rgb(255,255,255);\n"
"border:1px solid black;\n"
"}\n"
"")
        self.print_list_back.setObjectName("print_list_back")
        self.print_list = QtWidgets.QListWidget(self.select_file)
        self.print_list.setGeometry(QtCore.QRect(0, 0, 411, 361))
        self.print_list.setStyleSheet("#print_list{\n"
"\n"
"background-color:rgb(255,255,255);\n"
"border:1px solid black;\n"
"\n"
"\n"
"}\n"
"")
        self.print_list.setObjectName("print_list")
        self.stackedWidget.addWidget(self.select_file)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(4)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_4.setText(_translate("MainWindow", "File  :"))
        self.selectedfile.setText(_translate("MainWindow", "test.gcode"))
        self.label_5.setText(_translate("MainWindow", "Print Time :"))
        self.label_6.setText(_translate("MainWindow", "Time Left  :"))
        self.printtime.setText(_translate("MainWindow", "0 : 0 : 0"))
        self.timeleft.setText(_translate("MainWindow", "0 : 0 : 0"))
        self.SSidlabel.setText(_translate("MainWindow", "Enter SSID"))
        self.wifidonebutton.setText(_translate("MainWindow", "Connect"))
        self.wificancelbutton.setText(_translate("MainWindow", "Cancel"))
        self.PasswordLabel.setText(_translate("MainWindow", "Password"))
        self.v_scroll_up.setText(_translate("MainWindow", "^"))
        self.file_select.setText(_translate("MainWindow", "OK"))
        self.v_scroll_down.setText(_translate("MainWindow", "V"))
        self.print_list_back.setText(_translate("MainWindow", "Back"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

