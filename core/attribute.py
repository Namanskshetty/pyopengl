import numpy
from OpenGL.GL import *

class Attribute(object):
  def __init__(self, dataType, data):
    #type of elements in data array 
    # int |float|vec3,2,vec4
    self.dataType=dataType
    self.data=data
    #array of data to be stored in buffer#
    #reference to avilable buffer in gpu
    self.bufferRef=glGenBuffers(1)
    #upload data immediately
    self.uploadData()
  #upload this data to gpu buffer
  def uploadData(self):
    #convert data to numpy array format; convert to float
    data=numpy.array(self.data).astype(numpy.float32)
    #select buffer used by folloeing functions
    glBindBuffer(GL_ARRAY_BUFFER,self.bufferRef)

    #store the data in bound buffer
    glBufferData(GL_ARRAY_BUFFER,data.ravel(),GL_STATIC_DRAW)
  #associate variable in gpu program with this buffer
  def associateVariable(self,programRef,variableName):
    #get reference for program variable awith given name#
    variableRef=glGetAttribLocation(programRef,variableName)

    #if the program data does not refernecae the variable, exit
    if variableRef == -1:
      return
    #select the buffer by following functions
    glBindBuffer(GL_ARRAY_BUFFER,self.bufferRef)

    #speicfy how data will be read
    #form the buffaer currently bound to GL_ARRAY_BUFFER
    if self.dataType == "int":
      glVertexAttribPointer(variableRef,1,GL_INT,False,0,None)
    elif self.dataType=="float":
      glVertexAttribPointer(variableRef,1,GL_FLOAT,False,0,None)
    elif self.dataType=="vec2":
      glVertexAttribPointer(variableRef,2,GL_FLOAT,False,0,None)
    elif self.dataType=="vec3":
      glVertexAttribPointer(variableRef,3,GL_FLOAT,False,0,None) 
    elif self.dataType=="vec4":
      glVertexAttribPointer(variableRef,4,GL_FLOAT,False,0,None)    
    else:
      raise Exception("unkown data type"+self.dataType)

    #indicates data shoulf be streamed to variable from buffer 
    glEnableVertexAttribArray(variableRef)      
