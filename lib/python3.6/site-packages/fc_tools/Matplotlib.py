import sys,os
import matplotlib
import matplotlib.pyplot as plt

import numpy as np

from .others import isModuleFound

def get_colormap_names():
   maps=[m for m in plt.cm.datad if not m.endswith("_r")]
   maps.sort()
   return maps

def set_axes_equal(**kwargs):
  '''Make axes of 3D plot have equal scale so that spheres appear as spheres,
  cubes as cubes, etc..  This is one possible solution to Matplotlib's
  ax.set_aspect('equal') and ax.axis('equal') not working for 3D.
  
  Options:
    ax: a matplotlib axis, e.g., as output from plt.gca().
    fig: a matplotlib figure, e.g., as output from plt.gcf().
    
  Taken from http://stackoverflow.com/a/31364297/480551 and
  from http://stackoverflow.com/questions/41818245/inconsistent-figure-coordinates-in-matplotlib-with-equal-aspect-ratio
  
  '''
  fig=kwargs.get('fig',plt.gcf())
  ax=kwargs.get('ax',plt.gca())
  if not hasattr(ax, 'get_zlim'):
    plt.axis('equal')
    return
  
  fig.canvas.draw()
  ax.set_aspect('equal')
  x_limits = ax.get_xlim3d()
  y_limits = ax.get_ylim3d()
  z_limits = ax.get_zlim3d()
  x_range = x_limits[1] - x_limits[0]; x_mean = np.mean(x_limits)
  y_range = y_limits[1] - y_limits[0]; y_mean = np.mean(y_limits)
  z_range = z_limits[1] - z_limits[0]; z_mean = np.mean(z_limits)
  # The plot bounding box is a sphere in the sense of the infinity
  # norm, hence I call half the max range the plot radius.
  plot_radius = 0.5*max([x_range, y_range, z_range])
  ax.set_xlim3d([x_mean - plot_radius, x_mean + plot_radius])
  ax.set_ylim3d([y_mean - plot_radius, y_mean + plot_radius])
  ax.set_zlim3d([z_mean - plot_radius, z_mean + plot_radius])
  
def set_axes(ax,bbox):
  if len(bbox)==2:
    return
  if hasattr(ax, 'set_xlim3d'):
    if bbox[1]-bbox[0]>1e-10:
      ax.set_xlim3d(bbox[[0,1]])
    if bbox[3]-bbox[2]>1e-10:
      ax.set_ylim3d(bbox[[2,3]])
    if len(bbox)==6:
      if bbox[5]-bbox[4]>1e-10:
        ax.set_zlim3d(bbox[[4,5]])
  else:
    if bbox[1]-bbox[0]>1e-10:
      ax.set_xlim(bbox[[0,1]])
    if bbox[3]-bbox[2]>1e-10:
      ax.set_ylim(bbox[[2,3]])
  
  
def DisplayFigures(**kwargs):
  """ Distributes and resizes a set of figures on screen
    
  Syntax:
  
    DisplayFigures()
    DisplayFigures(nfig=value)
    DisplayFigures(screen=value)
  
  Without option, distributes and resizes all the previously created matplotlib 
  figures on screen. On multi-screen computer, one can select screen with the
  screen option (1st screen : DisplayFigures(screen=0) )
  One can also used nfig option to specify the numbers of figures. 
  
  Needs screeninfo package.
  
  Copyright 2017 by F. Cuvelier
  """
  if not isModuleFound('screeninfo'):
    return
  if sys.platform=='darwin':
    # import warnings
    # warnings.warn('fc_tools.Matplotlib.DisplayFigures function not yet implemented for DARWIN platform')
    return
  from screeninfo import get_monitors
  backend=matplotlib.backends.backend
  
  nfig=kwargs.get('nfig',0)
  screen=kwargs.get('screen',0)
  lfigs=np.arange(1,nfig+1)
  if nfig==0:
    lfigs=plt.get_fignums() # list of figure numbers
    nfig=len(lfigs)
  if nfig<=1:
    return
  if nfig<=4:
    nrow=2;ncol=2;
  elif nfig<=6:
    nrow=2;ncol=3;
  elif nfig<=9:
    nrow=3;ncol=3;  
  elif nfig<=12:
    nrow=3;ncol=4;
  elif nfig<=16:
    nrow=4;ncol=4;
  elif nfig<=20:
    nrow=4;ncol=5;
  else:
    print('To many figures!')
    return
  M=get_monitors()
  if len(M)<screen+1:
    print('Screen number %d not found! -> set to 0'%screen)
    screen=0
  h=M[screen].height
  w=M[screen].width
  posx=M[screen].x
  posy=M[screen].y
  #mgr = plt.get_current_fig_manager()
  #w = mgr.canvas.width()
  #h = mgr.canvas.height()
  w=3./4*w;h=3./4*h;
  wp=w/ncol;
  hp=h/nrow;
  k=0
  yp=20+posy
  d = 10  # width of the window border in pixels
  dd= 70 # menu in pixels
  for i in range(nrow):
    xp=100+posx
    for j in range(ncol):
      if k>=nfig:
        return
      fig=plt.figure(lfigs[k])
      SetGeometry(xp, yp, wp, hp)
      #mgr = plt.get_current_fig_manager()
      #mgr.window.setGeometry(xp, yp, wp, hp)
      xp=xp+wp+d
      k+=1
      #fig.canvas.draw() # ? for real time plotting
      fig.canvas.flush_events() # for real time plotting https://github.com/matplotlib/matplotlib/issues/7759/ from tacasweel 
    yp=yp+hp+d+dd
    
def SetGeometry(xp, yp, wp, hp):
  plt.gcf()
  backend=matplotlib.backends.backend
  mgr = plt.get_current_fig_manager()
  if backend.lower()=='qt5agg':
    mgr.window.setGeometry(xp, yp, wp, hp)
  elif backend.lower()=='qt4agg':
    mgr.window.setGeometry(xp, yp, wp, hp)  
  elif backend.lower()=='tkagg':
    mgr.window.geometry(newGeometry='%dx%d+%d+%d'%(wp,hp,xp,yp))
  else:
    print('SetGeometry not yet implemented for %s backend'%backend)
    
def SaveFigAsFile(fignum,filename,**kwargs):
  """ Save matplotlib figure number `fignum` as file `filename`
    
  Syntax:
  
    SaveFigAsFile(fignum,filename)
    SaveFigAsFile(fignum,filename,key=value)
 
  
  Option keys are
    - format: to specify file format. Default is 'eps'. (see matplotlib.pyplot.savefig)
    - tag: if True, tag the file name with python version as 
        'filename_fig<num>_Python<version>.eps'
      where <version> the python version without '.'.
      Default is False.
    - dir: to specify the directory where the files will be written. 
      Default current directory.
    - verbose: if True print some informations. Default False.
  
  Copyright 2017 by F. Cuvelier
  """
  tag=kwargs.get('tag', False )
  figext=kwargs.get('format', 'png' )
  savedir=kwargs.get('dir', '.' )
  verbose=kwargs.get('verbose',False)
  scale=kwargs.get('scale', 1.0 )
  size=kwargs.get('size', [800,600] ) # in pixels
  dpi=kwargs.get('dpi', 100 ) 
  if tag:
    Softname='Python'
    V=sys.version.split(' ')[0]
    Release=V.replace('.','')
    
  if not os.path.exists(savedir):
    os.makedirs(savedir)
    
  Fignums=np.array(plt.get_fignums())
  A=np.where(Fignums==fignum)[0]
  if len(A)==0:
    print('*** fc_tools:Warning: No figure %d to save'%numfig)
    return
  if tag:
    File=savedir+os.path.sep+filename+'_'+Softname+Release+'.'+figext
  else:
    File=savedir+os.path.sep+filename+'.'+figext
      
  fig=plt.figure(fignum)
  fig.set_dpi(dpi)
  fig.set_size_inches(np.array(size)/dpi)
  if scale != 1:
    fig.set_size_inches(scale*fig.get_size_inches())
  
  ax=plt.gca()
  fig.set_rasterized(True)
  if verbose:
    print('  Save figure %d in %s'%(fignum,File))
  fig.savefig(File,bbox_inches='tight',bbox_extra_artists=ax.get_default_bbox_extra_artists())    
    
def SaveAllFigsAsFiles(filename,**kwargs):
  """ Save all matplotlib figures as files 
    
  Syntax:
  
    SaveAllFigsAsFiles(filename)
    SaveAllFigsAsFiles(filename,key=value)
  
  Save each opened figure in file 'filename_fig<num>.eps' where <num> is the
  figure number.
  
  Option keys are
    - format: to specify file format. Default is 'eps'. (see matplotlib.pyplot.savefig)
    - tag: if True, tag the file name with python version as 
        'filename_fig<num>_Python<version>.eps'
      where <version> the python version without '.'.
      Default is False.
    - dir: to specify the directory where the files will be written. 
      Default current directory.
    - verbose: if True print some informations. Default False.
  
  Copyright 2017 by F. Cuvelier
  """
  tag=kwargs.get('tag', False )
  figext=kwargs.get('format', 'png' )
  savedir=kwargs.get('dir', '.' )
  verbose=kwargs.get('verbose',False)
  scale=kwargs.get('scale', 1.0 )
  size=kwargs.get('size', [800,600] ) # in pixels
  dpi=kwargs.get('dpi', 100 ) 
  if tag:
    Softname='Python'
    V=sys.version.split(' ')[0]
    Release=V.replace('.','')
    
  if not os.path.exists(savedir):
    os.makedirs(savedir)
    
  Fignums=plt.get_fignums()
  for nfig in Fignums:
    if tag:
      File=savedir+os.path.sep+filename+'_fig'+str(nfig)+'_'+Softname+Release+'.'+figext
    else:
      File=savedir+os.path.sep+filename+'_fig'+str(nfig)+'.'+figext
      
    fig=plt.figure(nfig)
    fig.set_dpi(dpi)
    fig.set_size_inches(np.array(size)/dpi)
    if scale != 1:
      fig.set_size_inches(scale*fig.get_size_inches())
    
    ax=plt.gca()
    fig.set_rasterized(True)
    if verbose:
      print('  Save figure %d in %s'%(nfig,File))
    fig.savefig(File,bbox_inches='tight',bbox_extra_artists=ax.get_default_bbox_extra_artists())
    
def error_colorbar_format():
  from matplotlib import ticker
  sfmt=ticker.ScalarFormatter(useMathText=True) 
  sfmt.set_powerlimits((0, 0))
  return sfmt

def showSparsity(M):
#  from matplotlib.pyplot as plt
  plt.spy(M, precision=1e-8, marker='.', markersize=3)
  plt.show()
