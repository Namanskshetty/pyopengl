import pygame
import sys
import webbrowser
from core.input import Input

class Base(object):
  def __init__(self): #self brings the py class here 
  #self represents the instance of the class. By using the “self” keyword we can access the attributes and methods of the class in python. It binds the attributes with the given arguments. The reason you need to use self. is because Python does not use the @ syntax to refer to instance attributes.
    #initilize pygame modules
    pygame.init()

    #width and height of windoww
    screenSize=(512,512) #it likes powers of 2

    #inicate rendaering options 
    displayFlags=pygame.DOUBLEBUF | pygame.OPENGL
                       #double buffer#  
    #create and display Window
    self.screen=pygame.display.set_mode(screenSize,displayFlags)

    #set the title of the window
    pygame.display.set_caption("Osi model(tor Circuit)")

    #determines if main loop is active
    self.running=True

    #manage time-releated dara and operations
    self.clock=pygame.time.Clock()

    ## manage user input
    self.input=Input()

  #impplemented by extending class
  def initialize(self):
    pass 

  #implement by extending class 
  def update(self):
    pass

  def run(self):
    #startup
    self.initialize()

    #main Loop
    while self.running:
      #process input##
      self.input.update()

      if self.input.quit:
        self.running=False
      ##update##
      self.update()

      ## render ##
      #display image on screen
      pygame.display.flip()

      #pause if necessary to achive 60 fps 
      self.clock.tick(60) #it might go up to 500fps cpu might fr yup

    ##shutdown
    pygame.quit()
    webbrowser.open("https://github.com/Namanskshetty")
    sys.exit()


