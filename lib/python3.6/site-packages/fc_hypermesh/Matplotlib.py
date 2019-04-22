import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon,Patch
from mpl_toolkits.mplot3d import Axes3D
import mpl_toolkits.mplot3d as a3
from mpl_toolkits.mplot3d.art3d import Poly3DCollection,Line3DCollection
from fc_tools.others import LabelBaseName
import fc_hypermesh.CartesianGrid as CG

def plotmesh(self,**kwargs):
    color=kwargs.pop('color',self.color)
    if self.type==0:
      return eval("PlotmeshSubTh"+str(self.m)+"simp"+str(self.d)+"D(self,color,**kwargs)")
    else:
      return eval("PlotmeshSubQh"+str(self.m)+"orth"+str(self.d)+"D(self,color,**kwargs)")

def PlotmeshSubTh2simp2D(self,color,**kwargs):
  from matplotlib.patches import Polygon
  from matplotlib.collections import PolyCollection
  Name=LabelBaseName(2,2)
  Poly2D=self.q[:,self.me].swapaxes(0,2)
  p = PolyCollection(Poly2D, facecolor="none",edgecolor = color)
  ax=plt.gca()
  ax.add_collection(p)
  ax.autoscale()
  legend_handle=Patch(color=color,**kwargs) # to improve
  label=r"$%s_{"%(Name)+str(int(self.label))+"}$"
  return legend_handle,label
  
def PlotmeshSubQh2orth2D(self,color,**kwargs):
  from matplotlib.patches import Polygon
  from matplotlib.collections import PolyCollection
  Name=LabelBaseName(2,2)
  Poly2D=self.q[:,self.me[[0,1,3,2],:]].swapaxes(0,2)
  p = PolyCollection(Poly2D, facecolor="none",edgecolor = color)
  ax=plt.gca()
  legend_handle=ax.add_collection(p)
  ax.autoscale()
  legend_handle=Patch(color=color,**kwargs) # to improve
  label=r"$%s_{"%(Name)+str(int(self.label))+"}$"
  return legend_handle,label
  
def PlotmeshSubTh1simp2D(self,color,**kwargs):
  ive=range(self.m+1)
  ANone=np.array([None]*self.nme)
  Name=LabelBaseName(2,1)
  X=np.array([self.q[0,self.me[0]],self.q[0,self.me[1]],ANone]).T.reshape((self.nme*3,))
  Y=np.array([self.q[1,self.me[0]],self.q[1,self.me[1]],ANone]).T.reshape((self.nme*3,))
  fig = plt.gcf()
  ax = fig.gca()
  #plt.rc('text', usetex=True)
  label=r"$%s_{"%(Name)+str(int(self.label))+"}$"
  legend_handle,=ax.plot(X,Y,color=color,picker=5,**kwargs)
  legend_handle.aname=label
  #legend_handle=plt.Line2D([0, 1],[0,1],color=color,**kwargs)
  #label=r"$%s_{"%(Name)+str(int(self.label))+"}$"
  return legend_handle,label

def PlotmeshSubQh1orth2D(self,color,**kwargs):
  return PlotmeshSubTh1simp2D(self,color,**kwargs)

def PlotmeshSubTh0simp2D(self,color,**kwargs):
  s=kwargs.get('s', 20 );kwargs.pop('s',None)
  marker=kwargs.get('marker', 'o' );kwargs.pop('marker',None)
  Name=LabelBaseName(2,0)
  fig = plt.gcf()
  ax = fig.gca()
  label=r"$%s_{"%(Name)+str(int(self.label))+"}$"
  #legend_handle,=ax.plot(self.q[0,0],self.q[1,0],color=color,linestyle='',marker='o',picker=5,**kwargs)
  legend_handle=ax.scatter(self.q[0,0],self.q[1,0],c=color,marker=marker,s=s,**kwargs)
  legend_handle.aname=label
  return legend_handle,label

def PlotmeshSubQh0orth2D(self,color,**kwargs):
  return PlotmeshSubTh0simp2D(self,color,**kwargs)

def PlotmeshSubTh0simp3D(self,color,**kwargs):
  s=kwargs.get('s', 5 );kwargs.pop('s',None)
  marker=kwargs.get('marker', 'o' );kwargs.pop('marker',None)
  Name=LabelBaseName(3,0)
  fig = plt.gcf()
  if len(fig.axes)>0:
    ax=fig.axes[0]
  else:
    ax = fig.gca( projection='3d')
  label=r"$%s_{"%(Name)+str(int(self.label))+"}$"
  #legend_handle=ax.scatter(self.q[0,0],self.q[1,0],self.q[2,0],c=color,marker=marker,picker=picker,**kwargs)
  legend_handle=ax.scatter(self.q[0,0],self.q[1,0],self.q[2,0],c=color,marker=marker,s=s,**kwargs)
  legend_handle.aname=label
  return legend_handle,label

def PlotmeshSubQh0orth3D(self,color,**kwargs):
  return PlotmeshSubTh0simp3D(self,color,**kwargs)
    
def PlotmeshSubTh1simp3D(self,color,**kwargs):
  Name=LabelBaseName(3,1)
  Line3D=self.q[:,self.me].swapaxes(0,2)
  fig = plt.gcf()
  if len(fig.axes)>0:
    ax=fig.axes[0]
  else:
    ax = fig.gca( projection='3d')
  ax.add_collection3d(Line3DCollection(Line3D,colors=color, **kwargs))
  legend_handle=plt.Line2D([0, 1],[0,1],color=color,**kwargs)
  label=r"$%s_{"%(Name)+str(int(self.label))+"}$"
  return legend_handle,label

def PlotmeshSubQh1orth3D(self,color,**kwargs):
  return PlotmeshSubTh1simp3D(self,color,**kwargs)
  
def PlotmeshSubTh2simp3D(self,color,**kwargs): 
  return PlotmeshSubGen2orth3D(self,color,**kwargs)


def PlotmeshSubQh2orth3D(self,color,**kwargs):  
  return PlotmeshSubGen2orth3D(self,color,**kwargs)

def PlotmeshSubGen2orth3D(self,color,**kwargs):  
  Name=LabelBaseName(3,2)
  edgecolor=kwargs.pop('edgecolor',None)
  if color is None:
    color=self.color
  if 'facecolor' in kwargs:
    color=kwargs.pop('facecolor',None)
  if color is None: 
    Line3D=self.q[:,self.me].swapaxes(0,2)
    if self.type==0:
      C=[[0,1],[1,2],[2,0]]
    else:
      C=[[0,1],[2,3],[0,2],[1,3]]
    Poly3D=np.zeros((0,2,3))
    if edgecolor is None:
      edgecolor=self.color
    for edge in C:
      Poly3D=np.concatenate((Poly3D,self.q[:,self.me[edge]].T))
    p = Line3DCollection(Poly3D,color=edgecolor,**kwargs)  
    legend_handle=Patch(color=edgecolor,**kwargs)
  else:  
    if self.type==0:
      Poly3D=self.q[:,self.me].swapaxes(0,2)
    else:  
      Poly3D=self.q[:,self.me[[0,1,3,2]]].swapaxes(0,2)
    p = Poly3DCollection(Poly3D, facecolor=color,edgecolor = edgecolor,**kwargs)
    legend_handle=Patch(color=color,**kwargs)
  label=r"$%s_{"%(Name)+str(int(self.label))+"}$"
  fig = plt.gcf()
  if len(fig.axes)>0:
    ax=fig.axes[0]
  else:
    ax = fig.gca( projection='3d')
  ax.add_collection3d(p)
  ax.autoscale()
  return legend_handle,label
  
def PlotmeshSubTh3simp3D(self,color,**kwargs):
  Name=LabelBaseName(3,3)
  Poly3D=[]
  C=CG.combs(np.arange(4),2)
  for i in range(6):
     A=self.q[:,self.me[C[i]]].T
     Poly3D+= A.tolist()
      
  fig = plt.gcf()
  if len(fig.axes)>0:
    ax=fig.axes[0]
  else:
    ax = fig.gca( projection='3d')
  
  ax.add_collection3d(Line3DCollection(Poly3D,colors=color,**kwargs))#linewidths=0.4, linestyles=':')) # linewidths=0.4, linestyles=':')
  #legend_handle,=plt.plot([0, 1],[0,1],color=color,visible=False,**kwargs)
  legend_handle=Patch(color=color,**kwargs) # to improve
  label=r"$%s_{"%(Name)+str(int(self.label))+"}$"
  return legend_handle,label

def PlotmeshSubQh3orth3D(self,color,**kwargs):
  Name=LabelBaseName(3,3)
  Poly3D=[]
  C=[[0,1],[0,4],[1,5],[4,5],[2,3],[2,6],[3,7],[6,7],[1,3],[5,7],[4,6],[0,2]]
  Poly3D=np.zeros((0,2,3))
  for edge in C:
     A=self.q[:,self.me[edge]].T
     Poly3D=np.concatenate((Poly3D,A))
  fig = plt.gcf()
  if len(fig.axes)>0:
    ax=fig.axes[0]
  else:
    ax = fig.gca( projection='3d') 
  ax.add_collection3d(Line3DCollection(Poly3D,colors=color,**kwargs))#linewidths=0.4, linestyles=':')) # linewidths=0.4, linestyles=':')
  ax.autoscale()
  #legend_handle,=plt.plot([0, 1],[0,1],color=color,visible=False,**kwargs)
  legend_handle=Patch(color=color,**kwargs) # to improve
  label=r"$%s_{"%(Name)+str(int(self.label))+"}$"
  return legend_handle,label