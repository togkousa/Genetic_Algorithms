// Include "options01_data.geo";
Include "partitions01_data.geo";
Include "partitions_shape.geo";

h=1/N;
Lx=LX;Ly=LY;Nx=NX;Ny=NY;pM[]={};
Call PartitionPoints;

vL[]={}; // labels of vertical lines
hL[]={}; // labels of horizontal lines 
pS[]={}; // labels of plane surfaces
Call PartitionLinesAndSurfaces;

hpL[]={}; // labels of horizontal physical lines
vpL[]={}; // labels of vertical physical lines

Call PhysicalLines;
Call PhysicalSurfaces;

