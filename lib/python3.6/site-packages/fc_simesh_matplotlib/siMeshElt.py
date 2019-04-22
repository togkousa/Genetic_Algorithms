import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon,Patch
from mpl_toolkits.mplot3d import Axes3D
import mpl_toolkits.mplot3d as a3
from mpl_toolkits.mplot3d.art3d import Poly3DCollection,Line3DCollection
from matplotlib.collections import LineCollection

from fc_tools.others import LabelBaseNameSimp
from fc_tools.colors import check_color
from fc_simesh.siMeshElt import issiMeshElt,move_mesh,mesh_label,getLocalValue,getLocalVector
import fc_matplotlib4mesh.simplicial as plt4sim

from  copy import deepcopy

def plotmesh(sTh,**kwargs):
  assert issiMeshElt(sTh), "First argument must be a siMeshElt object"
  #kwargs['name']=kwargs.get('name', mesh_label(sTh) )
  kwargs['color']=check_color(kwargs.pop('color', sTh.color))
  z=kwargs.pop('z',None)
  if z is not None:
    kwargs['z']=getLocalValue(sTh,z)
  move=kwargs.pop('move',None)
  if move is not None:
    kwargs['move']=getLocalVector(sTh,move)
  return plt4sim.plotmesh(sTh.q,sTh.me,**kwargs)

def plot(sTh,u,**kwargs):
  assert issiMeshElt(sTh), "First argument must be a siMeshElt object"
  return plt4sim.plot(sTh.q,sTh.me,getLocalValue(sTh,u),**kwargs)

def plotiso(sTh,u,**kwargs):
  assert issiMeshElt(sTh), "First argument must be a siMeshElt object"
  assert sTh.d==2 and sTh.dim==2
  vmin=kwargs.get('vmin', min(u));kwargs['vmin']=vmin
  vmax=kwargs.get('vmax', max(u));kwargs['vmax']=vmax
  return plt4sim.plotiso(sTh.q,sTh.me,getLocalValue(sTh,u),**kwargs)

#def PlotmeshSubTh2simp2D(sTh,color,**kwargs):
  #me=sTh.me.transpose();
  #Name=LabelBaseNameSimp(sTh.dim,sTh.dglobal,sTh.d)
  #move=kwargs.pop('move',None)
  #q=move_mesh(sTh,move)
  #fig = plt.gcf()
  #hl=plt.triplot(q[:,0],q[:,1],triangles=me,color=color,**kwargs)
  #legend_handle=hl[0]
  #label=r"$%s_{"%Name+str(sTh.label)+"}$"
  #for i in range(len(hl)):
    #hl[i].aname=label
  #return legend_handle,label
  
#def PlotmeshSubTh1simp2D(sTh,color,**kwargs):
  #move=kwargs.pop('move',None)
  #q=move_mesh(sTh,move)
  #fig = plt.gcf()
  #ive=range(sTh.d+1)
  #ANone=np.array([None]*sTh.nme)
  #Name=LabelBaseNameSimp(sTh.dim,sTh.dglobal,sTh.d)
  #X=np.array([q[sTh.me[0],0],q[sTh.me[1],0],ANone]).T.reshape((sTh.nme*3,))
  #Y=np.array([q[sTh.me[0],1],q[sTh.me[1],1],ANone]).T.reshape((sTh.nme*3,))
  #fig = plt.gcf()
  #ax = fig.gca()
  #label=r"$%s_{"%(Name)+str(int(sTh.label))+"}$"
  #legend_handle,=ax.plot(X,Y,color=color,**kwargs)
  #legend_handle.aname=label
  #return legend_handle,label

#def PlotmeshSubTh0simp2D(sTh,color,**kwargs):
  #marker=kwargs.pop('marker','o')
  #move=kwargs.pop('move',None)
  #q=move_mesh(sTh,move)
  #Name=LabelBaseNameSimp(sTh.dim,sTh.dglobal,sTh.d)
  #fig = plt.gcf()
  #ax = fig.gca()
  ##plt.rc('text', usetex=True)
  #label=r"$%s_{"%(Name)+str(int(sTh.label))+"}$"
  #legend_handle,=ax.plot(q[0,0],q[0,1],color=color,linestyle='',marker=marker,**kwargs)
  #legend_handle.aname=label
  ##legend_handle=plt.Line2D([0, 1],[0,1],color=color,**kwargs)
  ##label=r"$%s_{"%(Name)+str(int(sTh.label))+"}$"
  #return legend_handle,label


#def PlotmeshSubTh0simp3D(sTh,color,**kwargs):
  #marker=kwargs.pop('marker','o')
  #move=kwargs.pop('move',None)
  #q=move_mesh(sTh,move)
  #Name=LabelBaseNameSimp(sTh.dim,sTh.dglobal,sTh.d)
  #fig = plt.gcf()
  #ax = fig.gca(projection='3d')
  #label=r"$%s_{"%(Name)+str(int(sTh.label))+"}$"
  #legend_handle=ax.scatter(q[0,0],q[0,1],q[0,2],c=color,marker=marker,**kwargs)
  #legend_handle.aname=label
  #return legend_handle,label
    
#def PlotmeshSubTh1simp3D(sTh,color,**kwargs):
  #move=kwargs.pop('move',None)
  #q=move_mesh(sTh,move)
  #Name=LabelBaseNameSimp(sTh.dim,sTh.dglobal,sTh.d)
  #Q=q[sTh.me].swapaxes(0,1)
  #fig = plt.gcf()
  #if len(fig.axes)>0:
    #ax=fig.axes[0]
  #else:
    #ax = fig.gca( projection='3d')
  #ax.add_collection(Line3DCollection(Q,colors=color, **kwargs))
  #legend_handle=plt.Line2D([0, 1],[0,1],color=color,**kwargs)
  #label=r"$%s_{"%(Name)+str(int(sTh.label))+"}$"
  #return legend_handle,label
  
#def PlotmeshSubTh2simp3D(sTh,color,**kwargs):
  #Name=LabelBaseNameSimp(sTh.dim,sTh.dglobal,sTh.d)
  #alpha=kwargs.pop('alpha',None)
  #move=kwargs.pop('move',None)
  #q=move_mesh(sTh,move)
  #edgecolor=check_color(kwargs.pop('edgecolor',color))
  #facecolor=check_color(kwargs.pop('facecolor',color))
  #fig = plt.gcf()
  #if len(fig.axes)>0:
    #ax=fig.axes[0]
  #else:
    #ax = fig.gca( projection='3d')
  #if facecolor is None:
    #Q=np.concatenate((q[sTh.me[[0,1]]],q[sTh.me[[0,2]]],q[sTh.me[[1,2]]])).swapaxes(0,1)
    #Coll = Line3DCollection(Q,alpha=alpha,edgecolor=edgecolor, **kwargs)
    #ax.add_collection(Coll)
  #else:
    #Q=q[sTh.me].swapaxes(0,1)
    #aaa=ax.add_collection(Poly3DCollection(Q,alpha=alpha,facecolor=facecolor,edgecolor=edgecolor,**kwargs)) # BUG: with alpha=... don't work with ax.add_collection3d
    ##aaa.set_alpha(alpha)
    ##aaa.set_facecolor(color)
    ##aaa.set_edgecolor(color)
    
  #legend_handle=Patch(color=color,**kwargs)
  #label=r"$%s_{"%(Name)+str(int(sTh.label))+"}$"
  #return legend_handle,label
  
#def PlotmeshSubTh3simp3D(sTh,color,**kwargs):
  #Name=LabelBaseNameSimp(sTh.dim,sTh.dglobal,sTh.d)
  #move=kwargs.pop('move',None)
  #q=move_mesh(sTh,move)
  #me=sTh.me
  #Q=np.concatenate((q[me[[0,1]]],q[me[[0,2]]],q[me[[0,3]]],q[me[[1,2]]],q[me[[1,3]]],q[me[[2,3]]])).swapaxes(0,1)
  #fig = plt.gcf()
  #if len(fig.axes)>0:
    #ax=fig.axes[0]
  #else:
    #ax = fig.gca( projection='3d')
  #ax.add_collection3d(Line3DCollection(Q,colors=color,**kwargs))#linewidths=0.4, linestyles=':')) # linewidths=0.4, linestyles=':')
  #legend_handle=plt.Line2D([0, 1],[0,1],color=color,**kwargs)
  #label=r"$%s_{"%(Name)+str(int(sTh.label))+"}$"
  #return legend_handle,label

#def barycenters(sTh):
#Ba=np.zeros((sTh.nme,sTh.dim))
#for i in range(sTh.d+1):
  ##Ba=Ba+sTh.q[sTh.me[:,sTh.indve[i]]]
  #Ba=Ba+sTh.q[sTh.me]
#return Ba/(sTh.d+1)

def plotElementsNumber(sTh,**kwargs):
  assert issiMeshElt(sTh), "First argument must be a siMeshElt object"
  Ba=sTh.barycenters()
  fig = plt.gcf()
  ax = fig.axes[0]
  if sTh.dim==2:
    for k in range(sTh.nme):
      ax.annotate(str(k),(Ba[k,0],Ba[k,1]),verticalalignment='center', horizontalalignment='center',clip_on=True,**kwargs)
      # FC : annotate more efficient than text...
      
def plotGradBaCo(sTh,**kwargs):
  assert issiMeshElt(sTh), "First argument must be a siMeshElt object"
  scale=kwargs.get('scale', 10)
  Ba=sTh.barycenters()
  Normal=sTh.NormalFaces()
  Colors=selectColors(sTh.d+1)

  if sTh.dim==2:
    for i in range(sTh.d+1):
      plt.quiver(Ba[0],Ba[1],Normal[i,0,:],Normal[i,1,:],units='x',color=Colors[i],scale=scale)
      
      xlist = []
      ylist = [] 
      for k in range(sTh.nme):
        xlist.extend((Ba[0,k],sTh.q[sTh.me[i,k],0]))
        xlist.append(None)
        ylist.extend((Ba[1,k],sTh.q[sTh.me[i,k],1]))
        ylist.append(None)
      plt.plot(xlist,ylist,color=Colors[i],ls=':') 
  elif sTh.dim==3:
    for i in range(sTh.d+1):
      plt.quiver(Ba[0],Ba[1],Ba[2],Normal[i,0,:],Normal[i,1,:],Normal[i,2,:],units='x',color=Colors[i],scale=scale)
      
      xlist = [];ylist = [];zlist =[]
      for k in range(sTh.nme):
        xlist.extend((Ba[0,k],sTh.q[sTh.me[i,k],0]))
        xlist.append(None)
        ylist.extend((Ba[1,k],sTh.q[sTh.me[i,k],1]))
        ylist.append(None)
        zlist.extend((Ba[2,k],sTh.q[sTh.me[i,k],2]))
        zlist.append(None)
      plt.plot3(xlist,ylist,zlist,color=Colors[i],ls=':')
    
#def plotSubTh1simp2D(sTh,u,**kwargs):
  #plane=kwargs.pop('plane',True)
  #if len(u)==sTh.nqGlobal:
    #U=u[sTh.toGlobal]
  #else:
    #assert( len(u) == sTh.nq )
    #U=u    
  #if plane:
    #Q=sTh.q[sTh.me].swapaxes(0,1)
    #lines = LineCollection(Q,array=np.mean(U[sTh.me],axis=0),norm=matplotlib.colors.Normalize(vmin=min(u), vmax=max(u)),**kwargs)
    #ax = plt.gca()
    #ax.add_collection(lines)
  #else:
    #Q=np.hstack((sTh.q,U.reshape((sTh.nq,1))))
    #Q=Q[sTh.me].swapaxes(0,1)
    #fig = plt.gcf()
    #if len(fig.axes)>0:
      #ax=fig.axes[0]
    #else:
      #ax = fig.gca( projection='3d')
    #ax.add_collection(Line3DCollection(Q,array=np.mean(U[sTh.me],axis=0),norm=matplotlib.colors.Normalize(vmin=min(u), vmax=max(u)),**kwargs))
    #ax.set_zlim3d([min(u),max(u)])
  
#def plotSubTh2simp2D(sTh,u,**kwargs):
  #plane=kwargs.pop('plane',True)
  #shading=kwargs.pop('shading','gouraud')
  #if len(u)==sTh.nqGlobal:
    #U=u[sTh.toGlobal]
  #else:
    #assert( len(u) == sTh.nq )
    #U=u
  #if plane:
    #coll=plt.tripcolor(sTh.q[:,0],sTh.q[:,1],sTh.me.T, U,vmin=np.min(u),vmax=np.max(u), shading=shading,**kwargs)
  #else:
    #Q=np.hstack((sTh.q,U.reshape((sTh.nq,1))))
    #Q=Q[sTh.me].swapaxes(0,1)
    #fig = plt.gcf()
    #if len(fig.axes)>0:
      #ax=fig.axes[0]
    #else:
      #ax = fig.gca( projection='3d')
    #coll=ax.add_collection(Poly3DCollection(Q,array=np.mean(U[sTh.me],axis=0),norm=matplotlib.colors.Normalize(vmin=min(u), vmax=max(u)),**kwargs))
    #ax.set_zlim3d([min(u),max(u)])
  #return coll
  
#def plotSubTh2simp3D(sTh,u,**kwargs):
  #if len(u)==sTh.nqGlobal:
    #U=u[sTh.toGlobal]
  #else:
    #assert( len(u) == sTh.nq )
    #U=u    
  #v=np.mean(U[sTh.me],axis=0)
  ##mappable = plt.cm.ScalarMappable(cmap=plt.cm.coolwarm, norm=matplotlib.colors.Normalize(vmin=np.min(u), vmax=np.max(u)))
  ##facecolors = mappable.to_rgba(v)
  #Q=sTh.q[sTh.me].swapaxes(0,1)
  ##poly = Poly3DCollection(Q,facecolors=facecolors)
  #poly = Poly3DCollection(Q,array=v,norm=matplotlib.colors.Normalize(vmin=min(u), vmax=max(u)),**kwargs)
  #fig = plt.gcf()
  #if len(fig.axes)>0:
    #ax=fig.axes[0]
  #else:
    #ax = fig.gca( projection='3d')
  #col=ax.add_collection(poly)
  #return col
  
#def plotSubTh1simp3D(sTh,u,**kwargs):
  #if len(u)==sTh.nqGlobal:
    #U=u[sTh.toGlobal]
  #else:
    #assert( len(u) == sTh.nq )
    #U=u    
  #v=np.mean(U[sTh.me],axis=0)
  ##mappable = plt.cm.ScalarMappable(norm=matplotlib.colors.Normalize(vmin=np.min(u), vmax=np.max(u)))
  ##colors = mappable.to_rgba(v)
  #Q=sTh.q[sTh.me].swapaxes(0,1)
  ##lines = a3.art3d.Line3DCollection(Q,colors=colors,**kwargs)
  #lines = Line3DCollection(Q,array=v,norm=matplotlib.colors.Normalize(vmin=np.min(u), vmax=np.max(u)),**kwargs)
  #fig = plt.gcf()
  #if len(fig.axes)>0:
    #ax=fig.axes[0]
  #else:
    #ax = fig.gca( projection='3d')
  #col=ax.add_collection(lines)
  #return col
  
#def plotSubTh3simp3D(sTh,u,**kwargs):
  #s=kwargs.pop('s',1)
  #if len(u)==sTh.nqGlobal:
    #U=u[sTh.toGlobal]
  #else:
    #assert( len(u) == sTh.nq )
    #U=u    
  
  #fig = plt.gcf()
  #if len(fig.axes)>0:
    #ax=fig.axes[0]
  #else:
    #ax = fig.gca( projection='3d')
  #col=ax.scatter3D(sTh.q[:,0],sTh.q[:,1],sTh.q[:,2],s=s,c=U,vmin=min(u),vmax=max(u),**kwargs)  
  #return col
