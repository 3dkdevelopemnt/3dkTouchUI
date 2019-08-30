from Main_UI import Ui_MainWindow
import sys
from PyQt5 import QtWidgets,QtCore,QtGui,QtTest
from PyQt5.QtWidgets import QMessageBox
import time
from Api import octoprint_api


import time  as Stimer

import keyboard
import webbrowser 

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        self._hour=0
        self._minute=0
        self._second=0

        self.print_file=None
        self.prev_data=[]
        super(MainWindow,self).__init__()
        self.api=octoprint_api()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.timmer=QtCore.QTimer()
        self.timmer.timeout.connect(self.Job_Progress_Crawler)
        #self.timmer.start(2000)
        self.Auto_Connect()
        #self.api.connect_printer()
        self.ui.stackedWidget.setCurrentIndex(0)
        time.sleep(1)
        self.ui.stackedWidget.setCurrentIndex(1)
        self.ui.testbutton.clicked.connect(self.menupage)
        self.ui.setting.clicked.connect(self.startkeyborad)
        self.ui.Mback_button.clicked.connect(self.Home_page)
        self.ui.print_button.clicked.connect(self.List_files)
        self.ui.file_select.clicked.connect(self.start_print)
        self.ui.print_list.currentItemChanged.connect(self.selected_file)
        self.ui.print_list_back.clicked.connect(self.Home_page)
        self.ui.jobprogress.setValue(50)
        self.ui.stop.clicked.connect(self.stop_print)
        self.ui.setting.clicked.connect(self.show_keyboard)
        self.ui.cart_button.clicked.connect(self.web_view)

    def menupage(self):
        self.ui.stackedWidget.setCurrentIndex(2)

    def startkeyborad(self, returnFn, onlyNumeric=False, noSpace=False, text=""):
        #keyBoardobj = keyboard.Keyboard(onlyNumeric=onlyNumeric, noSpace=noSpace, text=text)
        #self.connect(keyBoardobj, QtCore.SIGNAL('KEYBOARD'), returnFn)
        #keyBoardobj.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        #keyBoardobj.show()
        pass

    def Home_page(self):
        self.ui.stackedWidget.setCurrentIndex(1)
    
    """
    This function Auto connect The printer by sacnning the ports

    """
    def Auto_Connect(self):
        print("Autoconnect is called!")
        time.sleep(1)
        
        self.api.connect_printer()
        # msg=QMessageBox()
        # msg.setWindowTitle("Connection Error")
        # msg.setText("Printer Connection Failed . make user printer is connected!")
        # msg.setStandardButtons(QMessageBox.Ok)
        # msg.show()
        pass

    """
    List Files : List all the available file in the local directory !
    """


    def List_files(self):
        self.ui.stackedWidget.setCurrentIndex(4)
        data=self.api.List_all_files()
        try:
            #count=self.ui.print_list.count()
            if data!=self.prev_data:
                self.ui.print_list.addItems(data)
                self.prev_data=data

        except:
            # msg=QMessageBox()
            # msg.setWindowTitle("file list error")
            # msg.setText("Caonnot list the files")
            # msg.setStandardButtons(QMessageBox.Ok)
            # msg.show()
            pass

    def selected_file(self):
        print("selected file",self.ui.print_list.count)
        self.print_file=self.ui.print_list.currentItem().text()
        print(self.ui.print_list.currentItem().text())
        
    def start_print(self):
        self.api.select_file(self.print_file)
        self.ui.selectedfile.setText(self.print_file)
        self.api.job_details()
        self.ui.stackedWidget.setCurrentIndex(1)
        # status=self.api.connect_printer()
        # if  not status:
        #     try:
        #         if status[0]=="error":

        #             print("error"+status[2])
        #             msg=QtWidgets.QMessageBox.about(self,status[1],status[2])
                    #msg.showMessage()
                    # msg.exec_()
            # except Exception as e:
                #just ignore the Error right now 
                # pass

        #self.api.startprint()
        self.ui.jobprogress.setValue(0)
        #self.api.startprint()
        self.timmer.start()


    def stop_print(self):
        self.timmer.stop()
        self._hour=0
        self._minute=0
        self._second=0
        print("printing halted")

    #######################################################
    #
    #++++++++++++++Setting up the tool/Nozile tempratuer
    #
    #######################################################


    def setToolTemp(self):
        self.api.Set_Tool_Temp()

    def Job_Progress_Crawler(self):
        QtTest.QTest.qWait(1000)
        #print(self._hour,":",self._minute,":",self._second)
        text=str(self._hour)+" : "+str(self._minute)+" : "+str(self._second)
        self.ui.printtime.setText(text)

        self._second+=1
        if (self._second==60):
            self._second=0
            self._minute+=1
            self.ui.jobprogress.setValue(self._minute)
        if (self._minute==60):
            self._minute=0
            self._hour+=1

        
    def show_keyboard(self):
        keyobj=keyboard.Keyboard_3DK()
        data=keyobj.exec_()
        #print(keyobj.con)
        self.ui.selectedfile.setText(keyobj.con)
    
    
    def web_view(self):
        webbrowser.open('http://3dk.in/')


if __name__=='__main__':
    app=QtWidgets.QApplication(sys.argv)
    Window=MainWindow()
    Window.show()
    sys.exit(app.exec_())