#!/usr/bin/env python
#coding:utf-8

from model.admin import Admin
from socketApp import client

def display():

    print "     [1] 登录 ............................."
    print "     [2] 注册 ............................."
    print "     [exit] 退出..........................."

def login():
    print "         欢迎进入登录页面    "
    user = raw_input('username: ')
    password = raw_input("password: ")
    admin = Admin()
    result = admin.CheckValiuser(user)

    if not result:
        print "用户名不存在"
    else:
        res = admin.CheckValidata(user,password)
        if not res:
            print "密码错误"
            login()
        else:
            uid = admin.Get_Uid(user)[0]
            client.connect_robot(uid)

def sign_in():
    print "         欢迎进入注册页面    "
    user = raw_input('username: ')
    password = raw_input("password: ")
    admin = Admin()
    result = admin.CheckValiuser(user)

    if not result:
        admin.Insert_User(user,password)
        print "注册成功............."
        print "请登录............"
        login()
    else:
        print "用户已存在,请输入有效的用户名"
        sign_in()

def main():

    chan_one = ["1","2"]
    display()
    while True:
        chance = raw_input("Please input your chance[1|2|exit]:")
        if chance in chan_one:
            if chance == '1':
                login()
            else:
                sign_in()
        elif chance == 'exit':
            print "退出....."
            exit()
        else:
            print "Your chance is wrong!"
            display()

if __name__ == '__main__':
    main()
