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
        self.variableRef= glGetUnifromLocation(programRef,varaibleName)
    #store data in unifrom varaible
    def uploadData(self):
        #if the variable does not exist ,ecit
        if self.variableRef==-1:
            return
        if self.dataType=="int":
            glUnifrom1i(self.variableRef,self.data)
        if self.dataType=="bool":
            glUnifrom1i(self.variableRef,self.data)        
        if self.dataType=="float":
            glUnifrom1f(self.variableRef,self.data)       
        if self.dataType=="vec2":
            glUnifrom2f(self.variableRef,self.data)       
        if self.dataType=="vec3":
            glUnifrom3f(self.variableRef,self.data)  
        if self.dataType=="vec4":
            glUnifrom4f(self.variableRef,self.data)  
        else:
            raise Exception("unkown uniform datatype "+self.dataType)





                  
