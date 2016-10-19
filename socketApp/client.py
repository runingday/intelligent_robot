#!/usr/bin/env python
#coding:utf-8

import socket


def connect_robot(uid):
    client = socket.socket()
    
    ip_port = ('127.0.0.1', 9999)
    
    client.connect(ip_port)
    
    recv_data = client.recv(1024)
    print recv_data
    while True:
        send_data = raw_input("please input your question: ")
        client.send(str(uid) + ":" + send_data)
        if send_data == 'exit':
            exit() 
        recv_data = client.recv(1024)
        print recv_data
        



