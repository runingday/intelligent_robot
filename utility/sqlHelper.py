#!/usr/bin/env python
#coding:utf-8
import MySQLdb
import conf

class MysqlHelper(object):

    def __init__(self):
        self.__conn_dict = conf.conn_dict

    def Get_Dict(self, sql, params):
        conn = MySQLdb.connect(**self.__conn_dict)
        cur = conn.cursor(cursorclass = MySQLdb.cursors.DictCursor)
        cur.execute(sql, params)
        data = cur.fetchall()

        cur.close()
        conn.close()

        return data
    
    def Get_One(self, sql, params):
        conn = MySQLdb.connect(**self.__conn_dict)
        #cur = conn.cursor(cursorclass = MySQLdb.cursors.DictCursor)
        cur = conn.cursor()
        cur.execute(sql, params)
        data = cur.fetchone()

        cur.close()
        conn.close()

        return data
    def Insert_record(self, sql, params):
        conn = MySQLdb.connect(**self.__conn_dict)
        cur = conn.cursor(cursorclass = MySQLdb.cursors.DictCursor)
        #cur = conn.cursor()
        
        cur.execute(sql, params)
        conn.commit()
        cur.close()
        conn.close()

    def Get_Value(self, sql, key):
        conn = MySQLdb.connect(**self.__conn_dict)
        cur = conn.cursor()
        cur.execute(sql % key)
        data = cur.fetchone()

        cur.close()
        conn.close()

        return data
        

        

