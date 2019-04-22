

Function PartitionPoints
  // [0,Lx]x[0,Ly]
  // Nx+1 points along x axis
  // Ny+1 points along y axis
  hx=Lx/Nx;hy=Ly/Ny;
  For j In {1:(Ny+1)}
    For i In {1:(Nx+1)}
       pM[] += newp ; Point(newp) = { (i-1)*hx, (j-1)*hy, 0, h};
    EndFor
  EndFor
Return

Function PartitionLinesAndSurfaces
  // Horizontal lines
  For j In {0:Ny}
    pl=j*(Nx+1);// label of left point
    For i In {1:Nx}
      hL[] += newreg; Line(newreg) = {pM[pl],pM[pl+1]};
      pl++;
    EndFor
  EndFor
  // Vertical lines
  For j In {1:Ny}
    pb=(j-1)*(Nx+1);// label of bottom point
    For i In {0:Nx}
      vL[] += newreg; Line(newreg) = {pM[pb],pM[pb+(Nx+1)]};
      pb++;
    EndFor
  EndFor
  // Plane surfaces
  ih=0;iv=0;
  For j In {1:Ny}
    For i In {1:Nx}
      l1= newreg; Line Loop(l1) = {hL[ih], -hL[ih+Nx], -vL[iv], vL[iv+1]};
      pS[] += newreg;  Plane Surface(newreg) = {l1};
      ih++;iv++;
    EndFor
    iv++;
  EndFor
Return

// Don't save negative labels!
Function PhysicalLinesBug
  // Horizontal lines
  inter=-1; // interface label must be <0
  pl=0;
  // bottom lines
  lab=1000;
  For i In {1:Nx}
    Physical Line(lab) = {hL[pl]};
    hpL[pl]=lab;
    lab++;pl++;
  EndFor
  For j In {2:Ny}
    For i In {1:Nx}
      Physical Line(inter) = {hL[pl]};
      hpL[pl]=inter;
      inter--;pl++;
    EndFor
  EndFor
  // upper lines
  lab=2000;
  For i In {1:Nx}
    Physical Line(lab) = {hL[pl]};
    hpL[pl]=lab;
    lab++;pl++;
  EndFor
  //  vertical lines
  labl=3000;
  labr=4000;
  pl=0;
  For j In {1:Ny}
    Physical Line(labl) = {vL[pl]};
    vpL[pl]=labl;
    labl++;pl++;
    For i In {1:Nx-1}
      Physical Line(inter) = {vL[pl]};
      vpL[pl]=inter;
      inter--;pl++;
    EndFor
    Physical Line(labr) = {vL[pl]};
    vpL[pl]=labr;
    labr++;pl++;
  EndFor  
Return


Function PhysicalLines
  // Horizontal lines
  inter=10000; // interface label start 
  pl=0;
  // bottom lines
  lab=1000;
  For i In {1:Nx}
    Physical Line(lab) = {hL[pl]};
    hpL[pl]=lab;
    lab++;pl++;
  EndFor
  For j In {2:Ny}
    For i In {1:Nx}
      Physical Line(inter) = {hL[pl]};
      hpL[pl]=inter;
      inter++;pl++;
    EndFor
  EndFor
  // upper lines
  lab=2000;
  For i In {1:Nx}
    Physical Line(lab) = {hL[pl]};
    hpL[pl]=lab;
    lab++;pl++;
  EndFor
  //  vertical lines
  labl=3000;
  labr=4000;
  pl=0;
  For j In {1:Ny}
    Physical Line(labl) = {vL[pl]};
    vpL[pl]=labl;
    labl++;pl++;
    For i In {1:Nx-1}
      Physical Line(inter) = {vL[pl]};
      vpL[pl]=inter;
      inter++;pl++;
    EndFor
    Physical Line(labr) = {vL[pl]};
    vpL[pl]=labr;
    labr++;pl++;
  EndFor  
Return

Function PhysicalSurfaces
  // Plane surfaces
  idx=0;
  For j In {1:Ny}
    For i In {1:Nx}
      Physical Surface(idx+1) = {pS[idx]};
      idx++;
    EndFor
  EndFor
Return

  