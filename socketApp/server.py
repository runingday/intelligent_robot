#!/usr/bin/env python
#coding:utf-8

import sys
import SocketServer
import MySQLdb
sys.path.append("..")
from model.admin import Admin


class MyServer(SocketServer.BaseRequestHandler):
    

    def handle(self):
        request = self.request
        request.send("hello. Can I help you.....")
        flag = True
        admin = Admin()


        while flag:
            data = request.recv(1024)
            uid = data.split(":")[0]
            content = data.split(":")[1]
            print uid,content
            if content == "exit":
                flag = False
            value = admin.Get_Value(content)
            if not value:
                prompt = "数据库中没有你需要的答案"
                admin.Insert_key_value(uid, content, prompt)
                request.send(prompt)
            else:
                admin.Insert_key_value(uid, content, value[0])
                request.send(value[0])
        request.close()
    
    def setup(self):
        pass

    def finish(self):
        pass

if __name__ == "__main__":
    server = SocketServer.ThreadingTCPServer(('127.0.0.1',9999), MyServer)
    server.serve_forever()
        
