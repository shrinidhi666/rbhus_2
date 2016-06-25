#!/usr/bin/env python2.7
#-*- coding: utf-8 -*-
__author__ = "Shrinidhi Rao"
__license__ = "GPL"
__email__ = "shrinidhi666@gmail.com"

import sys
sys.path.append("../../")
import setproctitle

from flask import Flask
from flask import request
import psutil
import simplejson
import  multiprocessing
import lib.db.rbhus_hosts
app = Flask(__name__)
setproctitle.setproctitle("web_api_server")


@app.route("/")
def ping():
  details = {}
  details['cpu_usage'] = psutil.cpu_percent(interval=1,percpu=True)
  details['memory'] = {'ram': psutil.virtual_memory(),'swap': psutil.swap_memory()}
  disk_partitions = psutil.disk_partitions()
  print(disk_partitions)
  return(simplejson.dumps(details))


def process(**kwargs):
  db_con = lib.db.rbhus_hosts.get_connection()
  rows = db_con.execute("select * from host_types",dictionary=True)
  return(simplejson.dumps(rows))

if (__name__ == '__main__'):
  app.run()
