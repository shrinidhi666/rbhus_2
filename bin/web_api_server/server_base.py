import setproctitle
import sys
import cherrypy
import psutil
import simplejson

setproctitle.setproctitle("web_api_server")


class web_api(object):
  @cherrypy.expose
  def ping(self):
    return "alive"


if (__name__ == '__main__'):
  cherrypy.quickstart(web_api())
