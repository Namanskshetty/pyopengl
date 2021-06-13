from OpenGL.GL import *

class Uniform(object):

    def __init__(self, dataType,data):
        #type of data
        # int|bool|flaat|vec2|vec3|vec4
        self.dataType = dataType

        # data to be sent to uniform variable
        self.data=data=data
        #ref for varaible location in program
        self.variableRef=None

    # get and store reference to uniform variable
    def locateVariable(self,programRef,varaibleName):
        self.variableRef= glGetUniformLocation(programRef,varaibleName)
    #store data in unifrom varaible
    def uploadData(self):
        #if the variable does not exist ,ecit
        if self.variableRef==-1:
            return
        if self.dataType=="int":
            glUniform1i(self.variableRef,self.data)
        elif self.dataType=="bool":
            glUniform1i(self.variableRef,self.data)        
        elif self.dataType=="float":
            glUniform1f(self.variableRef,self.data)       
        elif self.dataType=="vec2":
            glUniform2f(self.variableRef,self.data[0],self.data[1])  
        elif self.dataType=="vec3":
            glUniform3f(self.variableRef,self.data[0],self.data[1],self.data[2])  
        elif self.dataType=="vec4":
            glUniform4f(self.variableRef,self.data[0],self.data[1],self.data[2],self.data[3])  
        else:
            raise Exception("unkown uniform datatype "+self.dataType)
