import setproctitle
import sys
import cherrypy
import psutil
import simplejson

setproctitle.setproctitle("web_api_server")


class HelloWorld(object):
  @cherrypy.expose
  def index(self):
    return "Hello world!"

  @cherrypy.expose
  def get_node_info(self, **kwargs):
    cpu_stats = psutil.cpu_stats()
    print (cpu_stats)



if __name__ == '__main__':
  cherrypy.quickstart(HelloWorld())