#!/usr/bin/env python
#coding:utf-8

from utility.sqlHelper import MysqlHelper

class Admin(object):

    def __init__(self):
        self.__helper = MysqlHelper()

    def Get_One(self, user):
        sql = "select * from chat_user where user=%s"
        params = (user,)
        return self.__helper.Get_One(sql, params)

    def CheckValiuser(self, username):
        sql = "select * from chat_user where user=%s"
        params = (username,)
        return self.__helper.Get_One(sql, params)
    
    def CheckValidata(self, username, passwd):
        sql = "select * from chat_user where user=%s and pass=%s"
        params = (username, passwd)
        return self.__helper.Get_One(sql, params)

    def Insert_User(self, username, password):
        sql = "insert chat_user (user,pass) values(%s,%s)"
        params = (username, password)
        self.__helper.Insert_record(sql, params)

    def Get_Value(self, key):
        sql = "select key_value from key_value_db where key_inc like '%%%s%%'"
        return self.__helper.Get_Value(sql, key)

    def Insert_key_value(self, uid, client_data, server_data):
        sql = "insert chat_data (uid, client_data, server_data) values (%s,%s,%s)"
        params = (uid, client_data, server_data)
        self.__helper.Insert_record(sql, params)

    def Get_Uid(self, username):
        sql = "select id from chat_user where user=%s"
        params = (username,)
        return self.__helper.Get_One(sql, params)

        

        
