import sys, datetime, re
import xbmc, xbmcgui
import json
import operator

class GUI( xbmcgui.WindowXMLDialog ):
  def __init__( self, *args, **kwargs ):
    super(GUI,self).__init__( self, *args, **kwargs )
  def onInit(self):
    self.msgButtons = []
    self.msgButtons.append(self.getControl(41001))
    self.msgButtons.append(self.getControl(41002))
    self.msgButtons.append(self.getControl(41003))
    self.msgButtons.append(self.getControl(41004))
    self.msgButtons.append(self.getControl(41005))
  def onClick(self, cid):
    if cid == 40001:
      self.goUp()
    elif cid == 42001:
      self.goDown()
    else:
      self.showMessage()
  def updateMessages(self, messages):
    self.messages = messages
    self.showMessages(-5)
