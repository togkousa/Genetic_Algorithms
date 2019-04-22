import matplotlib.pyplot as plt
import numpy as np
#from mpl_toolkits.mplot3d import Axes3D
from scipy import linalg,sparse
from scipy.sparse.linalg import spsolve
import itertools
from math import factorial
#import matplotlib
#from matplotlib.patches import Polygon,Patch
#from mpl_toolkits.mplot3d import Axes3D
#import mpl_toolkits.mplot3d as a3
#from mpl_toolkits.mplot3d.art3d import Poly3DCollection,Line3DCollection
from fc_tools.colors import selectColors
#from fc_tools.graphics import isMayavi

def comb(n,k):
  import itertools
  return np.array([x for x  in itertools.combinations(np.arange(n),k)],dtype=int)

def issiMeshElt(sTh):
  return isinstance(sTh,siMeshElt)

class siMeshElt:
  def __init__(self):
     self.d=0
     self.dim=0
     self.nq=0
     self.nme=0
     self.q=None
     self.me=None
     self.dglobal=0
     self.toGlobal=None
     self.nqGlobal=0
     self.toParent=None
     self.nqParent=0
     self.nqParents=[] # nqParents[i]  i=0: parent, i=1:parent of parent, ...
     self.toParents=[]
     self.label=0
     self.Tag=''
     self.color=[]
     self.vols=None
     self.gradBaCo=None
     self.geolab =[]
     self.partlab=[]
     self.bbox=[]
     self.h=0
     
  def __init__(self,dim,d,label,q,me,toGlobal,nqGlobal,geolab,partlab):
     self.dim=dim
     self.d=d
     self.label=label
     self.q=q
     self.nq=q.shape[0]
     self.me=me
     self.nme=me.shape[1]
     self.dglobal=0
     self.toGlobal=toGlobal
     self.nqGlobal=nqGlobal
     self.toParent=toGlobal 
     self.nqParent=nqGlobal
     self.nqParents=[nqGlobal] # nqParents[i]  i=0: parent, i=1:parent of parent, ...
     self.toParents=[toGlobal]
     self.geolab=geolab
     self.partlab=partlab
     self.color=[]
     self.Tag=''
     self.ComputeVolVec()
     self.GetMaxLengthEdges()
     self.GradBaCo()
     #self.vols=ComputeVolVec(self.d,self.q,self.me)
     #self.gradBaCo=GradBaCo(self.d,self.q,self.me)
     #self.h=GetMaxLengthEdges(self.q,self.me)
     self.bbox=np.zeros((2*dim,)) # bounding box
     for i in range(dim):
       self.bbox[2*i]=min(q[:,i])
       self.bbox[2*i+1]=max(q[:,i])
     
  def __repr__(self):
    strret = ' %s object \n'%self.__class__.__name__ 
    strret += '      d : %d\n'%self.d 
    strret += '    dim : %d\n'%self.dim 
    strret += '  label : %d\n'%self.label
    strret += '     nq : %d\n'%self.nq
    strret += '    nme : %d\n'%self.nme
    strret += 'nqGlobal: %d\n'%self.nqGlobal
    strret += '      q : size=%s\n'%self.q.shape.__repr__()
    strret += '     me : size=%s\n'%self.me.shape.__repr__()
    strret += 'toGlobal: size=%s\n'%self.toGlobal.shape.__repr__()
    return strret  
  
  def feval(self,fun,**kwargs):
    Global=kwargs.get('global', False)
    dtype=kwargs.get('dtype', float)
    assert np.isscalar(fun) or isinstance(fun, type(lambda: None)) or isinstance(fun,np.lib.function_base.vectorize) or isinstance(fun,list), "1st argument must be a scalar, a def function, a lambda function or a list (of functions). Given a %s"%str(fun)
    if isinstance(fun,list):
      V=[]
      for i in range(len(fun)):
        V.append(self.feval(fun[i]))
      return np.array(V)  
    nargin=get_func_nargin(fun)
    if nargin is not None: # fun is a 'def' function or a 'lambda' function
      assert nargin==1 or nargin==self.dim, "1st argument is a function function and must have 1 or %d input arguments"%nargin
      if nargin==self.dim:
        fun=np.vectorize(fun)
        S='fun(self.q[:,0]'
        for i in range(1,self.dim):
          S=S+',self.q[:,'+str(i)+']'
        S=S+')'
        V=eval(S)
      else:
        V=fun(self.q.T)
      fun=V # With constant functions, V is a scalar!
    if np.isscalar(fun):
      if Global:
        V=fun*np.ones((self.nqGlobal,),dtype=dtype)
      else:
        V=fun*np.ones((self.nq,),dtype=dtype)
    return V
  
  def eval(self,f,**kwargs):
    """ Eval f on siMeshElt object and return a numpy array with shape (self.nq,)
      corresponding on the evaluate of f on each mesh vertices (if f is not a 
      list and not None)
      
      f could be:
        - a scalar
        - a def function
        - a lambda function
        - a numpy.vectorize function
        - a numpy array 
        - a list where each element could be on of the previous type
    """
    if f is None:
      return None
    dtype=kwargs.get('dtype', float)
    Num=kwargs.get('Num', 1)
    if np.isscalar(f):
      return f*np.ones((self.nq,),dtype=dtype)
    if isinstance(f, type(lambda: None)) or isinstance(f,np.lib.function_base.vectorize):
      V=self.feval(f)
      return self.feval(f)
    if isinstance(f,np.ndarray) and (f.shape[0]==self.nq) :
      return f
    if isinstance(f,list): # Vector Field case
      n=len(f)
      Fh=np.zeros((n*self.nq,));I=np.arange(self.nq)
      VFInd=getVFindices(Num,n,self.nq)
      for i in range(n):
        Fh[VFInd(I,i)]=self.eval(f[i])
      return Fh
    else:
      assert False
    

  def ComputeVolVec(self):
    # AJHanson_Geometry_for_N-Dimensional, (5) page 156 Graphics Gems IV edited by Paul S. Heckbert, 
    # published by Academic Press Limited
    # Introduction to the geometry of N Dimensions by D. M. Y. Sommerville (1929)
    if self.d==0:
      self.vols=1
      return
    d=self.d;q=self.q;me=self.me;nme=self.nme;
    X=np.zeros((d,nme,self.dim))
    #print(X.shape)
    for i in range(d):
      X[i]=q[me[i+1]]-q[me[0]]
    V=np.zeros((d,d,nme))
    for i in range(d):
      V[i,i]=(X[i]*X[i]).sum(axis=1)
      for j in range(i+1,d):
        V[i,j]=V[j,i]=(X[i]*X[j]).sum(axis=1)
    self.vols=np.array([np.sqrt(abs(linalg.det(V[::,::,k])))/factorial(d) for k in range(nme)])
 
  def GetMaxLengthEdges(self):
    ne=self.d+1;q=self.q;me=self.me
    h=0.
    for i in range(ne):
      for j in range(i+1,ne):
        h=max(h,np.sum((q[me[i]]-q[me[j]])**2,axis=1).max())
    self.h=np.sqrt(h)
    
  def GradBaCo(self):
    d=self.d;dim=self.dim
    nme=self.nme;q=self.q;me=self.me
    A=np.zeros((d,dim,nme))
    I=np.zeros((d,dim,nme),dtype=int)
    J=np.zeros((d,dim,nme),dtype=int)
    L=np.arange(nme)
    for i in range(d):
      A[i]=(q[me[i+1]]-q[me[0]]).T
      I[i]=np.tile(L*d+i,(dim,1))
      for j in range(dim):
        J[i,j]=L*dim+j
    N=d*dim*nme
    spA=sparse.csc_matrix((np.reshape(A,N),(np.reshape(I,N),np.reshape(J,N))),shape=(d*nme,dim*nme))
    spH=spA*spA.T
    Grad=np.hstack([-np.ones((d,1)),np.eye(d)])
    b=np.tile(Grad,(nme,1))
    #G=spsolve(spH,b)
    GradBaCo=spA.T*spsolve(spH,b)
    self.GradBaCo=GradBaCo.reshape((nme,dim,d+1)).swapaxes(1,2)
  
  def NormalFaces(self):
    d=self.d
    #(IndLocFaces,IndOpositePt)=getIndLocFaces(d)
    Normal=np.zeros((d+1,self.dim,self.nme))
    for i in range(d+1):
      #A=-self.GradBaCo[:,IndOpositePt[i],:]
      A=-self.GradBaCo[:,i,:]
      Normal[i,:,:]=A.T
      N2=np.sqrt(np.sum(A**2,axis=1))
      for j in range(self.dim):
        Normal[i,j,:]=Normal[i,j,:]/N2
    return Normal
      
  def barycenters(self):
    Ba=np.zeros((self.dim,self.nme))
    for i in range(self.d+1):
      Ba+=self.q[self.me[i]].T
    Ba/=(self.d+1)
    return Ba
  
  def move(self,U):
    self.q=move_mesh(self,U)
  
def move_mesh(sTh,U):
  Q=sTh.q
  if U is None:
    return Q
  assert(len(U)==sTh.dim)
  if len(U[0])==sTh.nqGlobal:
    for i in range(sTh.dim):
      Q[:,i]+=U[i][sTh.toGlobal]
  else:
    assert( len(U[0]) == sTh.nq )
    for i in range(sTh.dim):
      Q[:,i]+=U[i]
  return Q    
  
def getIndLocFaces(d):
  IndLocFaces=comb(d+1,d)
  IndOpositePt=np.zeros(d+1,dtype=int)
  I=np.arange(d+1)
  for i in range(d+1):
    IndOpositePt[i]=np.setdiff1d(I,IndLocFaces[i])
  return  IndLocFaces,IndOpositePt

def mesh_label(sTh):
  assert issiMeshElt(sTh), "First argument must be a siMeshElt object"
  return 'd=%d, lab=%d'%(sTh.d,sTh.label)

def getLocalValue(sTh,u):    
  if len(u)==sTh.nqGlobal:
    U=u[sTh.toGlobal]
  elif len(u)==sTh.nqParent:
    U=u[sTh.toParent]
  else:
    assert( len(u) == sTh.nq )
    U=u
  return U.ravel()

def getLocalVector(sTh,V): # V : list of n vectors
  assert isinstance(V,list)
  n=len(V)
  Vl=n*[None]
  for i in range(n):
    Vl[i]=getLocalValue(sTh,V[i])
  return Vl

def get_func_nargin(f):
  #assert  isinstance(f, type(lambda: None)) or isinstance(f,np.lib.function_base.vectorize), "1st argument must be a def function or a lambda function. Given a %s"%str(fun)
  if isinstance(f, type(lambda: None)): # fun is a 'def' function or a 'lambda' function
    return f.__code__.co_argcount
  if isinstance(f,np.lib.function_base.vectorize):
    return f.pyfunc.__code__.co_argcount
  return None