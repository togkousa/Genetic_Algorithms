import sys,os
import numpy as np
import mayavi 
from mayavi import mlab
from tvtk.api import tvtk
import tempfile
import shutil
import subprocess

def find_Colors_and_legends(figs,prev_found):
  if not hasattr(figs, '__iter__'):
    if isinstance(figs,mayavi.core.module_manager.ModuleManager):
      prev_found.append(figs)
    elif hasattr(figs, 'children'):
      for ch in figs.children:
        prev_found=find_Colors_and_legends(ch,prev_found)
    return prev_found

  for f in figs:
    if isinstance(f,mayavi.core.module_manager.ModuleManager):
      prev_found.append(f)
    elif hasattr(f, 'children'):
      for ch in f.children:
        prev_found=find_Colors_and_legends(ch,prev_found)
  return prev_found

# get objects mayavi.core.lut_manager.LUTManager
def get_colorbars(**kwargs):
  enable=kwargs.pop('enable',None)
  figure=kwargs.pop('figure',None)
  if figure is None:
    F=find_Colors_and_legends(mlab.get_engine().scenes,[])
  else:
    assert(isinstance(figure,mayavi.core.scene.Scene)) # use mlab.figure(1)
    F=find_Colors_and_legends(figure,[])
  CBs=[]
  for f in F:
    slm=f.trait_get()['scalar_lut_manager']
    if enable is None:
      CBs.append(slm)
    elif slm.show_scalar_bar==enable:
      CBs.append(slm)
    slm=f.trait_get()['vector_lut_manager']
    if enable is None:
      CBs.append(slm)
    elif slm.show_scalar_bar==enable:
      CBs.append(slm)
  return CBs

# option='label_text_property' for example
def get_colorbars_option(option,**kwargs):
  CBs=get_colorbars(**kwargs)
  CBOs=[]
  for cb in CBs:
    CBOs.append(cb.trait_get()[option])
  return CBOs

def set_colorbars_option(option,**kwargs):
  CBs=get_colorbars(**kwargs)
  for cb in CBs:
    cbo=cb.trait_get()[option]
    cbo.trait_set(**kwargs)
    
# set_scenes(background=(1,1,1))
def set_scenes(**kwargs):
  for s in mlab.get_engine().scenes:
    s.scene.trait_set(**kwargs)

# set_colormap(mlab.figure(1),'viridis')
# set_colormap(mlab.figure(1),'jet')
def set_colormap(fig,cmap):
  CBs=get_colorbars(figure=fig)
  for cb in CBs:
    cb.lut_mode=cmap

###
 #'background_color': (0.0, 0.0, 0.0),
 #'background_opacity': 0.0,
 #'bold': 1,
 #'bold_': 1,
 #'class_name': 'vtkTextProperty',
 #'color': (1.0, 1.0, 1.0),
 #'debug': False,
 #'debug_': 0,
 #'font_family': 'arial',
 #'font_family_min_value': 0,
 #'font_file': None,
 #'font_size': 12,
 #'global_warning_display': 1,
 #'global_warning_display_': 1,
 #'italic': 1,
 #'italic_': 1,
 #'justification': 'left',
 #'line_offset': 0.0,
 #'line_spacing': 1.1,
 #'m_time': 1950933,
 #'opacity': 1.0,
 #'orientation': 0.0,
 #'reference_count': 2,
 #'shadow': 0,
 #'shadow_': 0,
 #'shadow_offset': array([ 1, -1]),
 #'vertical_justification': 'bottom'}
### 
def set_colorbar_text(CandLs,**kwargs):
  if not hasattr(CandLs, '__iter__'):
    if isinstance(CandLs,tvtk.tvtk_classes.text_property.TextProperty):
      CandL.trait_set(**kwargs)
  for cl in CandLs:
    set_colorbar_text(cl,**kwargs)

def vtk_SaveAllFigsAsFiles_old(filename,**kwargs):
  tag=kwargs.get('tag', False )
  figext=kwargs.get('format', 'png' )
  savedir=kwargs.get('dir', '.' )
  figs=kwargs.get('figs',None) # list of figures number
  verbose=kwargs.get('verbose',False)
  scale=kwargs.get('scale', 1.0 )
  #if not isMayavi():
    #print('Needs Mayavi ...')
    #return

  if tag:
    Softname='Python'
    V=sys.version.split(' ')[0]
    Release=V.replace('.','')
    Tag=Softname+Release
    # FullTag=Tag+'_Mayavi'+mayavi.__version__.replace('.','') 
    
  if not os.path.exists(savedir):
    os.makedirs(savedir)
    
  set_colorbars_option('label_text_property',color=(0,0,0))
  for i in range(len(figs)):
    nfig=figs[i]
    if tag:
      File=savedir+os.path.sep+filename+'_fig'+str(nfig)+'_'+Tag+'.'+figext
    else:
      File=savedir+os.path.sep+filename+'_fig'+str(nfig)+'.'+figext
                   
    fig=mlab.figure(nfig)
    old_bg=fig.scene.background
    fig.scene.background=(1, 1, 1)
    #old_fg=fig.scene.foreground
    #fig.scene.foreground=(0, 0, 0)
    if verbose:
      print('  Save Mayavi Scene %d in %s'%(nfig,File))
    mlab.savefig(File,magnification=scale) 
    fig.scene.background=old_bg
    #fig.scene.foreground=old_fg
    
def SaveAllFigsAsFiles(filename,**kwargs):
  vtk_SaveAllFigsAsFiles(filename,**kwargs)
  
def vtk_SaveAllFigsAsFiles(filename,**kwargs):
  tag=kwargs.get('tag', False )
  figext=kwargs.get('format', 'png' )
  savedir=kwargs.get('dir', '.' )
  figs=kwargs.get('figs',None) # list of figures number
  verbose=kwargs.get('verbose',False)
  scale=kwargs.get('scale', 1.0 )
  #if not isMayavi():
    #print('Needs Mayavi ...')
    #return

  if tag:
    Softname='Python'
    V=sys.version.split(' ')[0]
    Release=V.replace('.','')
    Tag=Softname+Release
    # FullTag=Tag+'_Mayavi'+mayavi.__version__.replace('.','') 
    
  if not os.path.exists(savedir):
    os.makedirs(savedir)
  set_colorbars_option('label_text_property',color=(0,0,0))
  set_colorbars_option('title_text_property',color=(0,0,0))
  scenes=mlab.get_engine().scenes
  for i in range(len(scenes)):
    sc=scenes[i]
    fig=mlab.figure(sc) # set as current
    nfig=sc.name[13::] # sc.name is 'Mayavi Scene <NUM>'
    #nfig=figs[i]
    if tag:
      File=savedir+os.path.sep+filename+'_fig'+nfig+'_'+Tag+'.'+figext
    else:
      File=savedir+os.path.sep+filename+'_fig'+nfig+'.'+figext
                   
    old_bg=fig.scene.background
    fig.scene.background=(1, 1, 1)
    #old_fg=fig.scene.foreground
    #fig.scene.foreground=(0, 0, 0)
    if verbose:
      print('  Save Mayavi Scene %s in %s'%(nfig,File))
    mlab.savefig(File,magnification=scale) 
    fig.scene.background=old_bg
    #fig.scene.foreground=old_fg
    
def fc_legend(names,colors,d,txt=None):
  legendBox = tvtk.LegendBoxActor()
  legendBox.background_color=(0.9,0.9,0.9)
  legendBox.background_opacity=0.8
  legendBox.trait_set(use_background=True)
  istart=0
  if txt is not None:
    names.insert(0,txt)
    colors.insert(0,[0,0,0])
    istart=1
  
  legendBox.number_of_entries=len(names)
  
  points0 = np.array([[0,0,0], [1,0,0]], 'f')
  lines0 = np.array([[0]])
  mesh0 = tvtk.PolyData(points=points0, lines=lines0)
  
  if istart==1:
    legendBox.set_entry(0, mesh0, str(names[0]), tuple(colors[0]))
  
  if d==3:
    points = np.array([[-1,0,0], [1,0,0], [0,1,0], [0,0.5,0]], 'f')
    lines = np.array([[0,1],[1,2],[2,0],[0,3],[1,3],[2,3]])
    #mesh = tvtk.PolyData(points=points, lines=lines)
  if d==2:
    points = np.array([[0,0,0], [1,0,0], [0,1,0]], 'f')
    lines = np.array([[0,1],[1,2],[2,0]])
    #mesh = tvtk.PolyData(points=points, lines=lines)
  if d==1:
    points = np.array([[0,0,0], [1,0,0]], 'f')
    lines = np.array([[0,1]])
    
  mesh = tvtk.PolyData(points=points, lines=lines)

  for i in range(istart,len(names)):
    #legendBox.set_entry(i, mesh, handles[i].name, handles[i].actor.property.color)
    legendBox.set_entry(i, mesh, str(names[i]), tuple(colors[i]))
  fig=mlab.gcf() 
  fig.scene.add_actor(legendBox)
  
def title(text,**kwargs):
  """ textproperty options
    textproperty={
      'background_color': (0.0, 1.0, 0.0),
      'background_opacity': 0.1143,
      'bold': 1,
      'color': (0.0, 0.0, 0.0),
      'font_family': 'arial',
      'font_family_min_value': 0,
      'font_file': None,
      'font_size': 16,
      'italic': 0,
      'italic_': 0,
      'justification': 'centered',
      'line_offset': 0.0,
      'line_spacing': 1.1,
      'opacity': 1.0,
      'orientation': 0.0,
      'shadow': 1,
      'shadow_offset': array([ 1, -1]),
      'vertical_justification': 'top'
    }
  """ 
  justification=kwargs.pop('justification','center')
  vertical_justification=kwargs.pop('vertical_justification','top')
  textproperty=kwargs.pop('textproperty',dict())
  kwargs['color']=check_color(kwargs.pop('color', 'White'))
  t=mlab.text(0.5,0.99,text,**kwargs)
  t.actor.text_scale_mode='none'
  t.actor.text_property.justification=justification
  t.actor.text_property.vertical_justification=vertical_justification
  if len(textproperty):
    t.actor.text_property.trait_set(**textproperty)
  return t

class TemporaryDirectory(object):
  def __init__(self):
      self.tmp_dir = tempfile.mkdtemp()

  def __enter__(self):
      return self.tmp_dir

  def __exit__(self, type, value, traceback):
      shutil.rmtree(self.tmp_dir)
      self.tmp_dir = None
        
# inspired from https://pgi-jcns.fz-juelich.de/portal/pages/latex-mayavi.html        
def latex_out(string,preamble='',dpi=900):
  import PIL.Image as Image
  template = '''
  \\documentclass[margin=10pt]{standalone}
  %s
  \\begin{document}
      %s 
  \\end{document}
  '''.strip()
  document = template % (preamble,string)
  with TemporaryDirectory() as tmp_dir:
      with open(os.path.join(tmp_dir, 'math.tex'), 'w') as math_file:
          math_file.write(document)
      with open(os.devnull, 'w') as devnull:
          subprocess.check_call(['latex', 'math.tex'], cwd=tmp_dir, stdout=devnull, stderr=devnull)
          subprocess.check_call(['dvipng', '-bg', 'Transparent', '-D', str(dpi), '-T', 'tight', '-o', 'math.png',
                                  'math.dvi'], cwd=tmp_dir, stdout=devnull, stderr=devnull)
      math_img = Image.open(os.path.join(tmp_dir, 'math.png'))
      
  math_img_array = np.flip(np.array(Image.Image.convert(math_img,mode='F')).T,1)
  return math_img_array

def mlab_latex3D(latex_string, **kwargs):
  preamble=kwargs.pop('preamble','')
  dpi=kwargs.pop('dpi',900)
  kwargs['mode']=kwargs.pop('mode','point')
  kwargs['color']=check_color(kwargs.pop('color','White'))
  width=kwargs.pop('width',None)
  height=kwargs.pop('heigth',1.0)
  center=kwargs.pop('center',(0,0,0))
  img_array = latex_out(latex_string,preamble,dpi)
  index_array = np.where(img_array != 255)
  x=index_array[0];y=index_array[1]
  minx=x.min();miny=y.min()
  maxx=x.max();maxy=y.max()
  if width is not None:
    hx=(maxx-minx)/width
    x=(x-minx)/hx;y=(y-miny)/hx
    x=x-(x.max()-x.min())/2+center[0]
    y=y-(y.max()-y.min())/2+center[1]
  else:
    hy=(maxy-miny)/height
    x=(x-minx)/hy;y=(y-miny)/hy
    x=x-(x.max()-x.min())/2+center[0]
    y=y-(y.max()-y.min())/2+center[1]
  z=np.zeros(x.shape)+center[2]
  return mlab.points3d(x,y,z,name='LaTeX3D',**kwargs)

  #fig = mlab.gcf()
  #fig.scene._renwin.size
  #fig.scene._renwin.position
  #fig.scene.control.setFixedSize(1024,768)

from fc_tools.colors import check_color
