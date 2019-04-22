import numpy as np
#import sys,os

#from .others import isModuleFound
##def isMatplotlib():  
  ##isOk=True
  ##try:
    ##import matplotlib
  ##except ImportError:
    ##isOk=False
  ##return isOk

##if isMatplotlib(): 
#if isModuleFound('matplotlib'):
  #from fc_tools.Matplotlib import set_axes,set_axes_equal,DisplayFigures,SetGeometry,SaveAllFigsAsFiles

##def isMayavi():  
  ##ismayavi=True
  ##try:
    ##import vtk
    ##import tvtk
    ##import mayavi
  ##except ImportError:
    ##ismayavi=False
  ##return ismayavi

##if isMayavi():
#if isModuleFound('mayavi'):
  #from fc_tools.Mayavi import vtk_SaveAllFigsAsFiles
    
def check_3Dvec(point):
  if isinstance(point,list):
    point=np.array(point)  
  assert(isinstance(point,np.ndarray))
  assert( point.shape == (3,) )
  return point
  
  
class Plane:    
  def __init__(self,origin=[0,0,0],normal=[1,0,0]):
    self.origin=check_3Dvec(origin)
    self.normal_in=check_3Dvec(normal)
    self.normal=self.normal_in/np.sqrt(np.sum(self.normal_in**2))
    
  def Coefs(self):
    return np.hstack((self.normal,-np.dot(self.origin,self.normal)))