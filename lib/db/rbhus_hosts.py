#!/usr/bin/env python2.7
#-*- coding: utf-8 -*-
__author__ = "Shrinidhi Rao"
__license__ = "GPL"
__email__ = "shrinidhi666@gmail.com"


import sys
sys.path.append("../../")
import time

import psycopg2
import psycopg2.extras
import lib.db.base


class get_connection(lib.db.base.get_connection_base):
  def __init__(self):
    super(get_connection,self).__init__(database="rbhus",user="postgres",password="123",host="127.0.0.1",port="5432")



if(__name__=='__main__'):
  test_conn = get_connection()
  rows = test_conn.execute("select * from host_types",dictionary=True)
  print (rows)






