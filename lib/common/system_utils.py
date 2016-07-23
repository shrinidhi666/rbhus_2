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
import logging



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
    cpu_used_row = self.db_queue.execute("select cpu_used from host_details where host_ip=%s",(self.host_ip,),dictionary=True)
    if(not isinstance(cpu_used_row,int)):
      return (cpu_used_row[0]['cpu_used'])
    else:
      return (0)

  @cpu_used.setter
  def cpu_used(self,value):
    cpu_free = self.cpu_total - value
    if(cpu_free >= 0 and cpu_free <= self.cpu_total):
      self.db_queue.execute("update host_details set cpu_used=%s where host_ip=%s",(value,self.host_ip,))
    else:
      logging.error("not a valid cpu_used value")

  @property
  def loadavg(self):
    if (sys.platform.lower().find("linux") >= 0):
      return (os.getloadavg()[0])
    elif (sys.platform.lower().find("win") >= 0):
      return (psutil.cpu_percent(interval=1))

  @loadavg.setter
  def loadavg(self,value):
    pass

  @property
  def is_enabled(self):
    is_enabled_row = self.db_queue.execute("select is_enabled from host_details where host_ip=%s",(self.host_ip,),dictionary=True)
    if(not isinstance(is_enabled_row,int)):
      return (is_enabled_row[0]['is_enabled'])
    else:
      logging.error("no valid host_ip found")
    return (False)

  @is_enabled.setter
  def is_enabled(self,value):
    if(isinstance(value,bool)):
      self.db_queue.execute("update host_details set is_enabled=%s where host_ip=%s",(value,self.host_ip,))
    else:
      logging.error("boolean expected: True/False")











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
  print (local_dets.cpu_used)
  print(local_dets.loadavg)
  local_dets.cpu_used = 2
  print (local_dets.cpu_used)
  print (local_dets.is_enabled)
  local_dets.is_enabled = 0