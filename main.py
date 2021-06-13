import subprocess
subprocess.call("./bin.sh", shell=True)
from core.base import Base
from core.openGLUtlis import OpenGLUtlis
from OpenGL.GL import *
from core.attribute import Attribute
#render a 6 point

class Test(Base):
  def initialize(self):
    print("starting..")

    #create gpu program 

    # vertex sader code(points)
    vsCode='''
    in vec3 position;
    in vec3 vertexColor;
    out vec3 color;
    void main()
    {
      gl_Position=vec4(position.x,position.y,position.z,1.0);
      color=vertexColor;
    }'''

    #fragment shader code  (coor)
    fsCode='''
    in vec3 color;
    void main()
    {
      gl_FragColor=vec4(color.r,color.g,color.b,1.0);
    }'''  
    #send code to gpu to compile

    self.programRef=OpenGLUtlis.initlizeProgram(vsCode, fsCode)
    #render settings
    glPointSize(16) 
    glLineWidth(8)

    #set up VAOs(vertex array objects)
    vaoRef= glGenVertexArrays(1)
    glBindVertexArray(vaoRef)

    #setup vertex Attribute
    positionData=[[ 0.8,  0.0, 0.0],
                  [ 0.4,  0.6, 0.0],
                  [-0.4,  0.6, 0.0],
                  [-0.8,  0.0, 0.0],
                  [-0.4, -0.6, 0.0],
                  [ 0.4, -0.6, 0.0]]
    positionAttribute=Attribute("vec3",positionData)
    positionAttribute.associateVariable(self.programRef,"position")
    colorData=[[1.0,0.0,0.0],
               [1.0,0.5,0.0],
               [1.0,1.0,0.0],
               [0.0,1.0,0.0],
               [0.0,0.0,1.0],
               [0.5,0.0,1.0]]
    colorAttribute=Attribute("vec3",colorData)
    colorAttribute.associateVariable(self.programRef,"vertexColor")
    self.vertexCount=len(positionData)
  def update(self):
    # select program to use when rendering 
    glUseProgram(self.programRef)

    #renders geometric object(s) using program
    glDrawArrays(GL_TRIANGLE_FAN, 0, self.vertexCount)

#create an instance of this class and run the program

Test().run()
# https://github.com/Namanskshetty/pyopengl
