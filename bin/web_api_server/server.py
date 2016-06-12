import setproctitle
import sys
import cherrypy

setproctitle.setproctitle("web_api_server")


class HelloWorld(object):
  @cherrypy.expose
  def index(self):
    return "Hello world!"


if __name__ == '__main__':
  cherrypy.quickstart(HelloWorld())