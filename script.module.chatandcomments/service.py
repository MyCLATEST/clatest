# -*- coding: utf8 -*-

# Copyright (C) 2018 - Benjamin Hebgen <mail>
# This program is Free Software see LICENSE file for details

import os
import sys
import xbmc
import xbmcgui
import xbmcplugin
import xbmcaddon
import resources.lib.ContextMonitor

if (__name__ == "__main__"):
  xbmc.executebuiltin("ReloadSkin()")
  myMonitor = resources.lib.ContextMonitor.ContextMonitor()
  xbmc.Monitor().waitForAbort()
