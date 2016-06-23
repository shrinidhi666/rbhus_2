import setproctitle
import sys
from flask import Flask
from flask import request
import psutil
import simplejson
import  multiprocessing
import ../../lib.db.rbhus
app = Flask(__name__)
setproctitle.setproctitle("web_api_server")


@app.route("/ping")
def ping():
  return "alive"


def process(**kwargs):
  pass

if (__name__ == '__main__'):
  app.run()
