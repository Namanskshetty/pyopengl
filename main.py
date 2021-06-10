import subprocess
subprocess.call("./bin.sh", shell=True)
from core.base import Base
from core.openGLUtlis import OpenGLUtlis
from OpenGL import GL

#render a single point

class Test(Base):
  def initialize(self):
    print("starting..")


    #create gpu pro

    # vertex sader code
    vsCode='''
    void main()
    {
      gl_Position=vec4(0.0,0.0,0.0,1.0);
    }'''

    #fragment shader code  
    fsCode='''
    void main()
    {
      gl_FragColor=vec4(1.0,1.0,0.0,1.0);
    }'''  
    #send code to gpu to compile

    self.programRef=OpenGLUtlis.initlizeProgram(vsCode,fsCode)

    #render settings(optional) 
    GL.glPointSize(16) 
  def update(self):

    # select program to use when rendering 
    GL.glUseprogram(self.programRef)
    #renders geometric object(s) using program
    GL.glDrawArrays(GL.GL_POINTS,0,1)

#create an instance of this class and run the program

Test().run()
# https://github.com/Namanskshetty/pyopengl
