#!/usr/bin/env python2.7
#-*- coding: utf-8 -*-
__author__ = "Shrinidhi Rao"
__license__ = "GPL"
__email__ = "shrinidhi666@gmail.com"

import os
import sys

sys.path.append(os.sep.join(os.path.abspath(__file__).split(os.sep)[:-3]))

import lib.db.base
import lib.common.debug
import logging


class get_connection(lib.db.base.get_connection_base):
  def __init__(self):
    super(get_connection,self).__init__(database="rbhus_queue",user="postgres",password="123",host="127.0.0.1",port="5432")



if(__name__=='__main__'):
  test_conn = get_connection()
  if(test_conn):
    rows = test_conn.execute("select * from host_types",dictionary=True)
    logging.debug (rows)






