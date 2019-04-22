import os
from fc_tools.Sys import cdrun_and_get_stdout,run_and_get_stdout,isWindows,which

gitcmd=None
if isWindows():
  GIT=which('git.exe')
  if GIT is not None:	
    gitcmd='git.exe'
  else:  # Check if Windows Subsystem for Linux (WSL) is installed with git command in path
    WSL=which('wsl.exe')
    if WSL is not None:
      status,res=run_and_get_stdout('wsl.exe which git'.split(' '))
      if status==0:
         gitcmd='wsl.exe git'  
else:
  gitcmd='git'
  
def get_gitversion():  
  if gitcmd is None:
    return ''
  command=gitcmd+' --version'
  status,out=run_and_get_stdout(command.split(' '))
  if status==0:
    return out.strip()
  else:
    return ''  
  
def gitinfo():
  return {'name': 'fc-tools', 'tag': '0.0.21', 'commit': 'fb96440da285bb7128ed75c6536265f712b81029', 'date': '2019-03-27', 'time': '10-52-45', 'status': '0'} # automatically updated
  if len(inf)>0: # Only for developpers
    return inf
  import fc_tools,os
  D=os.path.realpath(os.path.join(fc_tools.__path__[0],os.path.pardir))
  if os.path.basename(D)=='src':
    D=os.path.realpath(os.path.join(D,os.path.pardir))
  return fc_tools.git.get_info(D)

def isrepository(rep=None):
  assert (rep is None) or (type(rep) is str)
  if rep is None:
    return os.path.isdir('.git')
  else:
    return os.path.isdir(rep+os.path.sep+'.git')
     


def get_commit(rep=None):
  if gitcmd is None:
    return ''
  command=gitcmd+' rev-parse HEAD'
  status,out=cdrun_and_get_stdout(command.split(' '),rep)
  if status==0:
    return out.strip()
  else:
    return ''
  
def get_remotecommit(remote):
  if gitcmd is None:
    return ''
  command=gticmd+' ls-remote %s | grep HEAD'%remote
  status,out=run_and_get_stdout(command.split(' '))
  if status==0:
    return out.strip()
  else:
    return ''
  
def get_rawdate(rep=None):
  if gitcmd is None:
    return ''
  command=gitcmd+' log -1 --pretty="%at"'
  status,out=cdrun_and_get_stdout(command.split(' '),rep)
  if status==0:
    t=int(out.strip().replace('"',''))
    return t
  else:
    return ''  
  
def get_date(rep=None):
  if gitcmd is None:
    return ''
  command=gitcmd+' log -1 --pretty="%at"'
  status,out=cdrun_and_get_stdout(command.split(' '),rep)
  if status==0:
    from time import localtime, strftime
    t=int(out.strip().replace('"',''))
    return strftime('%Y-%m-%d',localtime(t))
  else:
    return ''
  
def get_time(rep=None):
  if gitcmd is None:
    return ''
  command=gitcmd+' log -1 --pretty="%at"'
  status,out=cdrun_and_get_stdout(command.split(' '),rep)
  if status==0:
    from time import localtime, strftime
    t=int(out.strip().replace('"',''))
    return strftime('%H-%M-%S',localtime(t))
  else:
    return ''

def get_name(rep=None):
  url=get_url(rep)
  return url.split('/')[-1]
  
def get_url(rep=None):
  if gitcmd is None:
    return ''
  command=gitcmd+' config --get remote.origin.url'
  status,out=cdrun_and_get_stdout(command.split(' '),rep)
  if status==0:
    return out.strip()
  else:
    return ''
  
def isup2date(rep=None):
  if gitcmd is None:
    return ''
  command=gitcmd+' ls-files -m'
  status,out=cdrun_and_get_stdout(command.split(' '),rep)
  if status==0:
    #print(out)
    return len(out)==0
  else:
    return ''
  
def get_tag(rep=None):
  if gitcmd is None:
    return ''
  command=gitcmd+' log -1 --pretty="format:%d"'
  status,out=cdrun_and_get_stdout(command.split(' '),rep)
  if status==0:
    I=out.find('tag:')
    if I==-1:
      return ''
    else:
      return out[I+4::].split(')')[0].split(',')[0].strip()
  else:
    return ''
  
  
def get_exacttag(rep=None):
  if gitcmd is None:
    return ''
  command=gitcmd+' describe --tags --exact-match'
  status,out=cdrun_and_get_stdout(command.split(' '),rep)
  if status==0:
    return out.strip()
  else:
    return ''
  
def get_tags(rep=None):
  if gitcmd is None:
    return ''
  command=gitcmd+' tag'
  status,out=cdrun_and_get_stdout(command.split(' '),rep)
  if status==0:
    return out.strip()
  else:
    return ''  
  
def get_tagsinfo(rep=None):  
  if gitcmd is None:
    return ''
  command=gitcmd+' for-each-ref --format ''%(tag)|%(objectname)|%(taggerdate:raw)'' refs/tags  --sort=taggerdate | awk ''BEGIN{FS="|"};{t=strftime("%Y-%m-%d|%H:%M:%S",$3);printf"%s|%s|%s\n",$1,$2,t}'''  
  status,out=cdrun_and_get_stdout(command.split(' '),rep)
  if status==0:
    return out.strip()
  else:
    return ''  
  
def get_info(rep=None):
  if isrepository(rep):
    return {'name':get_name(rep),
            'tag' :get_tag(rep),
            'commit':get_commit(rep),
            'date':get_date(rep),
            'time':get_time(rep),
            'status':isup2date(rep)}
  else:
    return {'name':'',
            'tag' :'',
            'commit':'',
            'date':'',
            'time':'',
            'status':''}
  
def print_info(rep=None):
  if type(rep) is dict:
    D=rep
  else:
    D=get_info(rep)
  for k, v in D.items():
    print('{:>10}: {}'.format(k, v))
  
