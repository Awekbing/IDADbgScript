#coding=utf-8
import os,sys
import time
import threading

package = "com.example.test8"
startActivity = "com.example.test8.MainActivity"

device = " -s emulator-5554 "
cmdHead = "adb %s shell " %(device)

def adbCmd(cmd): 
	os.system(cmdHead + cmd)

def delayCmd(cmd, delayTime = 5):
	time.sleep(delayTime)
	os.system(cmdHead + cmd)	
	
 


#启动APP
adbCmd("am start -D -n %s/%s" %(package, startActivity))
os.system("adb %s forward tcp:23946 tcp:23946" % (device))
raw_input()


def jdbCmd():
	os.system("jdb -connect com.sun.jdi.SocketAttach:hostname=127.0.0.1,port=8700")

t1 = threading.Thread(target=jdbCmd)
t1.start()