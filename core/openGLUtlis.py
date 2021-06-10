from OpenGL import GL

# static meathod to load/compile openGl shaders
# also link to create GPU programs

class OpenGLUtlis(object):

  @staticmethod #for the static meathod
  def initlizeShader(shaderCode,shaderType):
    #specifing opengl version
    extension="#extension GL_ARB_shading_language_420pack: require \n"
    shaderCode="#version 130 \n" + extension + shaderCode

    #create a empty dhaser obj and return ref Value
    shaderRef=GL.glCreateShader(shaderType)
    # store source code in shader 
    GL.glShaderSource(shaderRef,shaderCode)
    #compile source code stored in shader
    GL.glCompileShader(shaderRef)
    #query weather compulation was sucessfull
    compileSuccess=GL.glGetShaderiv(shaderRef,GL.GL_COMPILE_STATUS)
    if not compileSuccess:
      #retrive error 
      errorMessage=GL.glGetShaderInfoLog(shaderRef)
      # free memory used to store shader program
      GL.glDeleteShader(shaderRef)
      #convert byte str to char str
      errorMessage="\n" +errorMessage.decode("utf-8")
      #print error msg and Stop
      raise Exception(errorMessage)
    #compilation was sucessfull 
    return shaderRef

  @staticmethod
  def initlizeProgram(vertexShaderCode,fragmentShaderCode):
    #compiler shaders and syore ref
    vertexShaderRef=OpenGLUtlis.initlizeShader(vertexShaderCode,GL.GL_VERTEX_SHADER)
    fragmentShaderRef=OpenGLUtlis.initlizeShader(fragmentShaderCode,GL.GL_FRAGMENT_SHADER)
    #CREATE PRO object
    programRef=GL.glCreateProgram()
    #attach previously compiled shaders
    GL.glAttachShader(programRef,vertexShaderRef)
    GL.glAttachShader(programRef,fragmentShaderRef)
    #link the vertexshader to frag shaderCode
    GL.glLinkProgram(programRef)

    #query if link was successfull
    linkSuccess=GL.glGetProgramiv(programRef,GL.GL_LINK_STATUS)

    if not linkSuccess:
      #retur error msg 
      errorMessage=GL.glGetProgramInfoLog(programRef)
      #free memory use to store prog 
      GL.glDeleteProgram(programRef)
      #convert byte str to char str
      errorMessage="\n" +errorMessage.decode("utf-8")
      #print error msg and Stop
      raise Exception(errorMessage)
    #linking was sucessfull 
    return programRef      

#https://github.com/namanskshetty/pyopengl
