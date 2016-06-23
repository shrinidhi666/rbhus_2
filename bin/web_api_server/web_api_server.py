import sys
sys.path.append("../../")
import setproctitle

from flask import Flask
from flask import request
import psutil
import simplejson
import  multiprocessing
import lib.db.rbhus
app = Flask(__name__)
setproctitle.setproctitle("web_api_server")


@app.route("/ping")
def ping():

  return process()


def process(**kwargs):
  db_con = lib.db.rbhus.get_connection()
  rows = db_con.execute("select * from host_types",dictionary=True)
  return(simplejson.dumps(rows))

if (__name__ == '__main__'):
  app.run()
