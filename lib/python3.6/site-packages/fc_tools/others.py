import types,inspect,numpy
from inspect import getsource
#from dill.source import getsource
import os,sys,tempfile,shutil,subprocess

def isModuleFound(name,**kwargs):
  verbose=kwargs.get('verbose',False)
  isOk=True
  try:
    __import__(name)
  except ImportError:
    isOk=False
    if verbose:
      print('%s is not founded!'%name)
  return isOk

def LabelBaseName(dim,d):
  if (d==dim):
    return r"\Omega"
  if (d+1==dim):
    return r"\Gamma"
  if (d+2==dim):
    return r"\partial\Gamma"
  return r"\partial^{%d}\Gamma"%(dim-d-1)
  #if (d+3==dim):
    #return r"\partial^2\Gamma"
    
    
def LabelBaseNameSimp(dim,d,ds):
  if (d==dim):
    return LabelBaseName(dim,ds)
  if (d+1==dim):
    return LabelBaseName(dim,ds+1)
  if (d+2==dim):
    return LabelBaseName(dim,ds+2)
  if (d+3==dim):
    return LabelBaseName(dim,ds+3)
  
def print_packages(packages):
  #packages=['fc_tools','fc_hypermesh','fc_oogmsh','fc_simesh','fc_matplotlib4mesh']
  for name in packages:
    print('package %s:'%name)
    if isModuleFound(name):
      f=__import__(name)
      print('  path    : %s'%f.__path__[0])
      print('  version : %s'%f.__version__)
    else:
      print('  not found')
      
def is_lambda_function(obj):
  return isinstance(obj, types.LambdaType) and obj.__name__ == "<lambda>"    

def is_def_function(obj):
  return ( isinstance(obj, types.BuiltinFunctionType) or isinstance(obj, types.FunctionType) ) and obj.__name__ != "<lambda>"   

def is_vectorized_function(obj):
  return isinstance(obj,numpy.lib.function_base.vectorize)

def is_function(obj):
  return is_lambda_function(obj) or is_def_function(obj) or is_vectorized_function(obj)
    
def get_short_lambda_source(lambda_func):
    try:
        source_lines, _ = inspect.getsourcelines(lambda_func)
    except IOError:
        return None
    if len(source_lines) > 1:
        return None
    return source_lines[0].strip()
    
def get_short_lambda_source2(lambda_func):
  import inspect,ast
  try:
    source_lines, _ = inspect.getsourcelines(lambda_func)
  except IOError:
    return None
  if len(source_lines) > 1:
    return None
  source_text = source_lines[0].strip()
  lambda_node = get_short_lambda_ast_node(lambda_func)

  lambda_text = source_text[lambda_node.col_offset:]
  min_length = len('lambda:_')  # shortest possible lambda expression
  while len(lambda_text) > min_length:
    try:
      ast.parse(lambda_text)
      return lambda_text
    except SyntaxError:
      lambda_text = lambda_text[:-1]
  return None  
    
def get_short_lambda_ast_node(lambda_func):
  import ast
  source_text = get_short_lambda_source(lambda_func)
  if source_text:
    source_ast = ast.parse(source_text)
    return next((node for node in ast.walk(source_ast)
      if isinstance(node, ast.Lambda)), None)    
    
def func2str(u,**kwargs):
  source=kwargs.get('source',True)
  #assert is_function(u), 'invalid type : %s given'%str(type(u))
  if is_lambda_function(u):
    Str=get_short_lambda_source2(u)
    if not source:
      i=Str.find(':')
      Str=Str[i+1::]
    return Str
    #if source:
      #Str=getsource(u)#.replace('\n','')
    #else:
      #Str=getsource(u).replace('\n','')
      #i=Str.find(':')
      #Str=Str[i+1::]
    #return Str
  if is_def_function(u):
    if source:
      Str=getsource(u)
    else:
      if u.__module__=='__main__':
        Str=u.__name__
      else:
        Str=u.__module__+'.'+u.__name__
    return Str
  if is_vectorized_function(u):
    return func2str(u.pyfunc)
  return ''

def get_nargin(fun):
  from inspect import getargspec#getfullargspec
  #return len(getfullargspec(fun).args)
  return len(getargspec(fun).args)

class TemporaryDirectory(object):
  def __init__(self):
      self.tmp_dir = tempfile.mkdtemp()

  def __enter__(self):
      return self.tmp_dir

  def __exit__(self, type, value, traceback):
      shutil.rmtree(self.tmp_dir)
      self.tmp_dir = None

def latex_tag(imagein,imageout,string,**kwargs):
  density=kwargs.pop('density',100)
  scalefont=kwargs.pop('scalefont',5)
  latex_string = '''
    \\scalefont{%g}
    \\begin{tikzpicture}
    \\node[anchor=south west,inner sep=0] (image) at (0,0,0) {\\includegraphics{%s}};
    %s
    \\end{tikzpicture}
  '''.strip()
  template = '''
  \\documentclass[border=2mm,margin=10pt]{standalone}
  \\usepackage{anyfontsize}
  \\usepackage{scalefnt}
  \\usepackage[x11names,svgnames]{xcolor}
  \\usepackage{tikz}
  \\usepackage{pagecolor}
  \\begin{document}
      %s 
  \\end{document}
  '''.strip()
  S=latex_string % (scalefont,imagein,string)
  document = template % (S)
  with TemporaryDirectory() as tmp_dir:
      print(tmp_dir)
      with open(os.path.join(tmp_dir, 'math.tex'), 'w') as math_file:
          math_file.write(document)
      with open(os.devnull, 'w') as devnull:
          subprocess.check_call(['pdflatex', 'math.tex'], cwd=tmp_dir, stdout=devnull, stderr=devnull)
          #subprocess.check_call(['dvipng', '-bg', 'Transparent', '-D', str(dpi), '-T', 'tight', '-o', 'math.png',
                                  #'math.dvi'], cwd=tmp_dir, stdout=devnull, stderr=devnull)
          subprocess.check_call(['convert', '-density',str(density),'math.pdf', imageout], cwd=tmp_dir, stdout=devnull, stderr=devnull)
   
# kwargs={'cwd': ...}
def run_command(shell_cmd,**kwargs):
  verbose=kwargs.pop('verbose',0)
  try:
    out=None
    out=subprocess.check_output(shell_cmd,shell=True, stderr=subprocess.STDOUT,**kwargs)
  except subprocess.CalledProcessError:
    print('***[fc_tools]: Execution of %s failed!\n'%shell_cmd)
    if out is not None:
      Out=out.decode("utf-8")
      for line in Out.splitlines():
        print(line)
      sys.exit()
    else:
      print('***[fc_tools]: Try manually to see error messages')
      sys.exit()
  if verbose>0:
    if out is not None:
      Out=out.decode("utf-8")
      for line in Out.splitlines():
        print(line)
      print('  -> done!')
   
def latex_overlay(imageout,string,**kwargs):
  density=kwargs.pop('density',100)
  scalefont=kwargs.pop('scalefont',10)
  pagecolor=kwargs.pop('pagecolor','green')
  latex_string = '''
    \\pagecolor{%s}
    \\scalefont{%g}
    \\begin{tikzpicture}
    %s
    \\end{tikzpicture}
  '''.strip()
  template = '''
  \\documentclass{standalone}
  \\usepackage{anyfontsize}
  \\usepackage{scalefnt}
  \\usepackage[x11names,svgnames]{xcolor}
  \\usepackage{tikz}
  \\usepackage{pagecolor}
  \\begin{document}
      %s 
  \\end{document}
  '''.strip()
  S=latex_string % (pagecolor,scalefont,string)
  document = template % (S)
  with TemporaryDirectory() as tmp_dir:
      print(tmp_dir)
      with open(os.path.join(tmp_dir, 'math.tex'), 'w') as math_file:
          math_file.write(document)
      shutil.copyfile(tmp_dir+os.sep+'math.tex', imageout+'.tex')
      run_command('pdflatex math.tex',cwd=tmp_dir,**kwargs)
      shutil.copyfile(tmp_dir+os.sep+'math.pdf', imageout+'.pdf')
      run_command('convert -trim -transparent white -density '+str(density)+' '+imageout+'.pdf '+imageout+'.png',**kwargs)

def build_video(input_format,output):
  import os
  import tempfile
  import shutil
  import subprocess
  # avconv -f image2 -i tmp/%05d.png output.avi
  # avconv -i concat:"output.avi|output.avi|output.avi|output.avi|output.avi|output.avi|output.avi" -c copy output1.avi
  from fc_tools.others import TemporaryDirectory
  verbose=1
  with TemporaryDirectory() as tmp_dir:
    tmp_file=tmp_dir+os.sep+'tmp.avi'
    print('write in %s'%tmp_file)
    #with open(os.devnull, 'w') as devnull:
      #subprocess.check_call(['avconv', '-f', 'image2', '-r' , '50', '-i' , input_format , tmp_file], cwd=tmp_dir, stdout=devnull, stderr=devnull)
      #subprocess.check_call(['avconv', '-i', concat, '-c', 'copy' ,output], cwd=tmp_dir, stdout=devnull, stderr=devnull)
  #print('Creating video %s'%output)
    avconv_cmd="avconv -f image2 -r 50 -i %s %s"%(input_format,tmp_file)
    try:
      out=None
      out=subprocess.check_output(avconv_cmd,shell=True, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError:
      print('***[fc_vfemp1_eigs]: Execution of %s failed!\n'%avconv_cmd)
      if out is not None:
        Out=out.decode("utf-8")
        for line in Out.splitlines():
          print(line)
        sys.exit()
      else:
        print('***[fc_vfemp1_eigs]: Try manually to see error messages')
        sys.exit()
    if verbose>0:
      if out is not None:
        Out=out.decode("utf-8")
        for line in Out.splitlines():
          print(line)
        print('  -> done!')
    # avconv -i concat:"output.avi|output.avi|output.avi|output.avi|output.avi|output.avi|output.avi" -c copy output1.avi
    strc='|%s'%tmp_file
    concat='concat:"%s%s"'%(tmp_file,9*strc)
    avconv_cmd="avconv -i %s -c copy %s"%(concat,output)
    try:
      out=None
      out=subprocess.check_output(avconv_cmd,shell=True, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError:
      print('***[fc_vfemp1_eigs]: Execution of %s failed!\n'%avconv_cmd)
      if out is not None:
        Out=out.decode("utf-8")
        for line in Out.splitlines():
          print(line)
        sys.exit()
      else:
        print('***[fc_vfemp1_eigs]: Try manually to see error messages')
        sys.exit()
    if verbose>0:
      if out is not None:
        Out=out.decode("utf-8")
        for line in Out.splitlines():
          print(line)
        print('  -> done!')
    print('Creating video %s'%output)

def mkdir_p(path):
  import os,errno
  try:
      os.makedirs(path)
  except OSError as exc: # Python >2.5
      if exc.errno == errno.EEXIST and os.path.isdir(path):
          pass
      else: raise
    
def system_run(cmd_str,**kwargs):
  import  subprocess
  verbose=kwargs.get('verbose',1)
  name=kwargs.get('name','[fc_tools]')
  stop=kwargs.get('stop',True)
  if verbose>0:
    print('%s Command line:\n  %s'%(name,cmd_str))
    print('%s Running command. Be patient...'%name)
  try:
    out=None
    out=subprocess.check_output(cmd_str,shell=True, stderr=subprocess.STDOUT)
  except subprocess.CalledProcessError:
    if out is not None:
      Out=out.decode("utf-8")
      for line in Out.splitlines():
        print(line)
    else:
      print('%s Try manually to see error messages'%name)
    if stop:
      raise NameError('%s Execution of %s failed!\n'%(name,cmd_str))
    else:
      print('%s Execution of %s failed!\n'%(name,cmd_str))
      return False

  if verbose>1:
    if out is not None:
      print('%s Printing command output:'%name)
      Out=out.decode("utf-8")
      for line in Out.splitlines():
        print(line)
  return True

def system_run_out(cmd_str,**kwargs):
  # Return output of the command
  import  subprocess
  verbose=kwargs.get('verbose',1)
  name=kwargs.get('name','[fc_tools]')
  stop=kwargs.get('stop',True)
  shell=kwargs.get('shell',True)
  if verbose>0:
    print('%s Command line:\n  %s'%(name,cmd_str))
    print('%s Running command. Be patient...'%name)
  try:
    out=None
    out=subprocess.check_output(cmd_str,shell=shell, stderr=subprocess.STDOUT)
  except subprocess.CalledProcessError:
    if out is not None:
      Out=out.decode("utf-8")
      for line in Out.splitlines():
        print(line)
    else:
      print('%s Try manually to see error messages'%name)
    if stop:
      raise NameError('%s Execution of %s failed!\n'%(name,cmd_str))
    else:
      print('%s Execution of %s failed!\n'%(name,cmd_str))
      return False
  
  if out is not None:
    Out=out.decode("utf-8")
  else:
    Out=''
  return Out

def simplicial_dimension(q,me,**kwargs):
  """
    

    Parameters
    ----------
    q : mesh vertices, dim-by-nq or nq-by-dim numpy array where
        dim is the space dimension (2 or 3) and nq the number of vertices.
    me: mesh elements connectivity array where elements are d-simplices. 
        me is a (d+1)-by-nme or nme-by-(d+1) numpy array where nme is the number
        of mesh elements and d is the simplicial dimension:
          d=0: points, 
          d=1: lines, 
          d=2: triangle, 
          d=3: tetrahedron
        default suppose to be (d+1)-by-nme when mesh is too small.
        
    Returns
    -------
    q  : The mesh vertices as a nq-by-dim numpy array
    me : The mesh elements connectivity array as nme-by-(d+1) numpy array
    dim: The space dimension
    d  : The simplicial dimension
  """
  assert (q.shape[0] <=3) or (q.shape[1] <=3)
  if q.shape[1] >3 :
    q=q.T
  dim=q.shape[1]
  d=kwargs.pop('d', None)
  assert (me.shape[0] <=dim+1) or (me.shape[1] <=dim+1)
  if (me.shape[0] <=dim+1) and (me.shape[1] <=dim+1):
    #print('Mesh too small to guess d-simplices dimension')
    #print(me.shape)
    #if me.shape[1]> me.shape[0]: # 
    if d is None:
      me=me.T
    else:
      if me.shape[0]==d+1:
        me=me.T
      assert me.shape[1]==d+1
  elif me.shape[1] >dim+1:
    me=me.T
  d=me.shape[1]-1
  return q,me,dim,d
