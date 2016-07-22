#!/usr/bin/env python2.7
#-*- coding: utf-8 -*-
__author__ = "Shrinidhi Rao"
__license__ = "GPL"
__email__ = "shrinidhi666@gmail.com"

import sys
import os
sys.path.append(os.sep.join(os.path.abspath(__file__).split(os.sep)[:-3]))
import time

import psycopg2
import psycopg2.extras


class get_connection_base(object):
  def __init__(self,database,user,password,host,port):
    self.database = database
    self.user = user
    self.password = password
    self.host = host
    self.port = port
    self.__conn = self.__connect()


  def __connect(self):
    while(True):
      try:
        conn = psycopg2.connect(database=self.database,user=self.user,password=self.password,host=self.host,port=self.port,cursor_factory=psycopg2.extras.RealDictCursor)
        conn.autocommit = True
        print("Opened database successfully")
        return (conn)
      except:
        errstr = str(sys.exc_info())
        print(errstr)
        if(errstr.find("Connection refused") >= 0):
          continue
        else:
          return(False)
        print("sleeping")
        time.sleep(1)


  def execute(self,query,data=None,dictionary=False):
    if(self.__conn):
      while(True):
        rows = None
        try:
          cur = self.__conn.cursor()
          cur.execute(query,data)
          if(dictionary):
            rows = cur.fetchall()
          cur.close()
          if(rows):
            return(rows)
          else:
            return(1)
        except:
          print (str(sys.exc_info()))
          time.sleep(1)

  def __del__(self):
    if(self.__conn):
      try:
        self.__conn.close()
        print ("Closed database connection")
      except:
        print (str(sys.exc_info()))

if(__name__=='__main__'):
  test_conn = get_connection_base(database="rbhus_render",user="postgres",password="123",host="127.0.0.1",port="5432")
  rows = test_conn.execute("select * from host_details",dictionary=True)
  print (rows)
