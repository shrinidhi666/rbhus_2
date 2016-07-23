#!/usr/bin/env python2.7
#-*- coding: utf-8 -*-
__author__ = "Shrinidhi Rao"
__license__ = "GPL"
__email__ = "shrinidhi666@gmail.com"

import os
import sys

sys.path.append(os.sep.join(os.path.abspath(__file__).split(os.sep)[:-3]))
import lib.common.system_utils
import setproctitle

import simplejson
import  cherrypy
setproctitle.setproctitle("web_api_server")

cherrypy._cpserver.Server.thread_pool = 30
class host_details(object):
  @cherrypy.expose
  def index(self):
    details = lib.common.system_utils.get_local_host_details()
    return(simplejson.dumps(details))



if (__name__ == '__main__'):
  cherrypy.tree.mount(host_details(),'/')
  cherrypy.engine.start()
  cherrypy.engine.block()
