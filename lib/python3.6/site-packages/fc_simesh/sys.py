import os
import fc_oogmsh

def get_geodirs(dim,d):
  s=get_pathname(dim,d)
  assert s is not None,"Unable to find geo directory for dim=%d and d=%d"%(dim,d)
  fullname=os.path.dirname(os.path.abspath(__file__))
  loc_dir=fullname+os.sep+'geodir'+os.sep+s
  return [loc_dir,fc_oogmsh.sys.get_geodirs(dim,d)]
  
def get_pathname(dim,d):
  if dim==2 and d==2:
    return '2d'
  if dim==3 and d==2:
    return '3ds'
  if dim==3 and d==3:
    return '3d'
  return None