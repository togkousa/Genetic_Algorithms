import sys
import numpy as np
from math import factorial
from fc_simesh.siMeshElt import siMeshElt
from fc_oogmsh.gmsh import ooGmsh,EltTypeSimplex
from fc_tools.colors import selectColors
from fc_hypermesh.OrthMesh import OrthMesh

# Medit format Name
simplices_dict={'Vertices':0,'Edges':1,'Triangles':2,'Tetrahedra':3}

def issiMesh(Th):
  return isinstance(Th,siMesh)

class siMesh:    
  def __init__(self,gmsh_file=None,**kwargs):
     self.d=0
     self.dim=0
     self.order=0
     self.sTh=[]
     self.nsTh=0
     self.toGlobal=[]
     self.toParent=[]
     self.sThsimp=[]
     self.sThlab=[]
     self.sThcolors=[]
     self.bbox=[] # Bounding box
     self.sThgeolab=[]
     self.sThphyslab=[]
     self.sThpartlabs={}
     self.M=[]
     self.sElts=[]
     self.nq=0
     if gmsh_file==None:
       return
     try:
       fid = open(gmsh_file, "r")
     except IOError:
       print("File '%s' not found." % (gmsh_file))
       sys.exit()
     isPhysical=kwargs.get('isPhysical', True)
     dim=kwargs.get('dim', 2)
     d=kwargs.get('d', None)
     mapping=kwargs.get('mapping', None)
     trans=kwargs.get('trans', None) #old option
     mapping=kwargs.get('mapping', trans)
     self.readgmsh(gmsh_file,dim,d,isPhysical,mapping)
     self.set_all()
          
  def __repr__(self):
    strret = ' %s object \n'%self.__class__.__name__ 
    strret += '      d : %d\n'%self.d 
    strret += '    dim : %d\n'%self.dim
    strret += '    nq  : %d\n'%self.nq
    strret += '    nme : %d\n'%self.get_nme()
    strret += '    sTh : %s of %d %s\n'%(self.sTh.__class__.__name__,len(self.sTh),self.sTh[0].__class__.__name__)
    strret += '   nsTh : %d\n'%self.nsTh
    strret += 'sThsimp : %s %s\n'%(str(self.sThsimp.shape),self.sThsimp.__class__.__name__)
    strret += '   '+np.array_str(self.sThsimp).replace('\n','\n          ')+'\n'
    strret += ' sThlab : %s %s\n'%(str(self.sThlab.shape),self.sThlab.__class__.__name__)
    strret += '   '+np.array_str(self.sThlab).replace('\n','\n          ')+'\n'
    return strret         
  
  def readgmsh(self,gmsh_file,dim,d,isPhysLabel,trans):
    self.dim=dim
    G=ooGmsh(gmsh_file)
    #Q=G.q
    if trans is not None:
      if trans.__code__.co_argcount==1:
        G.q=trans(G.q)
      elif trans.__code__.co_argcount==2:
        G.q=trans(G.q[:,0],G.q[:,1])
      elif trans.__code__.co_argcount==3:
        G.q=trans(G.q[:,0],G.q[:,1],G.q[:,2])
      else:
        print('Error with trans function')
      if isinstance(G.q,list):
        assert len(G.q) == G.dim
        G.q=np.array(G.q).T # nq-by-dim array
    #print(Q-G.q)  
    if G.dim!=dim:
      print('  Mesh %s is a %d-dimensional mesh\n    Force dimension to %d\n'%(gmsh_file,G.dim,G.dim))
      self.dim=G.dim
    if d==None:
      #d=[dim,dim-1]
      d=np.arange(self.dim,-1,-1)
    #self.d=max(d)
    self.toGlobal=G.toGlobal
    self.nq=G.toGlobal.shape[0]
    self.toParent=G.toGlobal
    self.M=G.M
    self.sElts=G.sElts
    
    for i in range(len(G.sElts)):
      dd=EltTypeSimplex(G.sElts[i].type)
      if (dd != None ) and (dd in d):
        nme=G.sElts[i].me.shape[1]
        if G.sElts[i].part_lab[0]==None:
          if isPhysLabel:
            mel=G.sElts[i].phys_lab
          else:
            mel=G.sElts[i].geo_lab
        else:
          print('to do')
       
        self.AddsiMeshElts(dd,G.q,nme,G.sElts[i].me,mel)#,geolab=G.sElts[i].GeometricalLabel,partlab=G.sElts[i].part_lab)
    self.sThsimp=np.array(self.sThsimp,dtype=int)
    self.sThlab=np.array(self.sThlab,dtype=int)
    self.d=max(self.sThsimp)
                           
  def AddsiMeshElts(self,d,q,nme,me,mel,**kwargs):
    Geolab=kwargs.get('geolab', None)
    Partlab=kwargs.get('partlab', None)
    labels=np.unique(mel)
    geolab=None
    partlab=None
    k=self.nsTh;
    nq=q.shape[0]
    if d==self.d:
      self.toParent=np.unique(np.concatenate((self.toParent,me.flatten())))
      self.toGlobal=self.toParent
    for i in range(len(labels)):
       I=(mel==labels[i]).nonzero()[0]
       ME=me[:,I]  
       if Geolab!=None:
         geolab=Geolab[I]
       if Partlab!=None:
         partlab=Partlab[I]
       indQ=np.unique(ME)
       Q=q[indQ]
       lQ=np.arange(0,len(indQ))
       J=np.zeros((nq,),dtype=int)
       J[indQ]=lQ
       MELoc=J[ME]
       self.sTh.append(siMeshElt(self.dim,d,labels[i],Q,MELoc,indQ,nq,geolab,partlab))
       self.sThsimp.append(d)
       self.sThlab.append(labels[i])
       self.nsTh+=1
       
       
  def AddCopysiMeshElt(self,ooElt):
    if len(np.intersect1d(self.toGlobal,ooElt.toGlobal))==len(ooElt.toGlobal):
      self.nsTh+=1
      k=self.nsTh
      from copy import deepcopy
      self.sTh.append(deepcopy(ooElt))
      #self.sThlab=np.append(self.sThlab,ooElt.label)
      #self.sThsimp=np.append(self.sThsimp,ooElt.d)
      self.sThlab.append(ooElt.label)
      self.sThsimp.append(ooElt.d)
      
  def AddsiMeshElt(self,ooElt):
    if self.sTh != []:
      #print(np.intersect1d(self.toGlobal,ooElt.toGlobal).shape)
      if not isinstance(ooElt.toGlobal,np.ndarray):
        ooElt.toGlobal=np.array([ooElt.toGlobal],dtype=int)
      #print(ooElt.toGlobal)
      #ooElt.toGlobal=np.array(ooElt.toGlobal,dtype=int)
      #print(ooElt.toGlobal)
      I=np.intersect1d(self.toGlobal,ooElt.toGlobal)
      if I.shape[0]!=1:
        #assert( len(ooElt.toGlobal)==1 )
      #else:
        assert( I.shape==ooElt.toGlobal.shape )
      #assert(len(np.intersect1d(self.toGlobal,ooElt.toGlobal))==len(ooElt.toGlobal))
      N=self.nsTh+1
    else:
      N=1;
      self.toGlobal=ooElt.toGlobal
      self.nq=ooElt.nq
    self.nsTh=N
    self.sTh.append(ooElt)
    self.sThlab.append(ooElt.label)
    self.sThsimp.append(ooElt.d)
      
  def find(self,d,labels=None):
    #sThsimp=np.array(self.sThsimp) # A l'arrache
    #sThlab=np.array(self.sThlab)
    ind=(self.sThsimp==d).nonzero()[0]
    if ind.shape[0]==0:
      return None
    if labels is None:
      return ind
    if isinstance(labels,int) or isinstance(labels,np.int64):
      I=np.where(self.sThlab[ind]==labels)[0]
      if I.shape[0]==1:
        return ind[I[0]]
      else:
        return None
    isList=False
    if isinstance(labels,list):
      islist=True
    labels=np.array(labels)
    Ind=[]
    for i in range(len(ind)):
      if self.sThlab[ind[i]] in labels:
        Ind.append(ind[i])
    if not isList:
      Ind=np.array(Ind)
    return Ind
  
  def set_nq(self):
    idxdom=self.find(self.d)
    assert(len(idxdom)>0)
    if len(idxdom)==1:
      self.nq=self.sTh[idxdom[0]].nq
      return
    toG=[]
    for i in idxdom:
      toG.append(self.sTh[i].toGlobal)
    self.nq=np.unique(np.concatenate(toG)).shape[0]
                           
  def set_colors(self):
    self.sThcolors=np.zeros((self.nsTh,3));
    for d in range(self.d+1):
      Ilab=self.find(d)
      if Ilab is not None:
        self.sThcolors[Ilab]=selectColors(len(Ilab))
        for jlab in Ilab:
          self.sTh[jlab].color=self.sThcolors[jlab]
          
  def set_bbox(self):
    self.bbox=self.sTh[0].bbox
    for k in range(self.nsTh):
      bb=self.sTh[k].bbox
      for i in range(self.dim):
        self.bbox[2*i]=min(self.bbox[2*i],bb[2*i])
        self.bbox[2*i+1]=max(self.bbox[2*i+1],bb[2*i+1])
   
  def set_dglobal(self):
    for k in range(self.nsTh):
      self.sTh[k].dglobal=self.d
      
  def set_all(self):
     #self.sThlab=np.array(self.sThlab)
     #self.sThsimp=np.array(self.sThsimp)
     self.set_nq()
     self.set_colors()
     self.set_bbox()
     self.set_dglobal()
      
  def get_nme(self):
    Ilab=self.find(self.d)
    nme=0
    for jlab in Ilab:
      nme+=self.sTh[jlab].nme
    return nme
  
  def get_h(self):
    Ilab=self.find(self.d)
    h=0
    for jlab in Ilab:
      h=max(self.sTh[jlab].h,h)
    return h
  
  def move(self,U):
    if isinstance(U,list):
      assert len(U)==self.dim
      V=np.array(U)
    elif isinstance(U,np.ndarray):
      V=U
    else:
      assert False
    assert (V.shape[0]==self.dim) and (V.shape[1]==self.nq)
    for i in range(self.nsTh):
      self.sTh[i].move(V)
  
  
  def feval(self,fun,**kwargs):
    """ Eval a def function or a lambda function on siMesh object
    """
    d=kwargs.get('d', self.d)
    if isinstance(fun,list):
      U=[]
      for f in fun:
        U.append(self.feval(f,**kwargs))
      return np.array(U)
    labels=kwargs.get('labels', self.sThlab[self.find(d)])
    U=np.zeros((self.nq,))
    for l in labels:
      k=self.find(d,labels=l)
      if k is not None:
        U[self.sTh[k].toGlobal]=self.sTh[k].feval(fun)
    return U
  
  def eval(self,f,**kwargs):
    """ Eval f on siMesh object and return a numpy array with shape (self.nq,)
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
  
  def barycenters(self,**kwargs):
    d=kwargs.get('d', self.d)
    labels=kwargs.get('labels', self.sThlab[self.find(d)])
    idxlab=self.find(d,labels)
    Ba=np.zeros((self.dim,len(idxlab)))
    j=0
    for i in idxlab:
      Ba[:,j]=np.mean(self.sTh[i].barycenters(),axis=1)
      j+=1
    return Ba
  
  def merge_vertices(self,**kwargs):
    d=kwargs.pop('d', self.d)
    labels=kwargs.pop('labels', self.sThlab[self.find(d)])
    toGlobal=[]
    Q=np.zeros((self.nq,self.dim))
    for l in labels:
      k=self.find(d,labels=[l])
      if len(k)==1:
        toGlobal=np.hstack((toGlobal,self.sTh[k[0]].toGlobal))
        Q[self.sTh[k[0]].toGlobal]=self.sTh[k[0]].q 
    toGlobal=np.int32(np.unique(toGlobal))
    Q=Q[toGlobal].T
    return Q,toGlobal
  
  def get_mesh(self,**kwargs):
    """
      
    """
    d=kwargs.pop('d', self.d)
    labels=kwargs.pop('labels', self.sThlab[self.find(d)])
    idxlab=self.find(d,labels=labels)
    if not isinstance(idxlab,list) and not isinstance(idxlab,np.ndarray):
      idxlab=[idxlab]
    toGlobal=[]
    ME=np.zeros((d+1,0),dtype=int)
    Q=np.zeros((self.nq,self.dim))
    for k in idxlab:
      toGlobal=np.hstack((toGlobal,self.sTh[k].toGlobal))
      Q[self.sTh[k].toGlobal]=self.sTh[k].q
      ME=np.hstack((ME,self.sTh[k].toGlobal[self.sTh[k].me]))
      
    toGlobal=np.int32(np.unique(toGlobal))
    Q=Q[toGlobal]
    N=len(toGlobal)
    idx=np.zeros((self.nq,),dtype=int)
    idx[toGlobal]=np.arange(N,dtype=int)
    ME=idx[ME]
    return Q,ME,toGlobal

     
  #from fc_simesh_matplotlib.siMesh import plotmesh,plot,plotGradBaCo,plotiso
  #if isMayavi(): 
    ##from fc_simesh.toolsmesh.vtk import vtkPlot,vtkPlotVal
    #from fc_simesh_mayavi.siMesh import vtk_plotmesh, vtk_slicemesh, vtk_plot, vtk_iso_surface, vtk_slice, vtk_sliceiso, vtk_plotiso, vtk_quiver, vtk_streamline
      
def LabelBaseName(Th,d):
  if (Th.d==Th.dim):
    if (d==Th.d):
      return r"\Omega"
    if (d+1==Th.d):
      return r"\Gamma"
    if (d+2==Th.d):
      return r"\partial\Gamma"
    if (d+3==Th.d):
      return r"\partial^2\Gamma"
  if (Th.d+1==Th.dim):
    if (d==Th.d):
      return r"\Omega"
    if (d+1==Th.d):
      return r"\Gamma"
    if (d+2==Th.d):
      return r"\partial\Gamma"

def HyperCube(d,N,**kwargs):
  mapping=kwargs.get('mapping',None)
  m_min=kwargs.get('m_min',0)
  assert(m_min in range(d+1))
  Oh=OrthMesh(d,N,mapping=mapping,m_min=m_min)
  ooTh=siMesh()
  ooTh.d=ooTh.dim=d
  Th=Oh.Mesh
  ooElt=siMeshElt(d,d,1,Th.q.T,Th.me,np.arange(Th.nq),Th.nq,None,None)
  ooTh.AddsiMeshElt(ooElt)

  for i in range(len(Oh.Faces)):
    for j in range(len(Oh.Faces[i])):
      sTh=Oh.Faces[i][j]
      ooElt=siMeshElt(d,sTh.m,j+1,sTh.q.T,sTh.me,sTh.toGlobal,Th.nq,None,None)
      ooTh.AddsiMeshElt(ooElt)
      
  ooTh.sThsimp=np.array(ooTh.sThsimp)
  ooTh.sThlab=np.array(ooTh.sThlab)
  ooTh.set_all()
  return ooTh

#def vtk_SaveAllFigsAsFiles(filename,**kwargs):
  #tag=kwargs.get('tag', False )
  #figext=kwargs.get('format', 'png' )
  #savedir=kwargs.get('dir', '.' )
  #figs=kwargs.get('figs',None) # list of figures number
  #verbose=kwargs.get('verbose',False)
  #scale=kwargs.get('scale', 1.0 )
  #import sys,os,mayavi
  #from mayavi import mlab
  #if tag:
    #Softname='Python'
    #V=sys.version.split(' ')[0]
    #Release=V.replace('.','')
    #Tag=Softname+Release
    ## FullTag=Tag+'_Mayavi'+mayavi.__version__.replace('.','') 
    
  #if not os.path.exists(savedir):
    #os.makedirs(savedir)
  
  #for i in range(len(figs)):
    #nfig=figs[i]
    #if tag:
      #File=savedir+os.path.sep+filename+'_fig'+str(nfig)+'_'+Tag+'.'+figext
    #else:
      #File=savedir+os.path.sep+filename+'_fig'+str(nfig)+'.'+figext
                   
    #fig=mlab.figure(nfig)
    #old_bg=fig.scene.background
    #fig.scene.background=(1, 1, 1)
    #if verbose:
      #print('  Save Mayavi Scene %d in %s'%(nfig,File))
    #mlab.savefig(File,magnification=scale) 
    #fig.scene.background=old_bg