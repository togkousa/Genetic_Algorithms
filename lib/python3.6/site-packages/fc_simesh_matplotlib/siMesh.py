import matplotlib.pyplot as plt
from matplotlib.patches import Patch
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np

from fc_tools.others import LabelBaseNameSimp
from fc_tools.colors import str2rgb,check_color
from fc_tools.graphics import set_axes
from fc_simesh.siMesh import issiMesh,LabelBaseName
from fc_simesh.siMeshElt import mesh_label

import fc_matplotlib4mesh.simplicial as plt4sim

from . import siMeshElt as sME

def plotmesh(Th,**kwargs):
  assert issiMesh(Th), "First argument must be a siMesh object"
  d=kwargs.pop('d', Th.d)
  latex=kwargs.pop('latex', True)
  all_labels=Th.sThlab[Th.find(d)]
  labels=np.intersect1d(kwargs.pop('labels', all_labels),all_labels)
  if np.isscalar(labels):
    labels=[labels]
  legend=kwargs.pop('legend', False)
  if len(labels)==0:
    print('No submesh found!')
    return
  #plt.rc('text', usetex=True, text.latex.unicode)
  #fig = plt.gcf()
  Legend_handle=[]
  Labels=[]
  LabName=LabelBaseName(Th,d)
  for l in labels:
    k=Th.find(d,labels=[l])
    if len(k)==1:
      lh=sME.plotmesh(Th.sTh[k[0]],**kwargs)
      if legend:
        if isinstance(lh,list):
          lh=lh[0]
        if isinstance(lh,Poly3DCollection): # BUG: plt.legend does not accept Poly3DCollection as input
          lkwargs=kwargs
          color=check_color(lkwargs.pop('color',Th.sTh[k[0]].color))
          edgecolor=check_color(lkwargs.pop('edgecolor','White'))
          facecolor=check_color(lkwargs.pop('facecolor',color))
          Legend_handle.append(Patch(facecolor=facecolor,edgecolor=edgecolor,**kwargs))
        else:
          Legend_handle.append(lh)
        if latex:
          Labels.append(r'$%s_{%d}$'%(LabName,l))
        else:
          Labels.append(mesh_label(Th.sTh[k[0]]))
      
  #ax=fig.axes[0]
  #ax.set_axis_off()
  #ax.set_axis_bgcolor('None')
  if legend:
    plt.legend(Legend_handle,Labels,loc='best', ncol=int(len(Legend_handle)/10)+1).draggable()
  #coef=1.0 
  #m=min(Th.bbox);M=max(Th.bbox)
  #if Th.dim==3:
    #ax.set_zlim(m*coef,M*coef)
  #ax.set_xlim(m*coef,M*coef)
  #ax.set_ylim(m*coef,M*coef) 
  #ax.set_aspect('equal')
  set_axes(plt.gca(),Th.bbox)
  return Legend_handle
  
def plot(Th,u,**kwargs):
  assert issiMesh(Th), "First argument must be a siMesh object"
  d=kwargs.pop('d', Th.d)
  kwargs['vmin']=kwargs.get('vmin', min(u))#;kwargs['vmin']=vmin
  kwargs['vmax']=kwargs.get('vmax', max(u))#;kwargs['vmax']=vmax
  labels=kwargs.pop('labels', Th.sThlab[Th.find(d)])
  merge=kwargs.pop('merge',True)
  colormap=kwargs.pop('colormap','viridis')
  kwargs['cmap']=kwargs.pop('cmap',plt.cm.get_cmap(name=colormap))
  if merge:
    (q,me,toGlobal)=Th.get_mesh(d=d,labels=labels)
    pp=plt4sim.plot(q,me,u[toGlobal],**kwargs)
    set_axes(plt.gca(),Th.bbox)
    return pp
  
  if isinstance(labels,int):
    labels=[labels]
  
  handles=[]
  for l in labels:
    k=Th.find(d,labels=[l])
    if len(k)==1:
      h=sME.plot(Th.sTh[k[0]],u,**kwargs)
      handles.append(h)
  #ax=plt.gca()
  set_axes(plt.gca(),Th.bbox)
  #coef=1.0 
  #m=min(Th.bbox);M=max(Th.bbox)
  #fig = plt.gcf()
  #ax=fig.axes[0]
  #if Th.dim==3:
    #ax.set_zlim(m*coef,M*coef)
  #ax.set_xlim(m*coef,M*coef)
  #ax.set_ylim(m*coef,M*coef) 
  #ax.set_aspect('equal')
  return handles
  
def plotiso(Th,u,**kwargs):
  assert issiMesh(Th), "First argument must be a siMesh object"
  assert(Th.dim==2 and Th.d==2)
  kwargs['vmin']=kwargs.get('vmin', min(u))
  kwargs['vmax']=kwargs.get('vmax', max(u))
  labels=kwargs.pop('labels', Th.sThlab[Th.find(Th.d)])
  merge=kwargs.pop('merge',True)
  
  colormap=kwargs.pop('colormap','viridis')
  kwargs['cmap']=kwargs.pop('map',plt.cm.get_cmap(name=colormap))
  if merge:
    (q,me,toGlobal)=Th.get_mesh(d=Th.d,labels=labels)
    pp=plt4sim.plotiso(q,me,u[toGlobal],**kwargs)
    set_axes(plt.gca(),Th.bbox)
    return pp
  
  if isinstance(labels,int):
    labels=[labels]
  handles=[]
  for l in labels:
    k=Th.find(Th.d,labels=[l])
    if len(k)==1:
      h=sME.plotiso(Th.sTh[k[0]],u,**kwargs)
      handles.append(h)
  set_axes(plt.gca(),Th.bbox)
  return handles
  
def plotGradBaCo(Th,**kwargs):
  assert issiMesh(Th), "First argument must be a siMesh object"
  d=kwargs.get('d', Th.d)
  labels=kwargs.get('labels', Th.sThlab[Th.find(d)])
  #PlotOptions=kwargs.get('PlotOptions', {})
  for l in labels:
    k=Th.find(d,labels=[l])
    if len(k)==1:
      sME.plotGradBaCo(Th.sTh[k[0]])
      
      
def quiver(Th,V,**kwargs):
  assert issiMesh(Th), "First argument must be a siMesh object"
  d=kwargs.pop('d', Th.d)
  labels=kwargs.pop('labels', Th.sThlab[Th.find(d)])
  if np.isscalar(labels):
    labels=[labels]
  scalars=kwargs.pop('scalars', None )
  scale_factor=kwargs.pop('scale_factor', 1 )
  scale=kwargs.pop('scale', 1/scale_factor )
  color=check_color(kwargs.pop('color', None))
  colormap=kwargs.pop('colormap','viridis')
  kwargs['cmap']=kwargs.pop('map',plt.cm.get_cmap(name=colormap))
  nvec=kwargs.pop('nvec', None ) 
  
  if color is not None:
    kwargs['color']=color
  else:
    if scalars is None:
      scalars=np.sqrt(np.sum(V**2,axis=0))
    if kwargs.get('clim',None) is None: 
      vmin=np.min(scalars);vmax=np.max(scalars)
      vmin=kwargs.pop('vmin',vmin)
      vmax=kwargs.pop('vmax',vmax)
      kwargs['clim']=kwargs.pop('clim',[vmin,vmax])
    
  Q,toGlobal=Th.merge_vertices(d=d,labels=labels)
  N=len(toGlobal)
  if np.isscalar(nvec):
    if nvec<N:
      I=np.random.choice(N,nvec,replace=False)
      N=nvec
      toGlobal=toGlobal[I]
      Q=Q[:,I]
  #toGlobal=[]
  #Q=np.zeros((Th.nq,Th.dim))
  #for l in labels:
    #k=Th.find(d,labels=[l])
    #if len(k)==1:
      #toGlobal=np.hstack((toGlobal,Th.sTh[k[0]].toGlobal))
      #Q[Th.sTh[k[0]].toGlobal]=Th.sTh[k[0]].q 
  #toGlobal=np.int32(np.unique(toGlobal))
  #Q=Q[toGlobal].T
  W=np.zeros((Th.dim,N))
  for i in np.arange(Th.dim):
    W[i]=V[i][toGlobal]
    
  args=[]
  if scalars is not None:
    if Th.dim==2:
      args.append(scalars[toGlobal])
    if Th.dim==3:
      cmap = plt.get_cmap()
      # One arrow : 3 lines (shaft,headA and headB) so 3 colors
      # Three arrows with colors value v1,v2 and v3: array is [ v1,v2,v3,v1,v1,v2,v2,v3,v3]!  
      #       for N arrows [shaft1,...,shaftN, headA1,headB1,headA2,headB2,...,headAN,headBN]
      C=scalars[toGlobal] # First all -- 
      C=np.concatenate((C,np.repeat(C,2))) 
      kwargs['colors']=cmap(C)
      kwargs['array']=C # for colormap
  if Th.dim==2:    
    pq=plt.quiver(Q[0],Q[1],W[0],W[1],scale=scale,*args,**kwargs)
  if Th.dim==3:
    fig = plt.gcf()
    if len(fig.axes)>0:
      ax=fig.axes[0]
    else:
      ax = fig.gca( projection='3d')
    pq=ax.quiver(Q[0],Q[1],Q[2],W[0]/scale,W[1]/scale,W[2]/scale,**kwargs)
  
  return pq
