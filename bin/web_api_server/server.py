import setproctitle
import sys
import cherrypy
import psutil
import simplejson

setproctitle.setproctitle("web_api_server")


class HelloWorld(object):
  @cherrypy.expose
  def ping(self):
    return "alive"

  @cherrypy.expose
  def get_node_info(self, **kwargs):
    node_info = {}
    node_info['cpu_count'] = psutil.cpu_count()
    if(sys.platform.lower().find('linux') >= 0):
      node_info['loadavg'] = open('/proc/loadavg','r').read().split()
    node_info['cpu_percent'] = psutil.cpu_percent(interval=1)

    return (simplejson.dumps(node_info))



if __name__ == '__main__':
  cherrypy.quickstart(HelloWorld())