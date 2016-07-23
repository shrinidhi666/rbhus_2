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
import lib.common.system_utils


def update_host_details_queue():
	details = lib.common.system_utils.get_local_host_details()
	details_list = details.keys()
	insert_query = "insert into host_details (host_ip,host_name,cpu_total,cpu_used,ram_total,ram_used,is_alive,load_avg)"
	



