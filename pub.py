#-*- coding: utf-8 -*- 
import paho.mqtt.publish as publish
import threading
import time
from time import ctime,sleep
import json

#hostname='162.105.80.59'
# hostname='192.168.199.231'
hostname='127.0.0.1'

device_json={"secretkey":"93cf82461c324858961b6cc70fc5033d","deviceprofile":{"devicename":"hhhh","IP":"1.1.1.1","location":"23","tags":"33","latitude":"33","longitude":"22","sensors":[{"name":"22","sid":"22","channels":[{"name":"22","type":"22","unit":"22","samplingperiod":"22"}]},{"name":"22","sid":"22","channels":[{"name":"22","type":"22","unit":"22","samplingperiod":"22"}]}],"actuators":[{"name":"22name"}]}}




def pub_TEST():
	while 1:
		msg=[{
			'topic':"TEST",
			'payload':" This just is the content of TEST--timestamp:"+ctime(),
			'qos':0,
			'retain':False
		}]
		publish.multiple(msg,hostname=hostname)
		sleep(5)
		pass


def pub_SB():
	while 1:
		device_json['deviceprofile']['devicename']='devicename'+str(int(time.time()))
		msg=[{
			'topic':"ICS",
			'payload':json.dumps(device_json),
			'qos':0,
			'retain':False
		}]
		publish.multiple(msg,hostname=hostname)
		print json.dumps(device_json)+'\n'
		sleep(5)
		pass



if __name__ == "__main__":
	#threads=[]
	t1=threading.Thread(target=pub_TEST)
	#threads.append(t)
	#t.setDaemon(True)
	t1.start()
	t2=threading.Thread(target=pub_SB)
	t2.start()
