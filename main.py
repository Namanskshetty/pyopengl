import subprocess
subprocess.call("./bin.sh", shell=True)
from core.base import Base
from core.openGLUtlis import OpenGLUtlis
from OpenGL.GL import *
from core.attribute import Attribute
from core.uniform import Uniform
from core.matrix import Matrix
from math import pi

class Test(Base):
  def initialize(self):
    print("starting..")

    #create gpu program 

    # vertex sader code(points)
    vsCode='''
    in vec3 position;
    uniform mat4 projectionMatrix;
    uniform mat4 modelMatrix;
    void main()
    {
        gl_Position = projectionMatrix * modelMatrix * vec4(position, 1.0);
    }
    '''
    fsCode="""
    out vec4 fragColor;
    void main()
    {
        fragColor=vec4(1.0, 0.0, 1.0,1.0);
    }
    """

    self.programRef=OpenGLUtlis.initlizeProgram(vsCode,fsCode)

    glClearColor(0.0,0.0,0.0,1.0)
    glEnable(GL_DEPTH_TEST)

    vaoRef=glGenVertexArrays(1)
    glBindVertexArray(vaoRef)
    positionData=[[ 0.0,  0.2, 0.0],
                  [ 0.1, -0.2, 0.0],
                  [-0.1, -0.2, 0.0]]
    positionAttribute=Attribute("vec3",positionData)
    positionAttribute.associateVariable(self.programRef,"position")
    self.vertexCount=len(positionData)
    mMatrix=Matrix.makeTranslation(0,0,-1)
    self.modelMatrix=Uniform("mat4",mMatrix)
    self.modelMatrix.locateVariable(self.programRef,"modelMatrix")

    pMatrix=Matrix.makePerspective()
    self.projectionMatrix=Uniform("mat4",pMatrix)
    self.projectionMatrix.locateVariable(self.programRef,"projectionMatrix")

  def update(self):
    movAm=0.01
    if self.input.isKeyPressed("w"):
      m=Matrix.makeTranslation(0,movAm,0)
      self.modelMatrix.data=m @ self.modelMatrix.data
    if self.input.isKeyPressed("s"):
      m=Matrix.makeTranslation(0,-movAm,0)
      self.modelMatrix.data=m @ self.modelMatrix.data
    if self.input.isKeyPressed("a"):
      m=Matrix.makeTranslation(-movAm,0,0)
      self.modelMatrix.data=m @ self.modelMatrix.data
    if self.input.isKeyPressed("d"):
      m=Matrix.makeTranslation(movAm,0,0)
      self.modelMatrix.data=m @ self.modelMatrix.data


    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glUseProgram(self.programRef)
    self.projectionMatrix.uploadData()
    self.modelMatrix.uploadData()
    glDrawArrays(GL_TRIANGLES,0,self.vertexCount)
Test().run()
# https://github.com/Namanskshetty/pyopengl
