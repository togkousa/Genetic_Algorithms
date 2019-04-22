import numpy as np
import os
import matplotlib.pyplot as plt
from fc_tools.graphics import set_axes_equal
import fc_matplotlib4mesh.simplicial as plt4sim

def getDataPath():
  fullname=os.path.dirname(os.path.abspath(__file__))
  return fullname+os.sep+'data'

def getMesh2D(d=2):
  assert d==2 or d==1
  data_path=getDataPath()
  npzfile = np.load(data_path+os.sep+'mesh%dsimp2D.npz'%d)
  q=npzfile['arr_0']
  me=npzfile['arr_1']
  return q,me

def getMesh3D(d=3):
  assert d==3 or d==2 or d==1
  data_path=getDataPath()
  npzfile = np.load(data_path+os.sep+'mesh%dsimp3D.npz'%d)
  q=npzfile['arr_0']
  me=npzfile['arr_1']
  return q,me

def getMesh3Ds(d=2):
  assert d==2 or d==1
  data_path=getDataPath()
  npzfile = np.load(data_path+os.sep+'mesh%dsimp3Ds.npz'%d)
  q=npzfile['arr_0']
  me=npzfile['arr_1']
  return q,me

def plotmesh2D():
  plt.ion()
  q2,me2=getMesh2D(2)
  q1,me1=getMesh2D(1)
  plt.close('all')
  plt.figure(1)
  plt4sim.plotmesh(q2,me2)
  plt.figure(2)
  plt4sim.plotmesh(q1,me1,color='Red',linewidth=2)
  plt4sim.plotmesh(q2,me2,color='LightGray',alpha=0.1)
  

  
def plotmesh3D():
  q3,me3=getMesh3D(3)
  q2,me2=getMesh3D(2)
  q1,me1=getMesh3D(1)
  plt.ion()
  plt.close('all')
  plt.figure(1)
  plt4sim.plotmesh(q3,me3)
  set_axes_equal()
  plt.figure(2)
  plt4sim.plotmesh(q2,me2,color='Red')
  set_axes_equal()
  plt.axis('off')
  plt.figure(3)
  plt4sim.plotmesh(q3,me3,color='LightGray',alpha=0.02)
  plt4sim.plotmesh(q1,me1,color='Magenta',linewidths=2)
  from fc_tools.graphics import Plane
  P=[Plane(origin=[0,0,1],normal=[0,0,-1]), Plane(origin=[0,0,1],normal=[0,-1,-1])]
  set_axes_equal()
  plt.axis('off')
  plt.figure(4)
  plt4sim.plotmesh(q3,me3,cut_planes=P,color='DarkGrey')
  plt4sim.plotmesh(q2,me2,cut_planes=P)
  plt4sim.plotmesh(q1,me1,color='Black',linewidths=2)
  set_axes_equal()
  plt.axis('off')
  
  
def plotmesh3Ds():
  q2,me2=getMesh3Ds(2)
  q1,me1=getMesh3Ds(1)
  plt.ion()
  plt.close('all')
  plt.figure(1)
  plt4sim.plotmesh(q2,me2,edgecolor='Red',facecolor=None)
  plt4sim.plotmesh(q1,me1,color='Black',linewidths=2)
  set_axes_equal()
  plt.figure(2)
  plt4sim.plotmesh(q2,me2,color='LightGray',alpha=0.1)
  plt4sim.plotmesh(q1,me1,color='Magenta',linewidths=2)
  plt.axis('off')
  set_axes_equal()
  
def plot2D():
  q2,me2=getMesh2D(2)
  q1,me1=getMesh2D(1)
  f=lambda x,y: 5*np.exp(-3*(x**2+y**2))*np.cos(x)*np.sin(y)
  u2=f(q2[:,0],q2[:,1])
  u1=f(q1[:,0],q1[:,1])
  plt.close('all')
  plt.ion()
  plt.figure(1)
  ps1=plt4sim.plot(q2,me2,u2)
  plt4sim.plotmesh(q1,me1,color='Black',linewidths=2)
  plt.colorbar()
  plt.figure(2)
  ps2=plt4sim.plot(q1,me1,u1,linewidths=2)
  plt.colorbar(ps2)
  plt4sim.plotmesh(q2,me2,color='LightGray',alpha=0.1)
  plt.axis('off')
  
  plt.figure(3)
  ps3=plt4sim.plot(q2,me2,u2,plane=False)
  plt4sim.plotmesh(q1,me1,z=u1,color='Black',linewidths=2)
  plt.colorbar(ps3)
  plt.axis('off')
  plt.figure(4)
  ps4=plt4sim.plot(q1,me1,u1,linewidths=2,plane=False)
  #plt4sim.plotmesh(q2,me2,z=u2,color='LightGray',alpha=0.1)
  plt.colorbar(ps4)
  plt.axis('off')
  
  
def plot3D():
  q3,me3=getMesh3D(3)
  q2,me2=getMesh3D(2)
  q1,me1=getMesh3D(1)
  f=lambda x,y,z: np.cos(3*x)*np.sin(2*y)*np.sin(3*z)
  u3=f(q3[:,0],q3[:,1],q3[:,2])
  u2=f(q2[:,0],q2[:,1],q2[:,2])
  u1=f(q1[:,0],q1[:,1],q1[:,2])
  plt.close('all')
  plt.ion()
  plt.figure(1)
  pp=plt4sim.plot(q3,me3,u3)
  plt4sim.plotmesh(q1,me1,color='Black',linewidths=2)
  plt.colorbar(pp)
  set_axes_equal()
  plt.figure(2)
  pp=plt4sim.plot(q2,me2,u2)
  plt4sim.plotmesh(q1,me1,color='Black',linewidths=2)
  plt.axis('off')
  set_axes_equal()
  plt.colorbar(pp)
  plt.figure(3)
  pp=plt4sim.plot(q1,me1,u1,linewidths=2,vmin=min(u3),vmax=max(u3))
  plt4sim.plotmesh(q3,me3,color='LightGray',alpha=0.1)
  plt.colorbar(pp)
  plt.axis('off')
  set_axes_equal()
  
def plot3Ds():
  q2,me2=getMesh3Ds(2)
  q1,me1=getMesh3Ds(1)
  f=lambda x,y,z: np.cos(3*x-1)*np.sin(2*y-2)*np.sin(3*z)
  u2=f(q2[:,0],q2[:,1],q2[:,2])
  u1=f(q1[:,0],q1[:,1],q1[:,2])
  plt.close('all')
  plt.ion()
  plt.figure(1)
  pp=plt4sim.plot(q2,me2,u2)
  plt4sim.plotmesh(q1,me1,color='Black',linewidths=2)
  plt.colorbar(pp)
  plt.axis('off')
  set_axes_equal()
  plt.figure(2)
  pp=plt4sim.plot(q1,me1,u1,linewidths=2,vmin=min(u2),vmax=max(u2))
  plt4sim.plotmesh(q2,me2,color='LightGray',alpha=0.1)
  plt.colorbar(pp)
  plt.axis('off')
  set_axes_equal()
  
def plotiso2D01():
  q2,me2=getMesh2D(2)
  q1,me1=getMesh2D(1)
  f=lambda x,y: 5*np.exp(-3*(x**2+y**2))*np.cos(x)*np.sin(y)
  u2=f(q2[:,0],q2[:,1])
  plt.close('all')
  plt.ion()
  cmap=plt.cm.get_cmap(name='viridis')
  plt4sim.plotiso(q2,me2,u2,niso=25,cmap=cmap)
  plt.colorbar()
  plt4sim.plotmesh(q1,me1,color='black')
  plt4sim.plotmesh(q2,me2,color='LightGray',alpha=0.04)
  set_axes_equal()
  plt.figure(2)
  plt4sim.plot(q2,me2,u2,cmap=cmap)
  plt.colorbar()
  set_axes_equal()
  plt4sim.plotiso(q2,me2,u2,isorange=np.arange(-1,1,0.2),color='White')
  
#def plotiso3D01():
  #q3,me3=getMesh3D(3)
  #q2,me2=getMesh3D(2)
  #q1,me1=getMesh3D(1)
  #f=lambda x,y,z: np.cos(3*x)*np.sin(2*y)*np.sin(3*z)
  #u3=f(q3[:,0],q3[:,1],q3[:,2])
  #u2=f(q2[:,0],q2[:,1],q2[:,2])
  #u1=f(q1[:,0],q1[:,1],q1[:,2])
  #plt.close('all') 
  #plt.figure(1)
  #plt4sim.plotiso(q2,me2,u2,line_width=2)
  #plt4sim.plotmesh(q2,me2, color='LightGray', alpha=0.1)
  #plt.colorbar()
  #plt.figure(2)
  #plt4sim.plot(q2,me2,u2)
  #plt4sim.plotiso(q2,me2,u2,line_width=2,color='White')
  #plt4sim.plotmesh(q1,me1, color='Black')
  #plt.colorbar()
  #plt.view(65,74,7)

#def plotiso3Ds01():
  #q2,me2=getMesh3Ds(2)
  #q1,me1=getMesh3Ds(1)
  #f=lambda x,y,z: np.cos(3*x-1)*np.sin(2*y-2)*np.sin(3*z)
  #u2=f(q2[:,0],q2[:,1],q2[:,2])
  #u1=f(q1[:,0],q1[:,1],q1[:,2])
  #plt.close('all') 
  #plt.figure(1)
  #plt4sim.plot(q2,me2,u2, alpha=0.7)
  #plt4sim.plotiso(q2,me2,u2, line_width=1.5)
  #plt.colorbar()
  #plt.figure(2)
  #plt4sim.plot(q2,me2,u2)
  #plt4sim.plotiso(q2,me2,u2, line_width=1.5,color='White')
  #plt4sim.plotmesh(q1,me1, color='Black')
  #plt.colorbar()
  
#def slicemesh3D01():
  #q3,me3=getMesh3D(3)
  #q2,me2=getMesh3D(2)
  #q1,me1=getMesh3D(1)
  #plt.close('all') 
  #plt.figure(1)
  #plt4sim.plotmesh(q2,me2,color='LightGray',alpha=0.05)
  #plt4sim.slicemesh(q3,me3,origin=(0,0,1),normal=(-1,0,1))
  #plt.view(132,53,7)
  #plt.figure(2)
  #plt4sim.plotmesh(q2,me2,color='LightGray',alpha=0.05)
  #for normal,color in [((1,0,0),'red'),((0,1,0),'magenta'),((0,0,1),'Maroon')]:
    #plt4sim.slicemesh(q3,me3,origin=(0,0,1),normal=normal,color=color)
  #plt.view(155,66,7)
  
#def slice3D01():
  #q3,me3=getMesh3D(3)
  #q2,me2=getMesh3D(2)
  #q1,me1=getMesh3D(1)
  #f=lambda x,y,z: np.cos(3*x)*np.sin(2*y)*np.sin(3*z)
  #u3=f(q3[:,0],q3[:,1],q3[:,2])
  #u2=f(q2[:,0],q2[:,1],q2[:,2])
  #u1=f(q1[:,0],q1[:,1],q1[:,2])
  #plt.close('all') 
  #plt.figure(1)
  #plt4sim.plotmesh(q2,me2,color='LightGray',alpha=0.05)
  #plt4sim.slice(q3,me3,u3,origin=(0,0,1),normal=(-1,0,1))
  #plt.view(132,53,7)
  #plt.colorbar()
  #plt.figure(2)
  #plt4sim.plotmesh(q2,me2,color='LightGray',alpha=0.05)
  #for normal in [(1,0,0),(0,1,0),(0,0,1)]:
    #plt4sim.slice(q3,me3,u3,origin=(0,0,1),normal=normal)
  #plt.view(155,66,7)
  #plt.colorbar()
  
#def sliceiso3D01():
  #q3,me3=getMesh3D(3)
  #q2,me2=getMesh3D(2)
  #q1,me1=getMesh3D(1)
  #f=lambda x,y,z: np.cos(3*x-y)*np.sin(2*y+x)*np.sin(3*z)
  #u3=f(q3[:,0],q3[:,1],q3[:,2])
  #u2=f(q2[:,0],q2[:,1],q2[:,2])
  #u1=f(q1[:,0],q1[:,1],q1[:,2])
  #plt.close('all') 
  #plt.figure(1)
  #plt4sim.plotmesh(q2,me2,color='LightGray',alpha=0.05)
  #plt4sim.sliceiso(q3,me3,u3,origin=(0,0,1),normal=(-1,0,1))
  #plt4sim.slicemesh(q3,me3,origin=(0,0,1),normal=(-1,0,1),color='DarkGray')
  #plt.view(132,53,7)
  #plt.colorbar()
  #plt.figure(2)
  #plt4sim.plotmesh(q2,me2,color='LightGray',alpha=0.05)
  #for normal in [(1,0,0),(0,1,0),(0,0,1)]:
    #plt4sim.slicemesh(q3,me3,origin=(0,0,1),normal=normal, color='LightGray')
    #plt4sim.sliceiso(q3,me3,u3,contours=15,origin=(0,0,1),normal=normal)
  #plt.view(155,66,7)
  #plt.colorbar()
  
def quiver2D01():
  (q,me)=getMesh2D(2)
  (q1,me1)=getMesh2D(1)
  f=lambda x,y:5*np.exp(-3*(x**2+y**2))*np.cos(x)*np.sin(y)
  u=f(q[:,0],q[:,1])
  w=[lambda x,y: y*np.cos(-(x**2+y**2)/10), lambda x,y: -x*np.cos(-(x**2+y**2)/10)]
  W=np.array([w[0](q[:,0],q[:,1]),w[1](q[:,0],q[:,1])])

  cmap=plt.cm.get_cmap(name='viridis')
  plt.ion()
  plt.close('all')
  plt.figure(1)
  plt4sim.quiver(q,W,scale=50,nvec=3000)
  plt4sim.plotmesh(q1,me1,color='Black')
  plt.colorbar()
  set_axes_equal()
  plt.figure(2)
  plt4sim.quiver(q,W,scalars=u,scale=50,nvec=3000)
  plt4sim.plotmesh(q1,me1,color='Black')
  #plt4sim.plotiso(q,me,u)
  plt.colorbar()
  set_axes_equal()
  plt.figure(3)
  plt4sim.quiver(q,W,scale=50,nvec=3000,color='Blue')
  plt4sim.plotmesh(q1,me1,color='Black')
  set_axes_equal()
  
def quiver3D01():
  (q3,me3)=getMesh3D(3)
  (q2,me2)=getMesh3D(2)
  (q1,me1)=getMesh3D(1)
  f=lambda x,y,z: 3*x**2-y**3+z**2+x*y
  w=[lambda x,y,z: y*np.cos(-(x**2+y**2)/10), lambda x,y,z: -x*np.cos(-(x**2+y**2)/10), lambda x,y,z: z]
  q=q3
  u3=f(q[:,0],q[:,1],q[:,2])
  W3=np.array([w[0](q[:,0],q[:,1],q[:,2]),w[1](q[:,0],q[:,1],q[:,2]),w[2](q[:,0],q[:,1],q[:,2])])
  q=q2
  u2=f(q[:,0],q[:,1],q[:,2])
  W2=np.array([w[0](q[:,0],q[:,1],q[:,2]),w[1](q[:,0],q[:,1],q[:,2]),w[2](q[:,0],q[:,1],q[:,2])])
  q=q1
  u1=f(q[:,0],q[:,1],q[:,2])
  W1=np.array([w[0](q[:,0],q[:,1],q[:,2]),w[1](q[:,0],q[:,1],q[:,2]),w[2](q[:,0],q[:,1],q[:,2])])

  cmap=plt.cm.get_cmap(name='jet')
  plt.ion()
  plt.close('all')
  plt.figure(1)
  pq=plt4sim.quiver(q3,W3,scale=20,nvec=3000)
  plt.colorbar(pq)
  plt4sim.plotmesh(q1,me1,color='Black')
  set_axes_equal()
  plt.figure(2)
  pq=plt4sim.quiver(q3,W3,scalars=u3,scale=20,nvec=3000,cmap=cmap)
  plt4sim.plotmesh(q1,me1,color='Black')
  plt.colorbar(pq)
  set_axes_equal()
  plt.axis('off')
  plt.figure(3)
  plt4sim.quiver(q3,W3,scale=20,nvec=3000,color='Blue')
  plt4sim.plotmesh(q1,me1,color='Black')
  set_axes_equal()
  plt.axis('off')
  
def quiver3Ds01():
  (q2,me2)=getMesh3Ds(2)
  (q1,me1)=getMesh3Ds(1)
  f=lambda x,y,z: 3*x**2-y**3+z**2+x*y
  w=[lambda x,y,z: y*np.cos(-(x**2+y**2)/10), lambda x,y,z: -x*np.cos(-(x**2+y**2)/10), lambda x,y,z: z]
  q=q2
  u2=f(q[:,0],q[:,1],q[:,2])
  W2=np.array([w[0](q[:,0],q[:,1],q[:,2]),w[1](q[:,0],q[:,1],q[:,2]),w[2](q[:,0],q[:,1],q[:,2])])
  q=q1
  u1=f(q[:,0],q[:,1],q[:,2])
  W1=np.array([w[0](q[:,0],q[:,1],q[:,2]),w[1](q[:,0],q[:,1],q[:,2]),w[2](q[:,0],q[:,1],q[:,2])])

  cmap=plt.cm.get_cmap(name='jet')
  plt.close('all')
  plt.ion()
  plt.figure(1)
  pq=plt4sim.quiver(q2,W2,scale=20,nvec=3000)
  plt.colorbar(pq)
  plt4sim.plotmesh(q1,me1,color='Black')
  set_axes_equal()
  plt.figure(2)
  pq=plt4sim.quiver(q2,W2,scalars=u2,scale=20,nvec=3000,cmap=cmap)
  plt4sim.plotmesh(q1,me1,color='Black')
  plt.colorbar(pq)
  set_axes_equal()
  plt.axis('off')
  plt.figure(3)
  plt4sim.quiver(q2,W2,scale=20,nvec=3000,color='Blue')
  plt4sim.plotmesh(q1,me1,color='Black')
  set_axes_equal()
  plt.axis('off')
  
#def iso_surface3D01():
  #q3,me3=getMesh3D(3)
  #q2,me2=getMesh3D(2)
  #q1,me1=getMesh3D(1)
  #f=lambda x,y,z: np.cos(3*x)*np.sin(2*y)*np.sin(3*z)
  #u=f(q3[:,0],q3[:,1],q3[:,2])
  #plt.close('all') 
  #plt.figure(1)
  #plt4sim.iso_surface(q3,me3,u,contours=5)
  #plt4sim.plotmesh(q2,me2,color='LightGray',alpha=0.05)
  #plt.colorbar()
  #plt.figure(2)
  #plt4sim.iso_surface(q3,me3,u,contours=np.linspace(-0.8,0.8,10))
  #plt4sim.plotmesh(q2,me2,color='LightGray',alpha=0.05)
  #plt.colorbar()
  
#def streamline3D01(N=15):
  #q3,me3=getMesh3D(3)
  #q2,me2=getMesh3D(2)
  #q1,me1=getMesh3D(1)
  #f=lambda x,y,z: 3*x**2-y**3+z**2+x*y
  #u=f(q3[:,0],q3[:,1],q3[:,2])
  #w=[lambda x,y,z: y*np.cos(-(x**2+y**2)/10), lambda x,y,z: -x*np.cos(-(x**2+y**2)/10), lambda x,y,z: z/5]
  #W=np.array([w[0](q3[:,0],q3[:,1],q3[:,2]),
              #w[1](q3[:,0],q3[:,1],q3[:,2]),
              #w[2](q3[:,0],q3[:,1],q3[:,2])])
  
  #plt.close('all') 
  #plt.figure(1)
  #plt4sim.streamline(q3,me3,u,W)
  #plt4sim.plotmesh(q2,me2,color='LightGray',alpha=0.05)
  #plt.colorbar()
  #plt.figure(2)
  #s_options={'visible':True}
  #sw_options={'normal':(0,0,1),'resolution':6}
  #st_options={'integration_direction':'both'}
  #plt4sim.streamline(q3,me3,u,W,seedtype='plane',linetype='tube',
                   #seed_options=s_options,
                   #seed_widget_options=sw_options,
                   #streamtracer_options=st_options)
  #plt4sim.plotmesh(q2,me2,color='LightGray',alpha=0.05)
  #plt.colorbar()

  #plt.figure(3)
  #sw_options={'center':(0.9,0,1), 'radius':0.1,'phi_resolution':8,
              #'theta_resolution':12,'enabled':False}
  #st_options={'integration_direction':'both'}
  #plt4sim.streamline(q3,me3,u,W,seed_widget_options=sw_options,
                   #streamtracer_options=st_options,colormap='jet')
  #sw_options['center']=(0,0,1)
  #sw_options['radius']=0.3
  #plt4sim.streamline(q3,me3,u,W,seed_widget_options=sw_options,
                   #streamtracer_options=st_options,colormap='jet')
  #plt.scalarbar()
  #plt.view(46.6,58,6.7)
  #plt4sim.plotmesh(q2,me2,color='LightGray',alpha=0.05)

  #plt.figure(4)
  #sw_options={'origin':(0,-1,0),'point1':(0,-1,2),'point2':(0,1,0),
              #'enabled':True,'resolution':6}
  #st_options={'integration_direction':'both'}
  #plt4sim.streamline(q3,me3,u,W,seedtype='plane',
                   #seed_widget_options=sw_options,
                   #streamtracer_options=st_options,colormap='jet')
  #plt.scalarbar()
  #plt.view(46.6,58,6.7)
  #plt4sim.plotmesh(q2,me2,color='LightGray',alpha=0.05)  