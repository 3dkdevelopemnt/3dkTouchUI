# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main_UI.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(546, 359)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.stackedWidget = QtGui.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 551, 361))
        self.stackedWidget.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.0281146, y2:1, stop:0.110184 rgba(47, 130, 255, 255), stop:0.459098 rgba(43, 156, 255, 255), stop:0.979967 rgba(136, 168, 255, 255));"))
        self.stackedWidget.setObjectName(_fromUtf8("stackedWidget"))
        self.SplashScreen = QtGui.QWidget()
        self.SplashScreen.setObjectName(_fromUtf8("SplashScreen"))
        self.widget = QtGui.QWidget(self.SplashScreen)
        self.widget.setGeometry(QtCore.QRect(-10, 0, 561, 361))
        self.widget.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(168, 168, 168, 255), stop:1 rgba(220, 220, 220, 255));"))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.label = QtGui.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(20, 50, 241, 181))
        self.label.setStyleSheet(_fromUtf8("background-color: rgba(255, 255, 255, 0);"))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8("C:/Users/Jithu P G/Downloads/graph-background.png")))
        self.label.setScaledContents(False)
        self.label.setObjectName(_fromUtf8("label"))
        self.stackedWidget.addWidget(self.SplashScreen)
        self.MainWindow_2 = QtGui.QWidget()
        self.MainWindow_2.setObjectName(_fromUtf8("MainWindow_2"))
        self.bed_label = QtGui.QLabel(self.MainWindow_2)
        self.bed_label.setGeometry(QtCore.QRect(200, 30, 71, 71))
        self.bed_label.setStyleSheet(_fromUtf8("background-color: rgba(255, 255, 255, 0);"))
        self.bed_label.setFrameShadow(QtGui.QFrame.Raised)
        self.bed_label.setText(_fromUtf8(""))
        self.bed_label.setPixmap(QtGui.QPixmap(_fromUtf8("../Julia2018AdvancedTouchUI/octoprint_Julia2018AdvancedTouchUI/templates/img/bed.png")))
        self.bed_label.setScaledContents(True)
        self.bed_label.setObjectName(_fromUtf8("bed_label"))
        self.bedprogressbar = QtGui.QProgressBar(self.MainWindow_2)
        self.bedprogressbar.setGeometry(QtCore.QRect(300, 30, 21, 81))
        self.bedprogressbar.setStyleSheet(_fromUtf8("#bedprogressbar{\n"
"\n"
"border-radius:5px;\n"
"background-color:#FFF;\n"
"text-align:center\n"
"}\n"
"#bedprogressbar::chunk{\n"
"background-color: rgb(255, 162, 0);\n"
"border-radius:5px;\n"
"}"))
        self.bedprogressbar.setProperty("value", 24)
        self.bedprogressbar.setOrientation(QtCore.Qt.Vertical)
        self.bedprogressbar.setTextDirection(QtGui.QProgressBar.TopToBottom)
        self.bedprogressbar.setObjectName(_fromUtf8("bedprogressbar"))
        self.Nozile_label = QtGui.QLabel(self.MainWindow_2)
        self.Nozile_label.setGeometry(QtCore.QRect(430, 40, 71, 61))
        self.Nozile_label.setStyleSheet(_fromUtf8("background-color: rgba(255, 255, 255, 0);"))
        self.Nozile_label.setText(_fromUtf8(""))
        self.Nozile_label.setPixmap(QtGui.QPixmap(_fromUtf8("../Julia2018AdvancedTouchUI/octoprint_Julia2018AdvancedTouchUI/templates/img/Nozzle.png")))
        self.Nozile_label.setScaledContents(True)
        self.Nozile_label.setObjectName(_fromUtf8("Nozile_label"))
        self.ntempprogress = QtGui.QProgressBar(self.MainWindow_2)
        self.ntempprogress.setGeometry(QtCore.QRect(400, 30, 21, 81))
        self.ntempprogress.setStyleSheet(_fromUtf8("#ntempprogress{\n"
"\n"
"border-radius:5px;\n"
"background-color:#FFF;\n"
"text-align:center\n"
"}\n"
"#ntempprogress::chunk{\n"
"background-color: rgb(255, 162, 0);\n"
"border-radius:5px;\n"
"}"))
        self.ntempprogress.setProperty("value", 24)
        self.ntempprogress.setOrientation(QtCore.Qt.Vertical)
        self.ntempprogress.setObjectName(_fromUtf8("ntempprogress"))
        self.jobprogress = QtGui.QProgressBar(self.MainWindow_2)
        self.jobprogress.setGeometry(QtCore.QRect(150, 130, 321, 23))
        self.jobprogress.setStyleSheet(_fromUtf8("#jobprogress{\n"
"\n"
"border-radius:10px;\n"
"background-color:#FFF;\n"
"text-align:center\n"
"}\n"
"#jobprogress::chunk{\n"
"background-color: rgb(76, 255, 73);\n"
"\n"
"border-radius: 8px;\n"
"}"))
        self.jobprogress.setProperty("value", 24)
        self.jobprogress.setObjectName(_fromUtf8("jobprogress"))
        self.label_4 = QtGui.QLabel(self.MainWindow_2)
        self.label_4.setGeometry(QtCore.QRect(150, 180, 51, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(_fromUtf8("background-color: rgba(255, 255, 255, 0);\n"
"color:#FFF;"))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.selectedfile = QtGui.QLabel(self.MainWindow_2)
        self.selectedfile.setGeometry(QtCore.QRect(270, 180, 241, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(12)
        self.selectedfile.setFont(font)
        self.selectedfile.setStyleSheet(_fromUtf8("#selectedfile{\n"
"background-color:rgba(225,225,225,0);\n"
"color:#FFF;\n"
"}"))
        self.selectedfile.setObjectName(_fromUtf8("selectedfile"))
        self.label_5 = QtGui.QLabel(self.MainWindow_2)
        self.label_5.setGeometry(QtCore.QRect(150, 210, 101, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(_fromUtf8("background-color: rgba(255, 255, 255, 0);\n"
"color:#FFF;"))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(self.MainWindow_2)
        self.label_6.setGeometry(QtCore.QRect(150, 240, 91, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet(_fromUtf8("background-color: rgba(255, 255, 255, 0);\n"
"color:#FFF;"))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.logo = QtGui.QLabel(self.MainWindow_2)
        self.logo.setGeometry(QtCore.QRect(-50, 50, 241, 181))
        self.logo.setStyleSheet(_fromUtf8("#logo{\n"
"background-color:rgba(225,225,225,0);\n"
"\n"
"}"))
        self.logo.setText(_fromUtf8(""))
        self.logo.setPixmap(QtGui.QPixmap(_fromUtf8("../graph-background.png")))
        self.logo.setScaledContents(True)
        self.logo.setWordWrap(False)
        self.logo.setObjectName(_fromUtf8("logo"))
        self.printtime = QtGui.QLabel(self.MainWindow_2)
        self.printtime.setGeometry(QtCore.QRect(270, 210, 101, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(14)
        self.printtime.setFont(font)
        self.printtime.setStyleSheet(_fromUtf8("#printtime{\n"
"background-color:rgba(225,225,225,0);\n"
"color:#FFF;\n"
"}"))
        self.printtime.setObjectName(_fromUtf8("printtime"))
        self.timeleft = QtGui.QLabel(self.MainWindow_2)
        self.timeleft.setGeometry(QtCore.QRect(270, 240, 101, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(14)
        self.timeleft.setFont(font)
        self.timeleft.setStyleSheet(_fromUtf8("#timeleft{\n"
"background-color:rgba(225,225,225,0);\n"
"color:#FFF;\n"
"}"))
        self.timeleft.setObjectName(_fromUtf8("timeleft"))
        self.testbutton = QtGui.QPushButton(self.MainWindow_2)
        self.testbutton.setGeometry(QtCore.QRect(30, 270, 91, 71))
        self.testbutton.setStyleSheet(_fromUtf8("#testbutton{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:8px;\n"
"}"))
        self.testbutton.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../Julia2018AdvancedTouchUI/octoprint_Julia2018AdvancedTouchUI/templates/img/menu.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.testbutton.setIcon(icon)
        self.testbutton.setIconSize(QtCore.QSize(40, 40))
        self.testbutton.setObjectName(_fromUtf8("testbutton"))
        self.setting = QtGui.QPushButton(self.MainWindow_2)
        self.setting.setGeometry(QtCore.QRect(140, 270, 91, 71))
        self.setting.setStyleSheet(_fromUtf8("#setting{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:8px;\n"
"}"))
        self.setting.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("../Julia2018AdvancedTouchUI/octoprint_Julia2018AdvancedTouchUI/templates/img/settings.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setting.setIcon(icon1)
        self.setting.setIconSize(QtCore.QSize(40, 40))
        self.setting.setObjectName(_fromUtf8("setting"))
        self.play_pause_button = QtGui.QPushButton(self.MainWindow_2)
        self.play_pause_button.setGeometry(QtCore.QRect(250, 270, 91, 71))
        self.play_pause_button.setStyleSheet(_fromUtf8("#play_pause_button{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 8px;\n"
"}"))
        self.play_pause_button.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("../Julia2018AdvancedTouchUI/octoprint_Julia2018AdvancedTouchUI/templates/img/play.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.play_pause_button.setIcon(icon2)
        self.play_pause_button.setIconSize(QtCore.QSize(40, 40))
        self.play_pause_button.setObjectName(_fromUtf8("play_pause_button"))
        self.stop = QtGui.QPushButton(self.MainWindow_2)
        self.stop.setGeometry(QtCore.QRect(360, 270, 91, 71))
        self.stop.setStyleSheet(_fromUtf8("#stop{\n"
"background-color:rgb(255,255,255);\n"
"border-radius:8px;\n"
"}"))
        self.stop.setText(_fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("../Julia2018AdvancedTouchUI/octoprint_Julia2018AdvancedTouchUI/templates/img/stop.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.stop.setIcon(icon3)
        self.stop.setIconSize(QtCore.QSize(40, 40))
        self.stop.setObjectName(_fromUtf8("stop"))
        self.stackedWidget.addWidget(self.MainWindow_2)
        self.Menupage = QtGui.QWidget()
        self.Menupage.setObjectName(_fromUtf8("Menupage"))
        self.print_button = QtGui.QToolButton(self.Menupage)
        self.print_button.setGeometry(QtCore.QRect(0, 0, 191, 171))
        self.print_button.setStyleSheet(_fromUtf8("#print_button{\n"
"border-color: rgb(255, 184, 42);\n"
"background-color: rgb(255, 255, 255);\n"
"}"))
        self.print_button.setText(_fromUtf8(""))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8("../Julia2018AdvancedTouchUI/octoprint_Julia2018AdvancedTouchUI/templates/img/printer.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.print_button.setIcon(icon4)
        self.print_button.setIconSize(QtCore.QSize(120, 120))
        self.print_button.setObjectName(_fromUtf8("print_button"))
        self.control_button = QtGui.QToolButton(self.Menupage)
        self.control_button.setGeometry(QtCore.QRect(190, 0, 181, 171))
        self.control_button.setStyleSheet(_fromUtf8("#control_button{\n"
"background-color:rgb(255,255,255);\n"
"}"))
        self.control_button.setText(_fromUtf8(""))
        self.control_button.setIcon(icon1)
        self.control_button.setIconSize(QtCore.QSize(120, 120))
        self.control_button.setObjectName(_fromUtf8("control_button"))
        self.calibrate_button = QtGui.QToolButton(self.Menupage)
        self.calibrate_button.setGeometry(QtCore.QRect(370, 0, 181, 171))
        self.calibrate_button.setStyleSheet(_fromUtf8("#calibrate_button{\n"
"background-color:rgb(255,255,255);\n"
"\n"
"}"))
        self.calibrate_button.setText(_fromUtf8(""))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8("../Julia2018AdvancedTouchUI/octoprint_Julia2018AdvancedTouchUI/templates/img/reload.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.calibrate_button.setIcon(icon5)
        self.calibrate_button.setIconSize(QtCore.QSize(120, 120))
        self.calibrate_button.setObjectName(_fromUtf8("calibrate_button"))
        self.cart_button = QtGui.QToolButton(self.Menupage)
        self.cart_button.setGeometry(QtCore.QRect(0, 170, 191, 191))
        self.cart_button.setStyleSheet(_fromUtf8("#cart_button{\n"
"background-color:rgb(255,255,255);\n"
"}"))
        self.cart_button.setText(_fromUtf8(""))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8("../Julia2018AdvancedTouchUI/octoprint_Julia2018AdvancedTouchUI/templates/img/cart.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cart_button.setIcon(icon6)
        self.cart_button.setIconSize(QtCore.QSize(120, 120))
        self.cart_button.setObjectName(_fromUtf8("cart_button"))
        self.settings_button = QtGui.QToolButton(self.Menupage)
        self.settings_button.setGeometry(QtCore.QRect(190, 170, 181, 191))
        self.settings_button.setStyleSheet(_fromUtf8("#settings_button{\n"
"background-color:rgb(255,255,255);\n"
"}\n"
""))
        self.settings_button.setText(_fromUtf8(""))
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8("../Julia2018AdvancedTouchUI/octoprint_Julia2018AdvancedTouchUI/templates/img/settings-1.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.settings_button.setIcon(icon7)
        self.settings_button.setIconSize(QtCore.QSize(120, 120))
        self.settings_button.setObjectName(_fromUtf8("settings_button"))
        self.Mback_button = QtGui.QToolButton(self.Menupage)
        self.Mback_button.setGeometry(QtCore.QRect(370, 170, 181, 191))
        self.Mback_button.setStyleSheet(_fromUtf8("#Mback_button{\n"
"background-color: rgb(255,255,255);\n"
"}"))
        self.Mback_button.setText(_fromUtf8(""))
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8("../Julia2018AdvancedTouchUI/octoprint_Julia2018AdvancedTouchUI/templates/img/back.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Mback_button.setIcon(icon8)
        self.Mback_button.setIconSize(QtCore.QSize(120, 120))
        self.Mback_button.setObjectName(_fromUtf8("Mback_button"))
        self.stackedWidget.addWidget(self.Menupage)
        self.WifiSettingPage = QtGui.QWidget()
        self.WifiSettingPage.setObjectName(_fromUtf8("WifiSettingPage"))
        self.SSidlabel = QtGui.QLabel(self.WifiSettingPage)
        self.SSidlabel.setGeometry(QtCore.QRect(30, 60, 111, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(16)
        self.SSidlabel.setFont(font)
        self.SSidlabel.setStyleSheet(_fromUtf8("#SSidlabel{\n"
"background-color:rgba(255,255,255,0);\n"
"color:#FFF;\n"
"\n"
"}"))
        self.SSidlabel.setObjectName(_fromUtf8("SSidlabel"))
        self.wifidonebutton = QtGui.QPushButton(self.WifiSettingPage)
        self.wifidonebutton.setGeometry(QtCore.QRect(100, 250, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.wifidonebutton.setFont(font)
        self.wifidonebutton.setStyleSheet(_fromUtf8("#wifidonebutton{\n"
"background-color:rgb(255,255,255);\n"
"border-radius:5px;\n"
"}"))
        self.wifidonebutton.setObjectName(_fromUtf8("wifidonebutton"))
        self.wificancelbutton = QtGui.QPushButton(self.WifiSettingPage)
        self.wificancelbutton.setGeometry(QtCore.QRect(290, 250, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.wificancelbutton.setFont(font)
        self.wificancelbutton.setStyleSheet(_fromUtf8("#wificancelbutton{\n"
"background-color:rgb(255,255,255);\n"
"border-radius:5px;\n"
"}"))
        self.wificancelbutton.setObjectName(_fromUtf8("wificancelbutton"))
        self.ssidtext = QtGui.QLineEdit(self.WifiSettingPage)
        self.ssidtext.setGeometry(QtCore.QRect(170, 50, 331, 41))
        self.ssidtext.setStyleSheet(_fromUtf8("#ssidtext{\n"
"background-color:rgb(255,255,255);\n"
"border-radius:5px;\n"
"}\n"
""))
        self.ssidtext.setObjectName(_fromUtf8("ssidtext"))
        self.PasswordLabel = QtGui.QLabel(self.WifiSettingPage)
        self.PasswordLabel.setGeometry(QtCore.QRect(30, 110, 91, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(16)
        self.PasswordLabel.setFont(font)
        self.PasswordLabel.setStyleSheet(_fromUtf8("#PasswordLabel{\n"
"background-color:rgba(255,255,255,0);\n"
"color :#FFF;\n"
"}\n"
""))
        self.PasswordLabel.setObjectName(_fromUtf8("PasswordLabel"))
        self.wifipassword = QtGui.QLineEdit(self.WifiSettingPage)
        self.wifipassword.setGeometry(QtCore.QRect(170, 110, 331, 41))
        self.wifipassword.setStyleSheet(_fromUtf8("#wifipassword{\n"
"background-color:rgb(255,255,255);\n"
"border-radius:5px;\n"
"}"))
        self.wifipassword.setObjectName(_fromUtf8("wifipassword"))
        self.stackedWidget.addWidget(self.WifiSettingPage)
        self.select_file = QtGui.QWidget()
        self.select_file.setObjectName(_fromUtf8("select_file"))
        self.v_scroll_up = QtGui.QToolButton(self.select_file)
        self.v_scroll_up.setGeometry(QtCore.QRect(410, 0, 141, 91))
        self.v_scroll_up.setStyleSheet(_fromUtf8("#v_scroll_up{\n"
"\n"
"background-color:rgb(255,255,255);\n"
"border:1px solid black;\n"
"\n"
"\n"
"}\n"
""))
        self.v_scroll_up.setObjectName(_fromUtf8("v_scroll_up"))
        self.file_select = QtGui.QToolButton(self.select_file)
        self.file_select.setGeometry(QtCore.QRect(410, 91, 141, 91))
        self.file_select.setStyleSheet(_fromUtf8("#file_select{\n"
"background-color: rgb(255, 255, 255);\n"
"border:1px solid black;\n"
"}\n"
""))
        self.file_select.setObjectName(_fromUtf8("file_select"))
        self.v_scroll_down = QtGui.QToolButton(self.select_file)
        self.v_scroll_down.setGeometry(QtCore.QRect(410, 180, 141, 101))
        self.v_scroll_down.setStyleSheet(_fromUtf8("#v_scroll_down{\n"
"background-color:rgb(255,255,255);\n"
"border:1px solid black;\n"
"}\n"
""))
        self.v_scroll_down.setObjectName(_fromUtf8("v_scroll_down"))
        self.print_list_back = QtGui.QToolButton(self.select_file)
        self.print_list_back.setGeometry(QtCore.QRect(410, 280, 141, 81))
        self.print_list_back.setStyleSheet(_fromUtf8("#print_list_back{\n"
"background-color:rgb(255,255,255);\n"
"border:1px solid black;\n"
"}\n"
""))
        self.print_list_back.setObjectName(_fromUtf8("print_list_back"))
        self.print_list = QtGui.QListWidget(self.select_file)
        self.print_list.setGeometry(QtCore.QRect(0, 0, 411, 361))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(20)
        self.print_list.setFont(font)
        self.print_list.setStyleSheet(_fromUtf8("#print_list{\n"
"\n"
"background-color:rgb(255,255,255);\n"
"border:1px solid black;\n"
"\n"
"\n"
"}\n"
""))
        self.print_list.setObjectName(_fromUtf8("print_list"))
        self.stackedWidget.addWidget(self.select_file)
        self.page = QtGui.QWidget()
        self.page.setObjectName(_fromUtf8("page"))
        self.sub_select_button = QtGui.QToolButton(self.page)
        self.sub_select_button.setGeometry(QtCore.QRect(0, 250, 191, 111))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.sub_select_button.setFont(font)
        self.sub_select_button.setObjectName(_fromUtf8("sub_select_button"))
        self.local_select_button = QtGui.QToolButton(self.page)
        self.local_select_button.setGeometry(QtCore.QRect(190, 250, 191, 111))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.local_select_button.setFont(font)
        self.local_select_button.setObjectName(_fromUtf8("local_select_button"))
        self.print_select_back_button = QtGui.QToolButton(self.page)
        self.print_select_back_button.setGeometry(QtCore.QRect(380, 250, 171, 111))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.print_select_back_button.setFont(font)
        self.print_select_back_button.setObjectName(_fromUtf8("print_select_back_button"))
        self.label_2 = QtGui.QLabel(self.page)
        self.label_2.setGeometry(QtCore.QRect(2, 0, 551, 251))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtGui.QWidget()
        self.page_2.setObjectName(_fromUtf8("page_2"))
        self.listWidget = QtGui.QListWidget(self.page_2)
        self.listWidget.setGeometry(QtCore.QRect(0, 0, 431, 361))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.toolButton = QtGui.QToolButton(self.page_2)
        self.toolButton.setGeometry(QtCore.QRect(430, 0, 121, 141))
        self.toolButton.setObjectName(_fromUtf8("toolButton"))
        self.stackedWidget.addWidget(self.page_2)
        self.settingpage = QtGui.QWidget()
        self.settingpage.setObjectName(_fromUtf8("settingpage"))
        self.toolButton_2 = QtGui.QToolButton(self.settingpage)
        self.toolButton_2.setGeometry(QtCore.QRect(0, 0, 551, 101))
        self.toolButton_2.setObjectName(_fromUtf8("toolButton_2"))
        self.toolButton_3 = QtGui.QToolButton(self.settingpage)
        self.toolButton_3.setGeometry(QtCore.QRect(0, 100, 551, 111))
        self.toolButton_3.setObjectName(_fromUtf8("toolButton_3"))
        self.stackedWidget.addWidget(self.settingpage)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label_4.setText(_translate("MainWindow", "File  :", None))
        self.selectedfile.setText(_translate("MainWindow", "test.gcode", None))
        self.label_5.setText(_translate("MainWindow", "Print Time :", None))
        self.label_6.setText(_translate("MainWindow", "Time Left  :", None))
        self.printtime.setText(_translate("MainWindow", "0 : 0 : 0", None))
        self.timeleft.setText(_translate("MainWindow", "0 : 0 : 0", None))
        self.SSidlabel.setText(_translate("MainWindow", "Enter SSID", None))
        self.wifidonebutton.setText(_translate("MainWindow", "Connect", None))
        self.wificancelbutton.setText(_translate("MainWindow", "Cancel", None))
        self.PasswordLabel.setText(_translate("MainWindow", "Password", None))
        self.v_scroll_up.setText(_translate("MainWindow", "^", None))
        self.file_select.setText(_translate("MainWindow", "OK", None))
        self.v_scroll_down.setText(_translate("MainWindow", "V", None))
        self.print_list_back.setText(_translate("MainWindow", "Back", None))
        self.sub_select_button.setText(_translate("MainWindow", "USB", None))
        self.local_select_button.setText(_translate("MainWindow", "Local", None))
        self.print_select_back_button.setText(_translate("MainWindow", "Back", None))
        self.label_2.setText(_translate("MainWindow", "Print From :", None))
        self.toolButton.setText(_translate("MainWindow", "...", None))
        self.toolButton_2.setText(_translate("MainWindow", "NETWORK SETTING", None))
        self.toolButton_3.setText(_translate("MainWindow", "VERSION", None))

