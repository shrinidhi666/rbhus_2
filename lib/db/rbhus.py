#!/usr/bin/python
import sys
import time

import psycopg2
import psycopg2.extras


class get_connection():
  def __init__(self):
    self.__conn = self.__connect()


  def __connect(self):
    while(True):
      try:
        conn = psycopg2.connect(database="rbhus",
                                       user="postgres",
                                       password="123",
                                       host="127.0.0.1",
                                       port="5432",
                                       cursor_factory=psycopg2.extras.RealDictCursor)
        conn.autocommit = True
        print("Opened database successfully")
        return (conn)
      except:
        print (str(sys.exc_info()))
        time.sleep(1)


  def execute(self,query):
    while(True):
      try:
        cur = self.__conn.cursor()
        cur.execute(query)
        rows = cur.fetchall()
        cur.close()
        return(rows)
      except:
        print (str(sys.exc_info()))
        time.sleep(1)

  def __del__(self):
    try:
      self.__conn.close()
      print ("Closed database connection")
    except:
      print (str(sys.exc_info()))

if(__name__=='__main__'):
  test_conn = get_connection()
  rows = test_conn.execute("select * from host_types")
  print (rows)






