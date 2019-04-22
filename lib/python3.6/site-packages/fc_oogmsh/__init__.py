# Copyright (C) 2018 F. Cuvelier
# License: GNU GPL version 3
__version__='<fc-bench>'
from .demos import *
from .Sys import configure,printenv,gitinfo
from .gmsh import ooGmsh,isooGmsh,buildmesh,buildmesh2d,buildmesh3d,buildmesh3ds,buildpartmesh,buildpartrectangle
