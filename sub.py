# -*- coding: utf-8 -*-    
import paho.mqtt.client as mqtt 
import json  

import pymongo


  
          
# 连接成功回调函数  
def on_connect(client, userdata, flags, rc):  
    print("Connected with result code " + str(rc))  
    # 连接完成之后订阅gpio主题  
    client.subscribe("ICS")  
  
# 消息推送回调函数  
def on_message(client, userdata, msg):  
    print(msg.topic+" "+str(msg.payload))  
    # 获得负载中的pin 和 value  
    # re = json.loads(str(msg.payload))  
     
  
if __name__ == '__main__': 

    #连接mongodb数据库，运行前先开启mongodb
    # conn = pymongo.MongoClient("localhost:27017")
    # db = conn.study
    # db.person.save({'id': 5, 'name': 'kaka', 'sex': 'male'})
    # print u'所有集合：',db.collection_name

    client = mqtt.Client()  
    client.on_connect = on_connect  
    client.on_message = on_message  
      
    try:  
        # 请根据实际情况改变MQTT代理服务器的IP地址  
        client.connect("127.0.0.1", 1883, 60)  
        client.loop_forever()  
    except KeyboardInterrupt:  
        client.disconnect()  





