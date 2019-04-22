import numpy as np
from math import factorial
import fc_hypermesh.CartesianGrid as CG

def KuhnTriangulation(d):
  q=CG.points(np.ones(d))
  qref=np.vstack([np.zeros((1,d)),np.tril(np.ones((d,d)))]).T
  P=CG.perms(np.arange(d))
  nme=factorial(d);nq=2**d
  me=np.zeros((d+1,nme),dtype=int)
  A=np.matrix(2**np.arange(d))
  for k in range(nme):
    me[:,k]=A*qref[P[k]]
    ql=q[:,me[:,k]]
    s=orientation(ql)
    if (s==-1):
      tmp=me[0,k]
      me[0,k]=me[d,k]
      me[d,k]=tmp
  return q,me

def orientation(ql):
  #d=ql.shape[1]
  #D=np.c_[np.ones((d+1,1)),ql]
  d=ql.shape[0]
  D=np.r_[np.ones((1,d+1)),ql]
  return np.sign(np.linalg.det(D))

def Faces(N,m):
  N=np.array(N)
  d=len(N)
  sTh=CG.TriFaces(N,m)
  for k in range(len(sTh)):
    for i in range(d):
      sTh[k].q[i]/=N[i]
  return sTh

def Triangulation(N):
  d=len(N)
  q,me=CG.Triangulation(N)
  for i in range(d):
    q[i,:]/=N[i]
  return q,me