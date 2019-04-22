""" ====================
    fc_hypermesh package
    ====================
    
    The fc_hypermesh package contains a simple class object `OrthMesh` which 
    permits, in any dimension d>=1 to obtain a simplicial mesh or orthotope mesh 
    with all their m-faces, 0<=m<d,$ of a d-orthotope. If the `Matplotlib` package
    is installed, it is also possible with the `plotmesh` method of the class 
    object `OrthMesh` to represent a mesh or its m-faces for d<=3.
    
    ==================== =========================================================
    Objects
    ==============================================================================
    OrthMesh             Contain a main mesh of a d-orthotope and all its m-faces. 
                         See `OrthMesh` help.
    EltMesh              Elementary mesh (low level class).
                         See `EltMesh` help.
                         
    ==================== =========================================================
    Demo functions
    ==============================================================================
    See `demos` help
    
    ==================== =========================================================
    Benchmark functions
    ==============================================================================
    See `benchs` help
    
    Algorithms used in `fc_hypermesh` package are described in the report 
      'Vectorized algorithms for regular tessellations of d-orthotopes and 
       their faces' 
    by F. Cuvelier and available at http:\\...
    
    :author:     F. Cuvelier
    :email:      cuvelier@math.univ-paris13.fr
    :copyright:  (c) 2017
    :license:    GNU General Public License.
"""
__version__ = '0.0.12'
from fc_hypermesh.OrthMesh import OrthMesh
from fc_hypermesh.benchs import bench01
from fc_hypermesh import demos

