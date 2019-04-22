import fc_oogmsh

def demo01(**kwargs):
  print('***********************')
  print('Running demo01 function')
  print('***********************')
  print('*** fc_oogmsh.buildmesh2d : 1st call')
  meshfile=fc_oogmsh.buildmesh2d('condenser11',25,force=True,verbose=3,**kwargs)
  print('*** fc_oogmsh.buildmesh2d : 2nd call')
  meshfile=fc_oogmsh.buildmesh2d('condenser11',25,force=True,**kwargs)
  print('*** fc_oogmsh.buildmesh2d : 3th call')
  meshfile=fc_oogmsh.buildmesh2d('condenser11',25,**kwargs)
  
def demo02(**kwargs):
  print('***********************')
  print('Running demo02 function')
  print('***********************')
  print('*** Build mesh file')
  meshfile=fc_oogmsh.buildmesh2d('condenser11',25,force=True,**kwargs)
  print('*** Read mesh file')
  oGh=fc_oogmsh.ooGmsh(meshfile)
  print('*** Print oGh ->')
  print(oGh)
  print('*** Print oGh.sElts[0] ->')
  print(oGh.sElts[0])
  
def demo03(**kwargs):
  print('***********************')
  print('Running demo03 function')
  print('***********************')
  print('*** Building the mesh')
  meshfile=fc_oogmsh.buildmesh2d('condenser11',25,**kwargs);
  print('*** Partitioning the mesh')
  pmfile=fc_oogmsh.buildpartmesh(meshfile,5,force=True,**kwargs);
  oGh=fc_oogmsh.ooGmsh(pmfile)
  print('*** Print oGh ->')
  print(oGh)
  print('*** Print oGh.sElts[0] ->')
  print(oGh.sElts[0])
  
def demo04(**kwargs):
  print('***********************')
  print('Running demo04 function')
  print('***********************')
  print('*** Build mesh file')
  #pmfile=fc_oogmsh.buildpartrectangle(1,1,3,2,100,force=True, verbose=3,options='-string "Mesh.Partitioner=2;" -string "Mesh.MetisAlgorithm=3;"',**kwargs)
  pmfile=fc_oogmsh.buildpartrectangle(1,1,3,2,100,force=True, verbose=3,options='-string "Mesh.MetisAlgorithm=3;"',**kwargs)
  print('*** Read mesh file')
  oGh=fc_oogmsh.ooGmsh(pmfile)
  print('*** Print oGh ->')
  print(oGh)
  print('*** Print oGh.sElts[0] ->')
  print(oGh.sElts[0])
  
def demo05(**kwargs):
  print('***********************')
  print('Running demo05 function')
  print('***********************')
  print('*** Building the partitioned mesh')
  meshfile=fc_oogmsh.buildmesh2d('condenser11',25,force=True, options='-part 5', savemesh='./toto.msh',verbose=3,**kwargs);
  print('*** Reading the mesh file')
  oGh=fc_oogmsh.ooGmsh(meshfile)
  print('*** Print oGh ->')
  print(oGh)
  print('*** Print oGh.sElts[1] ->')
  print(oGh.sElts[1])
  print('*** Print oGh.sElts[1].part_lab ->')
  print(oGh.sElts[1].part_lab)
  
def alldemos(**kwargs):
  for i in range(1,6):
    eval('demo'+'%02d'%i+'(**kwargs)')
