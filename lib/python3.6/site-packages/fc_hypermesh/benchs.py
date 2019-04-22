import time
from . import OrthMesh

def bench01(d,ctype,Box,LN):
  #d=3
  #ctype='simplicial'
  #Box=[[-1,1],[-1,1],[-1,1]]
  #LN=range(20,170,20)
  Oh=OrthMesh(d,2,type=ctype,box=Box) # To force compilation
  print('# BENCH in dimension %d with %s mesh'%(d,ctype))
  print('#d: %d'%d)
  print('#type: %s'%ctype)
  print('#box: %s'%str(Box))
  print('#desc:  N        nq       nme    time(s)')
  for N in LN:
    tstart=time.time()
    Oh=OrthMesh(d,N,type=ctype,box=Box)
    t=time.time()-tstart
    print('     %4d  %8d  %8d     %2.3f'%(N,Oh.Mesh.nq,Oh.Mesh.nme,t))
    
def allbenchs():
  bench01(2,'orthotope',[[-1,1],[-1,1]],range(1000,5000,1000))
  bench01(3,'orthotope',[[-1,1],[-1,1],[-1,1]], range(50,300,50))
  bench01(4,'orthotope',[[-1,1],[-1,1],[-1,1],[-1,1]], [10,20,30,40,50])
  bench01(5,'orthotope',[[-1,1],[-1,1],[-1,1],[-1,1],[-1,1]], [5,10,15,20,25])
  bench01(2,'simplicial',[[-1,1],[-1,1]],range(1000,5000,1000))
  bench01(3,'simplicial',[[-1,1],[-1,1],[-1,1]], range(40,170,20))
  bench01(4,'simplicial',[[-1,1],[-1,1],[-1,1],[-1,1]], range(10,30,4))
  bench01(5,'simplicial',[[-1,1],[-1,1],[-1,1],[-1,1],[-1,1]], range(2,12,2))