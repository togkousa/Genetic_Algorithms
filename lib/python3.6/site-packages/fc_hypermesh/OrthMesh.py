""" ==============
    class OrthMesh
    ==============
    
    The aim of the class `OrthMesh` is to use functions of the `CartesianGrid` module  for 
    creating regular tessallations with simplices or orthotopes of an d-orthope and all 
    its m-faces (0<=m<=d).
"""

import numpy as np
from fc_tools.others import isModuleFound,LabelBaseName

class OrthMesh:
  """ 
    ==============
    class OrthMesh
    ==============
    
    The aim of the class `OrthMesh` is to use functions of the `CartesianGrid` 
    module  for creating regular tessallations with simplices or orthotopes of 
    an d-orthope and all its m-faces (0<=m<=d).
    The d-orthope to mesh is given in R^d by
      Oh=[a_1,b_1]x...x[a_d,b_d]
  
    Class attributes (main)
    -----------------------
    d     space dimension (integer).
    N     number of discretization in each space dimension or list of d 
          integers: one value by space dimension.
    type  type of the mesh elements, 'simplicial'(default) or 'orthotope' 
          (string).
    box   box corresponding to the d-orthotope to mesh. Could be given by a 
          2D list or array such that 
             a_i=box[i-1][0] and b_i=box[i-1][1]
          or
             a_i=box[i-1,0] and b_i=box[i-1,1]
    Mesh  main mesh as an `EltMesh` object, ``Mesh.q`` is the vertices array 
          and ``Mesh.me`` the connectivity array.
    Faces list of list of EltMesh objects. Faces[i] contains all meshes representing
          all  (d-i)-faces of the d-orthotope Oh. The k-th (d-i)-face is given
          by the `EltMesh` object ``Faces[i][k]``: its vertices array is 
          ``Faces[i][k].q`` and its the connectivity array ``Faces[i][k].me``.
          By construction, we have
             Mesh.q[:,Faces[i][k].toGlobal] == Faces[i][k].q
          
    Class properties
    ----------------
    constructor: ``Th=OrthMesh(d,N,**kwargs)``
          
  """
  
  def __init__(self,d,N,**kwargs):
    """ Th=OrthMesh(d,N,**kwargs)
        
        Parameters
        ----------
        d     space dimension 
        N     either a 1D array/list of length `d` such that `N[i-1]` is the number 
              of discretization for `[a_i,b_i]` or either an integer if the number 
              of discretization is the same in all space directions.
        
        Optional key/value parameters
        -----------------------------
        box=[[a_1,b_1],[a_2,b_2],...,[a_d,b_d]]
            Use to set the d-orthotope. By default, the unit reference d-hypercube
            is choosed: [0,1]^d
        type=value
            If value=='orthotope' then the tessallation is done with orthotopes.
            If value=='simplicial' then the tessallation is done with simplices.
        mapping=mapfun
            mapfun is a mapping function.
            
        :example:
        
        >>> Th=OrthMesh(3,[5,3,4])
        >>> Th.Mesh
        EltMesh object 
            type (str): simplicial
            type : 0
              d : 3
              m : 3
              q : (3,120)
              me : (4,360)
        >>> Th.Faces[1][0]
        EltMesh object 
            type (str): simplicial
            type : 0
              d : 3
              m : 1
              q : (3,5)
              me : (2,4)
        >>> Th.Mesh.q[:,Th.Faces[1][0].toGlobal] == Th.Faces[1][0].q
        array([[ True,  True,  True,  True,  True],
               [ True,  True,  True,  True,  True],
               [ True,  True,  True,  True,  True]], dtype=bool)
        
    """
    import fc_hypermesh.CartesianGrid as CG
    from fc_hypermesh.EltMesh import EltMesh
    from fc_tools.colors import selectColors

    ctype=kwargs.get('type', 'simplicial' )
    box=kwargs.get('box',np.ones((d,1))*np.array([0,1]))
    m_min=kwargs.get('m_min',0)
    mapping=kwargs.get('mapping',None)

    N=np.atleast_1d(N)
    assert len(N)==1 or len(N)==d
    if len(N)==1:
      N=N[0]*np.ones(d)
    if (ctype=='orthotope'):
      funMesh = lambda N: CG.TessHyp(N)
      funFaces = lambda N,m: CG.TessFaces(N,m)
      ntype=1
    else: # default 'simplicial'
      funMesh = lambda N: CG.Triangulation(N)
      funFaces = lambda N,m: CG.TriFaces(N,m)
      ntype=0
    self.d=d
    self.box=np.array(box,dtype=float)
    assert self.box.shape==(d,2)
    self.type=ctype
    [q,me]=funMesh(N)
    trans=lambda Q: MappingBox(Q,N,box)
    if mapping is not None:
      my_mapp=lambda Q: mapping(trans(Q))
    else:
      my_mapp=trans
    self.Mesh=EltMesh(d,d,my_mapp(q),me,label=1,type=ntype)
    self.set_box()
    self.Faces=[]
    i=0
    for m in np.arange(d-1,m_min-1,-1):
      self.Faces.append(funFaces(N,m))
      nsTh=len(self.Faces[i])
      colors = selectColors(nsTh)
      for j in np.arange(nsTh):
        self.Faces[i][j].q=my_mapp(self.Faces[i][j].q)
        self.Faces[i][j].label=j+1
        self.Faces[i][j].color=colors[j]
        self.Faces[i][j].type=ntype
      i+=1
      
  def __repr__(self):
    strret = ' %s object \n'%self.__class__.__name__ 
    strret += '      d : %d\n'%self.d 
    strret += '  Mesh  : %s\n'%str(self.Mesh)
    for F in self.Faces:
      strret += ' Number of %d-faces : %d\n'%(F[0].m,len(F))
      i=0
      for f in F:
        strret += '   [%2d] (type,nq,nme) : (%s,%d,%d)\n'%(i,f.strtype(),f.nq,f.nme)
        i+=1
    return strret         
   
  def getFacesIndex(self,m): # must be improved
    A=np.array(np.arange(self.d-1,-1,-1))
    return np.where(A==m)[0][0]
  
  def set_box(self):
    for i in range(self.d):
      self.box[i,0]=np.min(self.Mesh.q[i])
      self.box[i,1]=np.max(self.Mesh.q[i])
   
  def plotmesh(self,**kwargs):
    """ plotmesh(self,**kwargs)
    
    """
    if not isModuleFound('matplotlib'):
      print('plotmesh needs matplotlib package!')
      return
    import matplotlib.pyplot as plt
    if self.d > 3:
      print('Unable to plot in dimension %d > 3!'%self.d)
      return
    m=kwargs.pop('m',self.d)
    assert m in range(self.d+1)
    legend=kwargs.pop('legend', False);
    fig=plt.gcf()
    if m==self.d:
      Legend_handle,Labels=self.Mesh.plotmesh(**kwargs)
      Legend_handle=[Legend_handle]
      Labels=[Labels]
    else:
      Legend_handle=[];Labels=[]
      idx=self.getFacesIndex(m)
      F=self.Faces[idx]
      nF=len(F);
      for i in range(nF):
        Leg,Lab=F[i].plotmesh(**kwargs)
        Legend_handle.append(Leg)
        Labels.append(Lab)
    fig = plt.gcf()
    ax=fig.axes[0]
    if self.d==3:
      ax.set_zlim(self.box[2,0],self.box[2,1])
    ax.set_xlim(self.box[0,0],self.box[0,1])
    ax.set_ylim(self.box[1,0],self.box[1,1]) 
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    if self.d==3:
      ax.set_zlabel('z')
    #-> No background
    ax.patch.set_facecolor('None')
    fig.patch.set_visible(False) 
    #<-
    if legend:
      plt.legend(Legend_handle,Labels,loc='best', ncol=int(len(Legend_handle)/10)+1).draggable()
      
def MappingBox(q,N,box):
  box=np.array(box,dtype=float)
  d=len(N)
  
  for i in range(d):
    q[i]=box[i,0]+(box[i,1]-box[i,0])/(1.*N[i])*q[i] #BUG: take care with whole division
  return q