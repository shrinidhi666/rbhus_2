import setproctitle
import sys
from flask import Flask
from flask import request
import psutil
import simplejson
import  multiprocessing

app = Flask(__name__)
setproctitle.setproctitle("web_api_server")


@app.route("/ping")
def ping():
  return "alive"


def process(**kwargs)

if (__name__ == '__main__'):
  app.run()
