#!/usr/bin/env python2.7
#-*- coding: utf-8 -*-
__author__ = "Shrinidhi Rao"
__license__ = "GPL"
__email__ = "shrinidhi666@gmail.com"

import os
import sys

sys.path.append(os.sep.join(os.path.abspath(__file__).split(os.sep)[:-3]))
import setproctitle

import psutil
import simplejson
import  cherrypy
setproctitle.setproctitle("web_api_server")

cherrypy._cpserver.Server.thread_pool = 30
class host_details(object):
  @cherrypy.expose
  def index(self):
    details = {}
    details['cpu_usage_all'] = psutil.cpu_percent(interval=1,percpu=True)
    details['cpu_usage'] = psutil.cpu_percent(interval=1)
    details['memory'] = {'ram': psutil.virtual_memory(),'swap': psutil.swap_memory()}
    if(sys.platform.lower().find("linux") >= 0):
      details['loadavg'] = os.getloadavg()
    details['disk'] = psutil.disk_partitions()
    return(simplejson.dumps(details))



if (__name__ == '__main__'):
  cherrypy.tree.mount(host_details(),'/')
  cherrypy.engine.start()
  cherrypy.engine.block()
