import numpy
import sys,os,errno
import os.path as op
import subprocess

def getDataPath():
  fullname=op.dirname(op.abspath(__file__))
  #fulldir=fullname[:fullname.rfind(os.sep)]
  return fullname+os.sep+'data'