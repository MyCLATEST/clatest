# -*- coding: utf8 -*-

# Copyright (C) 2018 - Benjamin Hebgen <mail>
# This program is Free Software see LICENSE file for details

import os
import sys
import xbmc
import xbmcgui
import xbmcplugin
import xbmcaddon
import simplejson as json
import gui

class ContextMonitor(xbmc.Player):
  def __init__ (self, *args, **kwargs):
    self.callback = args[0]
    self.trigger = args[1]
    self.messages = []
    super(ContextMonitor, self).__init__ ()
  def onPlayBackStarted(self):
    if xbmc.getInfoLabel('Container.FolderPath').startswith(self.trigger): 
      self.ui = gui.GUI( 'script-chatdialog-main.xml', xbmcaddon.Addon().getAddonInfo('path').decode('utf-8'))
      self.callback()
      self.ui.doModal()
      del self.ui
  def setMessages(self, messages):
    self.messages = messages
    self.ui.updateMessages(self.messages)
  def addMessage(self, message):
    self.messages.append(message)
    self.ui.updateMessages(self.messages)
