from fc_oogmsh import gmsh
from fc_simesh.siMesh import siMesh,HyperCube
import numpy as np


def feval2D01():
  meshfile=gmsh.buildmesh2d('condenser11',50)
  Th=siMesh(meshfile)  

  g1=lambda x,y: np.cos(x)*np.sin(y)
  g2=lambda X: np.cos(X[0])*np.sin(X[1])

  def g3(x,y):
    return np.cos(x)*np.sin(y)

  def g4(X):
    return np.cos(X[0])*np.sin(X[1])

  z1=Th.feval(g1)
  z2=Th.feval(g2)
  z3=Th.feval(g3)
  z4=Th.feval(g4)

  print('max(abs(z2-z1))=%e'%max(abs(z2-z1)))
  print('max(abs(z3-z1))=%e'%max(abs(z3-z1)))
  print('max(abs(z4-z1))=%e'%max(abs(z4-z1)))
  
  
def feval3D01():  
  meshfile=gmsh.buildmesh3d('cylinderkey',15)
  Th=siMesh(meshfile)
  g1=lambda x,y,z: 3*x**2-y**3+z**2+x*y
  g2=lambda X: 3*X[0]**2-X[1]**3+X[2]**2+X[0]*X[1]
  
  def g3(x,y,z):
    return 3*x**2-y**3+z**2+x*y
  
  def g4(X):
    return 3*X[0]**2-X[1]**3+X[2]**2+X[0]*X[1]
  
  z1=Th.feval(g1)
  z2=Th.feval(g2)
  z3=Th.feval(g3)
  z4=Th.feval(g4)

  print('max(abs(z2-z1))=%e'%max(abs(z2-z1)))
  print('max(abs(z3-z1))=%e'%max(abs(z3-z1)))
  print('max(abs(z4-z1))=%e'%max(abs(z4-z1)))
  
def feval3Ds01():  
  meshfile=gmsh.buildmesh3ds('demisphere5',30)
  Th=siMesh(meshfile)
  g1=lambda x,y,z: 3*x**2-y**3+z**2+x*y
  g2=lambda X: 3*X[0]**2-X[1]**3+X[2]**2+X[0]*X[1]
  
  def g3(x,y,z):
    return 3*x**2-y**3+z**2+x*y
  
  def g4(X):
    return 3*X[0]**2-X[1]**3+X[2]**2+X[0]*X[1]
  
  z1=Th.feval(g1)
  z2=Th.feval(g2)
  z3=Th.feval(g3)
  z4=Th.feval(g4)

  print('max(abs(z2-z1))=%e'%max(abs(z2-z1)))
  print('max(abs(z3-z1))=%e'%max(abs(z3-z1)))
  print('max(abs(z4-z1))=%e'%max(abs(z4-z1)))
  
def feval2D02():
  meshfile=gmsh.buildmesh2d('condenser11',50)
  Th=siMesh(meshfile)  
  f=lambda x,y: np.cos(2*x)*np.sin(3*y)

  def g(x,y,cx,cy): 
    return np.cos(cx*x)*np.sin(cy*y)

  g1=lambda x,y: g(x,y,2,3)
  g2=lambda X: g(X[0],X[1],2,3)

  z=Th.feval(f)
  z1=Th.feval(g1)
  z2=Th.feval(g2)

  print('max(abs(z1-z))=%e'%max(abs(z1-z)))
  print('max(abs(z2-z))=%e'%max(abs(z2-z)))
  
  
def feval3D02():  
  meshfile=gmsh.buildmesh3d('cylinderkey',15)
  Th=siMesh(meshfile)
  f=lambda x,y,z: 3*x**2-2*y**3+4*z**2-x*y
  
  def g(x,y,z,a,b,c,d):
    return a*x**2+b*y**3+c*z**2+d*x*y
  
  g1=lambda x,y,z: g(x,y,z,3,-2,4,-1)
  g2=lambda X: g(X[0],X[1],X[2],3,-2,4,-1)

  z=Th.feval(f)
  z1=Th.feval(g1)
  z2=Th.feval(g2)

  print('max(abs(z1-z))=%e'%max(abs(z1-z)))
  print('max(abs(z2-z))=%e'%max(abs(z2-z)))
  
def feval3Ds02():  
  meshfile=gmsh.buildmesh3ds('demisphere5',30)
  Th=siMesh(meshfile)
  f=lambda x,y,z: 3*x**2-2*y**3+4*z**2-x*y
  
  def g(x,y,z,a,b,c,d):
    return a*x**2+b*y**3+c*z**2+d*x*y
  
  g1=lambda x,y,z: g(x,y,z,3,-2,4,-1)
  g2=lambda X: g(X[0],X[1],X[2],3,-2,4,-1)

  z=Th.feval(f)
  z1=Th.feval(g1)
  z2=Th.feval(g2)

  print('max(abs(z1-z))=%e'%max(abs(z1-z)))
  print('max(abs(z2-z))=%e'%max(abs(z2-z)))  


def feval2D03():
  meshfile=gmsh.buildmesh2d('condenser11',50)
  Th=siMesh(meshfile)  
  # f : R^2 -> R^3
  f=[lambda x,y: np.cos(2*x)*np.sin(3*y),
    lambda x,y: np.cos(3*x)*np.sin(4*y),
    lambda x,y: np.cos(4*x)*np.sin(5*y)]
  
  g=[lambda X: np.cos(2*X[0])*np.sin(3*X[1]),
    lambda x,y: np.cos(3*x)*np.sin(4*y),
    lambda x,y: np.cos(4*X[0])*np.sin(5*X[1])]
  
  V1=Th.feval(f)
  V2=Th.feval(f)
  print('V1.shape='+str(V1.shape)+' V2.shape='+str(V2.shape))
  print('max(abs(V1-V2))=%e'%np.max(np.abs(V1-V2)))
  
def feval3D03():  
  meshfile=gmsh.buildmesh3d('cylinderkey',15)
  Th=siMesh(meshfile)
    # f : R^3 -> R^2
  f=[lambda x,y,z: np.cos(2*x)*np.sin(3*y)-z,
    lambda x,y,z: np.cos(3*x)*np.sin(4*y)+z]
  
  g=[lambda X: np.cos(2*X[0])*np.sin(3*X[1])-X[2],
    lambda x,y,z: np.cos(3*x)*np.sin(4*y)+z]
  
  V1=Th.feval(f)
  V2=Th.feval(f)
  print('V1.shape='+str(V1.shape)+' V2.shape='+str(V2.shape))
  print('max(abs(V1-V2))=%e'%np.max(np.abs(V1-V2)))
  
  
def feval3Ds03():  
  meshfile=gmsh.buildmesh3ds('demisphere5',30)
  Th=siMesh(meshfile)
    # f : R^3 -> R^2
  f=[lambda x,y,z: np.cos(2*x)*np.sin(3*y)-z,
    lambda x,y,z: np.cos(3*x)*np.sin(4*y)+z]
  
  g=[lambda X: np.cos(2*X[0])*np.sin(3*X[1])-X[2],
    lambda x,y,z: np.cos(3*x)*np.sin(4*y)+z]
  
  V1=Th.feval(f)
  V2=Th.feval(f)
  print('V1.shape='+str(V1.shape)+' V2.shape='+str(V2.shape))
  print('max(abs(V1-V2))=%e'%np.max(np.abs(V1-V2)))
  
def find2D01():
  meshfile=gmsh.buildmesh2d('condenser11',50)
  Th=siMesh(meshfile)
  print('*** 1: print mesh')
  print(Th)
  print('*** 2: print labels of the 2-simplex elementary meshes')
  idx=Th.find(2)
  print('d=2, labels='+str(Th.sThlab[idx]))
  print('*** 3: print labels of the 1-simplex elementary meshes')
  idx=Th.find(1)
  print('d=1, labels='+str(Th.sThlab[idx]))
  d=2;lab=6
  print('*** 4: print %d-simplex elementary meshes with label %d'%(d,lab))
  idx=Th.find(d,labels=lab)
  print('Th.sThlab[%d]=%s'%(idx,Th.sThlab[idx]))
  print('Th.sTh[%d] is the '%idx + str(Th.sTh[idx]))
  d=1;lab=101
  print('*** 5: print %d-simplex elementary meshes with label %d'%(d,lab))
  idx=Th.find(d,labels=lab)
  print('Th.sThlab[%d]=%s'%(idx,Th.sThlab[idx]))
  print('Th.sTh[%d] is the '%idx + str(Th.sTh[idx]))
  
def find3D01():  
  meshfile=gmsh.buildmesh3d('cylinder3dom',15)
  Th=siMesh(meshfile)
  print('*** 1: print mesh')
  print(Th)
  d=3
  print('*** 2: print labels of the %d-simplex elementary meshes'%d)
  idx=Th.find(d)
  print('d=%d, labels='%d +str(Th.sThlab[idx]))
  d=2
  print('*** 3: print labels of the %d-simplex elementary meshes'%d)
  idx=Th.find(d)
  print('d=%d, labels='%d +str(Th.sThlab[idx]))
  d=1
  print('*** 4: print labels of the %d-simplex elementary meshes'%d)
  idx=Th.find(d)
  print('d=%d, labels='%d +str(Th.sThlab[idx]))
  d=3;lab=10
  print('*** 5: print %d-simplex elementary meshes with label %d'%(d,lab))
  idx=Th.find(d,labels=lab)
  print('Th.sThlab[%d]=%s'%(idx,Th.sThlab[idx]))
  print('Th.sTh[%d] is the '%idx + str(Th.sTh[idx]))
  d=2;lab=112
  print('*** 6: print %d-simplex elementary meshes with label %d'%(d,lab))
  idx=Th.find(d,labels=lab)
  print('Th.sThlab[%d]=%s'%(idx,Th.sThlab[idx]))
  print('Th.sTh[%d] is the '%idx + str(Th.sTh[idx]))
  d=1;lab=120
  print('*** 7: print %d-simplex elementary meshes with label %d'%(d,lab))
  idx=Th.find(d,labels=lab)
  print('Th.sThlab[%d]=%s'%(idx,Th.sThlab[idx]))
  print('Th.sTh[%d] is the '%idx + str(Th.sTh[idx]))
  
def find3Ds01():  
  meshfile=gmsh.buildmesh3ds('demisphere5',30)
  Th=siMesh(meshfile)
  print('*** 1: print mesh')
  print(Th)
  d=2
  print('*** 2: print labels of the %d-simplex elementary meshes'%d)
  idx=Th.find(d)
  print('d=%d, labels='%d +str(Th.sThlab[idx]))
  d=1
  print('*** 3: print labels of the %d-simplex elementary meshes'%d)
  idx=Th.find(d)
  print('d=%d, labels='%d +str(Th.sThlab[idx]))
  d=0
  print('*** 4: print labels of the %d-simplex elementary meshes'%d)
  idx=Th.find(d)
  print('d=%d, labels='%d +str(Th.sThlab[idx]))
  d=2;lab=10
  print('*** 5: print %d-simplex elementary meshes with label %d'%(d,lab))
  idx=Th.find(d,labels=lab)
  print('Th.sThlab[%d]=%s'%(idx,Th.sThlab[idx]))
  print('Th.sTh[%d] is the '%idx + str(Th.sTh[idx]))
  d=1;lab=5
  print('*** 6: print %d-simplex elementary meshes with label %d'%(d,lab))
  idx=Th.find(d,labels=lab)
  print('Th.sThlab[%d]=%s'%(idx,Th.sThlab[idx]))
  print('Th.sTh[%d] is the '%idx + str(Th.sTh[idx]))
  d=0;lab=13
  print('*** 7: print %d-simplex elementary meshes with label %d'%(d,lab))
  idx=Th.find(d,labels=lab)
  print('Th.sThlab[%d]=%s'%(idx,Th.sThlab[idx]))
  print('Th.sTh[%d] is the '%idx + str(Th.sTh[idx]))
      
