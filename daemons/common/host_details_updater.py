#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
__author__ = "Shrinidhi Rao"
__license__ = "GPL"
__email__ = "shrinidhi666@gmail.com"

import sys
import os

sys.path.append(os.sep.join(os.path.abspath(__file__).split(os.sep)[:-3]))
import lib.db.rbhus_queue
import lib.db.rbhus_infra
import lib.common.system_utils
import lib.common.debug
import time
import logging


def update_host_details():
  local_host = lib.common.system_utils.local_host()
  local_host.update()


if (__name__ == "__main__"):
  while (True):
    try:
      update_host_details();
    except:
      logging.debug(sys.exc_info())
    time.sleep(5)
