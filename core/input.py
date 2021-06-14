import pygame

class Input(object):

  def __init__(self):

    #has the user quit
    self.quit=False
    #LIST TO STORE KEY STATES
    # down & up: discrete events, last for oneiteraton
    # pressed: continuosus events, between down and up events
    self.keyDownList   =[]
    self.keyPressedList=[]
    self.keyUpList     =[]
  
  def update(self):
    #iterate over all user events(keyboard/mouse)
    # that have occured since last time events checked
    #reset discrete jey sorted
    self.keyDownList   =[]
    self.keyUpList     =[]
    for event in pygame.event.get():
      #event quit occurs by clicking the close window
      if event.type==pygame.QUIT:
        self.quit=True
      #check for key down and key up events
      #get name of the key from event
      # and append to or remove from corresponding lists
      if event.type==pygame.KEYDOWN:
        keyName=pygame.key.name(event.key)
        self.keyDownList.append(keyName)
        self.keyPressedList.append(keyName)
      if event.type==pygame.KEYUP:
        keyName=pygame.key.name(event.key)
        self.keyPressedList.remove(keyName) 
        self.keyUpList.append(keyName)
               
  #functions to query the key state
  def isKeyDown(self,keyName):
    return keyName in self.keyDownList 

  def isKeyPressed(self,keyName):
    return keyName in self.keyPressedList

  def isKeyUp(self,keyName):
    return keyName in self.keyUpList



