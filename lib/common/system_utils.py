#!/usr/bin/env python2.7
#-*- coding: utf-8 -*-
__author__ = "Shrinidhi Rao"
__license__ = "GPL"
__email__ = "shrinidhi666@gmail.com"


import sys
import os
sys.path.append(os.sep.join(os.path.abspath(__file__).split(os.sep)[:-3]))
import lib.db.rbhus_queue
import lib.db.rbhus_infra
import simplejson
import psutil
import socket
import multiprocessing



class local_host(object):

  def __init__(self):
    self.db_queue = lib.db.rbhus_queue.get_connection()
    self.db_infra = lib.db.rbhus_infra.get_connection()

  @property
  def host_ip(self):
    return (socket.gethostbyname(socket.gethostname()))

  @host_ip.setter
  def host_ip(self,value):
    pass

  @property
  def host_name(self):
    return (socket.gethostname())

  @host_name.setter
  def host_name(self,value):
    pass

  @property
  def cpu_total(self):
    return (multiprocessing.cpu_count())

  @cpu_total.setter
  def cpu_total(self,value):
    pass

  @property
  def cpu_used(self):

    self.db_queue.execute()








def get_local_host_details():
  local_dets = local_host()

  details = {}
  details['host_name'] = socket.gethostname()
  details['host_ip'] = local_dets.host_ip
  details['cpu_usage_all'] = psutil.cpu_percent(interval=1,percpu=True)
  details['cpu_usage'] = psutil.cpu_percent(interval=1)
  details['memory'] = {'ram_total': psutil.virtual_memory(),'swap_total': psutil.swap_memory()}
  if(sys.platform.lower().find("linux") >= 0):
    details['loadavg'] = os.getloadavg()
  details['disk'] = psutil.disk_partitions()
  details['cpu_total'] = multiprocessing.cpu_count()

  return(details)


if(__name__ == '__main__'):
  local_dets = local_host()
  local_dets.host_ip = "test"
  print(local_dets.host_ip)