""" =======
    EltMesh
    =======
    
    Only contains the `EltMesh` class used by `OrthMesh` class.
"""

from fc_tools.others import isModuleFound

class EltMesh:
  """ class EltMesh
  
      This class is used to store an elementary mesh given by its vertices array `q` and 
      its connectivity array `me`
      
      see description in `Class object OrthMesh` in the report.
  """
  def __init__(self,d,m,q,me,**kwargs):
    import numpy as np
    color=kwargs.get('color', [0,0,1] )
    label=kwargs.get('label', '' )
    type=kwargs.get('type', None)
    toGlobal=kwargs.get('toGlobal', None)
    assert  m <= d 
    assert q.shape[0]==d 
    self.d=d
    self.m=m
    self.q=q
    self.me=me
    if type is None:
      if (me.shape[0]==m+1): # m-simplicial
        self.type=0
      elif (me.shape[0]==2**m): # m-orthotope
        self.type=1;
      else:
        raise NameError('Trouble with "me" dimension!')
    else:
      assert type in [0,1]
      assert ( (type==0) and (me.shape[0]==m+1) ) or ( (type==1) and (me.shape[0]==2**m) ) 
      self.type=type
      
    self.nq=q.shape[1]
    self.nme=me.shape[1]
    if toGlobal is None:
      self.toGlobal=None
    else:
      self.toGlobal=np.array(toGlobal,dtype=int)
    
    self.color=color
    self.label=label
  def __repr__(self):
    strret = ' %s object \n'%self.__class__.__name__ 
    strret += '    type (str): %s\n'%self.strtype()
    strret += '    type : %d\n'%self.type
    strret += '       d : %d\n'%self.d 
    strret += '       m : %d\n'%self.m
    strret += '       q : (%d,%d)\n'%self.q.shape
    strret += '      me : (%d,%d)\n'%self.me.shape
   # strret += 'toGlobal : (%d,)\n'%self.toGlobal.shape
    return strret  

  def strtype(self):
    if self.type==0:
      return 'simplicial'
    if self.type==1:  
      return 'orthotope'
    return 'unknow'
  
  if isModuleFound('matplotlib'):
    from .Matplotlib import plotmesh

