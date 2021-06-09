import pygame

class Input(object):

  def __init__(self):

    #has the user quit
    self.quit=False
  
  def update(self):
    #iterate over all user events(keyboard/mouse)
    # that have occured since last time events checked

    for event in pygame.event.get():
      #event quit occurs by clicking the close window
      if event.type==pygame.QUIT:
        self.quit=True
        