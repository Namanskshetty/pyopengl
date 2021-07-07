class Geometry(object):
  def __init__(self):
    #sict to setattr
    self.attribute={}
    #no of verticses
    self.vertexCount = None
  def countVertices(self):
    #the no of vertices in length of any
    #attribute object array of data
    attrib = list(self.attributes.values())[0]
    self.vertexCount=len( attrib.data )
