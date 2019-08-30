import requests
from contextlib import contextmanager
import json
import os
import serial.tools.list_ports
#import webbrowser
#setup you ip here
ip="http://localhost:5000"
#setup your API KEY HERE
Api_Key="FD550BD4DA2442BA906AD1850539D6DB"


class octoprint_api:


    def __init__(self):
        x=12

    
    def List_all_files(self):
        url=ip+'/api/files'
        header={'X-Api-Key': 'FD550BD4DA2442BA906AD1850539D6DB' }
        payload ={"exclude":'temperature',"history": 'true',"limit": None}
        payload = {"recursive":'false', "force":'false'}
        response=requests.get(url,headers=header,params=payload)
        files=response.json()
        items=[]
        #print(files)
        #lst=files['files']
        #print("Type---",type(lst))
        #print(files['files']['name'])
        newDict={}
        for item in files['files']:
            newDict.update(item)
            files['files']=newDict
            #print("File Name :",files['files']['name'],"type",files['files']['typePath'])
            if(files['files']['type']!='folder'):
                items.append(files['files']['name'])
            print(files['files']['type'])
        return items

    def select_file(self,file,prnt=False):
        #select the current selected file from file list view for printing !
        print("selectef file have been printing",file)
        url='http://localhost:5000/api/files/local/'+format(file)
        header={'content-type': 'application/json','X-Api-Key': 'FD550BD4DA2442BA906AD1850539D6DB'}
        payload = {'command': 'select', 'print': True}
        res=requests.post(url, data=json.dumps(payload), headers=header)
        print("file has been selected for printing ")
        print(res)

    def startprint(self):
        url="http://localhost:5000/api/job"
        payload = {'command': 'start'}
        headers = {'content-type': 'application/json', 'X-Api-Key': 'FD550BD4DA2442BA906AD1850539D6DB'}
        res=requests.post(url, data=json.dumps(payload), headers=headers)
        #print(res)

    def job_details(self):
        url='http://localhost:5000/api/job'
        headers = {'X-Api-Key':'FD550BD4DA2442BA906AD1850539D6DB'}
        response = requests.get(url, headers=headers)
        result=response.json()
        data=result.values()
        #print(data)
    """
    Auto connect the printer : The Acuto Connect is called  after Application boot up , The Auto Connect 
    try connect the printer 3 time if all its failes it ask the user to manualy connect the printer 
    through the interface !

    """


    def connect_printer(self):
        url='http://localhost:5000/api/connection'
        header={'content-type': 'application/json' ,'X-Api-Key': 'FD550BD4DA2442BA906AD1850539D6DB'}
        #get all avilable serial ports
        try:
            #scan the avilable ports connected ! 
            ports = serial.tools.list_ports.comports()
            
            #holds list of avilable ports
            port_list=[]
            
            #fetch each port details 
            for port, desc, hwid in sorted(ports):
                print("Connectiong Port to ",port)
                port_list.append(port)
                payload = {"command": "connect", "port": "{}".format(port), "baudrate": int("250000") }
                res=requests.post(url,data=json.dumps(payload),headers=header)
                print("Printer Connected response>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                print(res.text())
        except Exception as e:
            err=["error","Serial por connection error",str(e)]
            print("Printer Connected response error>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            return err
    
    def _tool_dict(self,data):
        if isinstance(data, (int, float)):
                data = (data,)
        if isinstance(data, dict):
                ret = data
        else:
                ret = {}
                for n, thing in enumerate(data):
                        ret['tool{}'.format(n)] = thing
        return ret


    def Set_Tool_Temp(self):
        url='http://localhost:5000/api/printer/tool'
        target=self._tool_dict(60)
        print(target)
        payload = {"command": "target", 'targets':target}
        headers = {'content-type': 'application/json', 'X-Api-Key': 'FD550BD4DA2442BA906AD1850539D6DB'}
        res=requests.post(url, data=json.dumps(payload), headers=headers)
        print("Tool Temp res",res)

    def Set_Bed_Temp(self):
        url=ip+"/api/printer/bed"
        payload = {"command": "target", 'target':target}
        headers = {'content-type': 'application/json', 'X-Api-Key': 'FD550BD4DA2442BA906AD1850539D6DB'}
        res=requests.post(url, data=json.dumps(payload), headers=headers)
    

    def jog(self,x=None,y=None,z=None,absolute=False,speed=None):
        print("Jog the axis")
        url="http://localhost:5000/api/printer/printhead"
        payload = {'command': 'jog', 'absolute': absolute}
        if x != None:
            payload['x'] = x
        if y != None:
            payload['y'] = y
        if z != None:
            payload['z'] = z
        if speed != None:
            payload['speed'] = speed
        print ("jog called" + str(payload))
        headers = {'content-type': 'application/json', 'X-Api-Key': 'FD550BD4DA2442BA906AD1850539D6DB'}
        requests.post(url, data=json.dumps(payload), headers=headers)

    def setHome(self):
         url='http://localhost:5000/api/printer/printhead'
         header={'content-type': 'application/json','X-Api-Key': 'FD550BD4DA2442BA906AD1850539D6DB'}
         axes=['x', 'y', 'z']
         payload = {"command": "home", "axes": axes}
         res=requests.post(url, data=json.dumps(payload), headers=header)
         print(res.text)
         return res


    def stop_printing(self):
        print("stoping the current job !")
        url='http://localhost:5000/api/job'
        header={'content-type': 'application/json' ,'X-Api-Key': 'FD550BD4DA2442BA906AD1850539D6DB'}
        payload = {"command": "cancel"}
        res=requests.post(url,data=json.dumps(payload),headers=header)
        self.setHome()


    def pause_print(self):
        print("pause the current job !")
        url='http://localhost:5000/api/job'
        header={'content-type': 'application/json' ,'X-Api-Key': 'FD550BD4DA2442BA906AD1850539D6DB'}
        payload = {"command": "pause"}
        res=requests.post(url,data=json.dumps(payload),headers=header)
    
