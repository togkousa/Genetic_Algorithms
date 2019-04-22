import os #,platform
#from cpuinfo import program_paths,run_and_get_stdout
#from cpuinfo import run_and_get_stdout

# Comme from: https://stackoverflow.com/questions/377017/test-if-executable-exists-in-python
def which(program):
  import os
  def is_exe(fpath):
      return os.path.isfile(fpath) and os.access(fpath, os.X_OK)

  fpath, fname = os.path.split(program)
  if fpath:
      if is_exe(program):
          return program
  else:
      for path in os.environ["PATH"].split(os.pathsep):
          exe_file = os.path.join(path, program)
          if is_exe(exe_file):
              return exe_file

  return None
  
def program_paths(program):
  return which(program)

def program_in_paths(program):
  return not( which(program) is None )

# from https://github.com/workhorsy/py-cpuinfo/blob/master/cpuinfo/cpuinfo.py line 236
def run_and_get_stdout(command, pipe_command=None):
  import subprocess,sys
  if not pipe_command:
    p1 = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    output = p1.communicate()[0]
    if not (sys.version_info[0] == 2):
      output = output.decode(encoding='UTF-8')
    return p1.returncode, output
  else:
    p1 = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    p2 = subprocess.Popen(pipe_command, stdin=p1.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    p1.stdout.close()
    output = p2.communicate()[0]
    if not (sys.version_info[0] == 2):
      output = output.decode(encoding='UTF-8')
  return p2.returncode, output

def run_and_get_stdout_v2(command, pipe_command=None):
  if type(command)==list:
    prg=command[0].strip().split(' ')[0]
  else:
    prg=command.strip().split(' ')[0]
  if program_in_paths(prg):
    import subprocess,sys
    if not pipe_command:
      p1 = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
      output = p1.communicate()[0]
      if not (sys.version_info[0] == 2):
        output = output.decode(encoding='UTF-8')
      return p1.returncode, output
    else:
      p1 = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
      p2 = subprocess.Popen(pipe_command, stdin=p1.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
      p1.stdout.close()
      output = p2.communicate()[0]
      if not (sys.version_info[0] == 2):
        output = output.decode(encoding='UTF-8')
    return p2.returncode, output
  else:
    return -1,None

def getSystem():
  import platform
  return platform.system().lower()

def isWindows():
  return getSystem() == 'windows'

def isMAC():
  return getSystem() == 'darwin'

def isLinux():
  return getSystem() == 'linux'

def getComputerName():
  import socket
  return socket.gethostname().lower()

def getUserName():
  import os
  return os.getlogin()
  
def getSoftware():
  import sys
  Release=sys.version.split(' ')[0]  
  Software='Python'
  return [Software,Release]

# Only Windows
def has_wmic(): 
  return program_in_paths('wmic.exe')
  #return len(program_paths('wmic')) > 0

# Only MAC
def has_sw_vers():
  return program_in_paths('sw_vers')
  #return len(program_paths('sw_vers')) > 0

def has_system_profiler():
  return program_in_paths('system_profiler')
  #return len(program_paths('system_profiler')) > 0

def has_sysctl():
  return program_in_paths('sysctl')
  #return len(program_paths('sysctl')) > 0

def has_lscpu():
  return program_in_paths('lscpu')
  #return len(program_paths('lscpu')) > 0

def has_lsb_release():
  return program_in_paths('lsb_release')
  #return len(program_paths('lsb_release')) > 0

def has_uname():
  return program_in_paths('uname')
  #return len(program_paths('uname')) > 0

def has_os_release():
  return os.path.exists('/etc/os-release')

def has_cpuinfo():
  return os.path.exists('/proc/cpuinfo')

def has_meminfo():
  return os.path.exists('/proc/meminfo')

def cat_os_release():
  return run_and_get_stdout(['cat', '/etc/os-release'])

def getArch():
  if isLinux():
    return getArch_Linux()
  if isWindows():
    return getArch_Windows()
  if isMAC():
    return getArch_MAC()
  return 'Unknow'

def getOSinfo():
  if isLinux():
    return getOSinfo_Linux()
  if isWindows():
    return getOSinfo_Windows()
  if isMAC():
    return getOSinfo_MAC()
  return {'distributor':getSystem(),'description':'Unknow','release':'Unknow','codename':'Unknow'}

def find_key_value(key,delimiter,Lines):
  for line in Lines:
    S=line.split(delimiter)
    if len(S)==2 and S[0].strip()==key:
      return S[1]
  return 'Unknow'

def strclean(s):
  if s[0]=='"' and s[-1]=='"':
    return s[1:-1]
  return s.strip()

def getArch():
  if isLinux() or isMAC():
    return getArch_Unix()
  if isWindows():
    return getArch_Windows()
  return 'Unknow'
  
def getArch_Unix(): 
  if has_uname():
    res,out=run_and_get_stdout(["uname", "-m"])
    return out.strip()
  return 'Unknow'

def getArch_Windows():  
  if has_wmic():
    res,out=run_and_get_stdout(["wmic", "os","get", "/value"])
    Lines=out.splitlines()
    return strclean(find_key_value('OSArchitecture','=',Lines))
  return 'Unknow'

def getOSinfo_Linux():
  arch=getArch_Unix()
  if has_lsb_release():
    res,out=run_and_get_stdout(["lsb_release", "-i","-s"])
    distributor=out.strip()
    res,out=run_and_get_stdout(["lsb_release", "-r","-s"])
    release=out.strip()
    res,out=run_and_get_stdout(["lsb_release", "-c","-s"])
    codename=out.strip()
    res,out=run_and_get_stdout(["lsb_release", "-d","-s"])
    description=out.strip()
    shortname=distributor
    return {'distributor': distributor,'description':description,'release':release,'codename':codename,
            'shortname':shortname,'arch':arch}
  if has_os_release():
    res,out=cat_os_release()
    Lines=out.splitlines()
    distributor=strclean(find_key_value('ID','=',Lines))
    description=strclean(find_key_value('PRETTY_NAME','=',Lines))
    release=strclean(find_key_value('VERSION_ID','=',Lines))
    codename=strclean(find_key_value('VERSION_CODENAME','=',Lines))
    shortname=distributor
    return {'distributor': distributor,'description':description,'release':release,'codename':codename,
            'shortname':shortname,'arch':arch}
  distributor=getSystem()
  return {'distributor':distributor,'description':'Unknow','release':'Unknow','codename':'Unknow',
          'shortname':shortname,'arch':arch}

def getOSinfo_Windows():
  arch=getArch_Windows()
  if has_wmic():
    res,out=run_and_get_stdout(["wmic", "os","get", "/value"])
    Lines=out.splitlines()
    distributor=strclean(find_key_value('Manufacturer','=',Lines))
    description=strclean(find_key_value('Caption','=',Lines))
    release=strclean(find_key_value('Version','=',Lines))
    codename=strclean(find_key_value('BuildNumber','=',Lines))
    shortname='Windows'
    return {'distributor': distributor,'description':description,'release':release,'codename':codename,
            'shortname':shortname,'arch':arch}
  return {'distributor':getSystem(),'description':'Unknow','release':'Unknow','codename':'Unknow',
          'shortname':shortname,'arch':arch}

def getOSinfo_MAC():
  arch=getArch_Unix()
  if has_sw_vers():
    res,out=run_and_get_stdout(["sw_vers"])
    Lines=out.splitlines()
    distributor='Apple Inc.'
    description=strclean(find_key_value('ProductName',':',Lines))
    release=strclean(find_key_value('BuildVersion',':',Lines))
    codename=strclean(find_key_value('ProductVersion',':',Lines)).strip()
    shortname='macOS'
    return {'distributor': distributor,'description':description.strip(),'release':release.strip(),'codename':codename.strip(),
            'shortname':shortname,'arch':arch}
  return {'distributor':getSystem(),'description':'Unknow','release':'Unknow','codename':'Unknow',
          'shortname':shortname,'arch':arch}

def getRAM():
  " getRAM returns the RAM in Go of the machine"
  if isLinux():
    return getRAM_Linux()
  if isMAC():
    return getRAM_MAC()
  if isWindows():
    return getRAM_Windows()
  return 'Unknow'
  
def getRAM_Linux(): 
  if has_meminfo():
    res,out=run_and_get_stdout(["grep", "MemTotal:","/proc/meminfo"])
    #out='MemTotal:       65630144 kB\n'
    S=out.split(':')[1].strip() # '65630144 kB'
    ram=eval(S.split(' ')[0])/(1024**2)
    return ram
  return '???'

def getRAM_MAC(): 
  if has_sysctl():
    res,out=run_and_get_stdout(["sysctl", "-n","hw.memsize"])
    ram=eval(out.strip())/(1024**3)
    return ram
  return '???'

def getRAM_Windows():  
  if has_wmic():
    res,out=run_and_get_stdout(["wmic", "ComputerSystem","get", "TotalPhysicalMemory","/value"])
    Lines=out.splitlines()
    ram=eval(strclean(find_key_value('TotalPhysicalMemory','=',Lines)))/(1024**3)
    return ram
  return '???'

def getCPUinfo():
  if isLinux():
    return getCPUinfo_Linux()
  if isMAC():
    return getCPUinfo_MAC()
  if isWindows():
    return getCPUinfo_Windows()
  return 'Unknow'

def getCPUinfo_Linux_full():
  #import numpy as np
  if has_cpuinfo():
    res,out=run_and_get_stdout(["grep", "cpu cores", "/proc/cpuinfo"])
    Scpucores=out.splitlines()
    cores=eval(Scpucores[0].split(':')[1])
    res,out=run_and_get_stdout(["grep", "model name", "/proc/cpuinfo"])
    Smodelname=out.splitlines()
    res,out=run_and_get_stdout(["grep", "core id", "/proc/cpuinfo"])
    Scoreid=out.splitlines()
    res,out=run_and_get_stdout(["grep", "physical id", "/proc/cpuinfo"])
    Sphysicalid=out.splitlines()
    N=len(Sphysicalid)
    Lname=N*[None]
    Aphysicalid=N*[None]
    Acoreid=N*[None]
    Acpucores=N*[None]
    #Aphysicalid=np.zeros((N,))
    #Acoreid=np.zeros((N,))
    #Acpucores=np.zeros((N,))
    for i in range(N):
      Aphysicalid[i]=eval(Sphysicalid[i].split(':')[1].strip())
      Acoreid[i]=eval(Scoreid[i].split(':')[1].strip())
      Acpucores[i]=eval(Scpucores[i].split(':')[1].strip())
      Lname[i]=Smodelname[i].split(':')[1].strip()
    #return (Lname,Aphysicalid,Acoreid,Acpucores)
  
    #pids=np.unique(Aphysicalid)
    pids=list(set(Aphysicalid))
    npids=len(pids)
    
    CPUS=[None]*npids
    for i in range(npids):
      idx=Aphysicalid.index(pids[i])
      ncoreperproc=int(Acpucores[idx])
      nidx=Aphysicalid.count(pids[i])
      nthreadspercore=int(nidx/ncoreperproc)
      #nthreadspercore=int(len(idx)/ncoreperproc)
      #idx=Aphysicalid==pids[i]
      #ncoreperproc=int(Acpucores[idx][0])
      #nthreadspercore=int(len(idx)/ncoreperproc)
      #CPUS[i]={'name': Lname[idx[0]] , 'ncoreperproc':ncoreperproc, 'nthreadspercore':nthreadspercore,
               #'socket':pids[i]}
      CPUS[i]={'name': Lname[idx] , 'ncoreperproc':ncoreperproc, 'nthreadspercore':nthreadspercore,
               'socket':pids[i]}         
    return CPUS
  return None

def getCPUinfo_Linux():
  CPUS=getCPUinfo_Linux_full()
  if CPUS is not None:
    return {'name'           : CPUS[0]['name'],
            'ncoreperproc'   :CPUS[0]['ncoreperproc'],
            'nthreadspercore':CPUS[0]['nthreadspercore'],
            'nprocs':len(CPUS)}
  return None

def getCPUinfo_Windows():
  if has_wmic():
    res,out=run_and_get_stdout(["wmic", "cpu","get", "/value"])
    Lines=out.splitlines()
    name=strclean(find_key_value('Name','=',Lines))
    
    ncoreperproc=int(eval(find_key_value('NumberOfCores','=',Lines)))
    NumberOfLogicalProcessors=int(eval(strclean(find_key_value('NumberOfLogicalProcessors','=',Lines))))
    nthreadspercore=int(NumberOfLogicalProcessors/ncoreperproc)
    
    res,out=run_and_get_stdout(["wmic", "computersystem","get","numberofprocessors", "/value"])
    Lines=out.splitlines()
    nprocs=int(eval(find_key_value('NumberOfProcessors','=',Lines)))
    return {'name': name,'ncoreperproc':ncoreperproc,'nthreadspercore':nthreadspercore,'nprocs':nprocs}
  #return {'name': '???','ncoreperproc':'???','nthreadspercore':'???','nprocs':'???'}
  return None

def getCPUinfo_MAC():
  if has_sysctl():
    res,out=run_and_get_stdout(["sysctl","-a", "machdep.cpu.brand_string"])
    name=out.split(':')[1].strip()
    
    res,out=run_and_get_stdout(["sysctl","hw"])
    Lines=out.splitlines()
    ncoreperproc=int(eval(find_key_value('hw.physicalcpu',':',Lines)))
    NumberOfLogicalProcessors=int(eval(strclean(find_key_value('hw.logicalcpu',':',Lines))))
    nthreadspercore=int(NumberOfLogicalProcessors/ncoreperproc)
    
    nprocs=0
    if has_system_profiler():
      res,out=run_and_get_stdout(["system_profiler","SPHardwareDataType"])
      Lines=out.splitlines()
      nprocs=int(eval(strclean(find_key_value('Number of Processors',':',Lines))))
    
    return {'name': name,'ncoreperproc':ncoreperproc,'nthreadspercore':nthreadspercore,'nprocs':nprocs}
  return None

def getGitCurrentCommit():
  proc = subprocess.Popen(["git","log"],stdout=subprocess.PIPE)
  out, err = proc.communicate()
  Out=str(out)
  Out1=Out[Out.find('commit'):Out.find('\n')]
  return Out1.split('\\n')[0] # or '\\n'
  
def getGitCurrentBranch():
  out=subprocess.Popen("git -c color.branch=false  branch", shell=True, stdout=subprocess.PIPE).stdout.read()
  Out=str(out)
  return Out[Out.find('*'):Out.find('\\n')]

def getGitRemoteURL():
  out=subprocess.Popen("git config --get remote.origin.url", shell=True, stdout=subprocess.PIPE).stdout.read()
  Out=out.decode("utf-8")
  return Out[:Out.find('\n')] 

class CD:
  """Context manager for changing the current working directory
  
      with CD('/tmp'):
        ...
        
      https://stackoverflow.com/questions/431684/how-do-i-cd-in-python
  """
  def __init__(self, newPath):
      self.newPath = os.path.expanduser(newPath)

  def __enter__(self):
      self.savedPath = os.getcwd()
      os.chdir(self.newPath)

  def __exit__(self, etype, value, traceback):
      os.chdir(self.savedPath)

from contextlib import contextmanager
import os

@contextmanager
def cd(newdir):
  """
    with cd('/tmp'):
     ...
     
    https://stackoverflow.com/questions/431684/how-do-i-cd-in-python/24176022#24176022
  """ 
  prevdir = os.getcwd()
  os.chdir(os.path.expanduser(newdir))
  try:
      yield
  finally:
      os.chdir(prevdir)
      
def cdrun_and_get_stdout(command,rep=None):
  # return status,output
  #command=['git', 'rev-parse', 'HEAD']
  if rep is not None:
    with cd(rep):
      return run_and_get_stdout(command)
  else:
    return run_and_get_stdout(command)
  
        
