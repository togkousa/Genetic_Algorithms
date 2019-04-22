Function CreateCircle
  // Center Points of circle (cx,cy) with radius r 
  // PhysLab is the physical label of the boundary
  // CenterLab 
  // h
  If( CenterLab < 0 )
    PFC = newp; Point(PFC) = {cx, cy, 0, h};
    Centerstore[]={Centerstore[],PFC};
  Else
    PFC = CenterLab;
  EndIf
  PF1 = newp;Point(PF1) = {cx+r, cy, 0, h};
  PF2 = newp;Point(PF2) = {cx,cy+r, 0, h};
  PF3 = newp;Point(PF3) = {cx-r, cy, 0, h};
  PF4 = newp;Point(PF4) = {cx,cy-r, 0, h};
  PC1 = newreg;Circle(PC1) = {PF1, PFC, PF2};
  PC2 = newreg;Circle(PC2) = {PF2, PFC, PF3};
  PC3 = newreg;Circle(PC3) = {PF3, PFC, PF4};
  PC4 = newreg;Circle(PC4) = {PF4, PFC, PF1};
  Line Loop(PhysLab) = {PC1, PC2, PC3, PC4};
  Coherence;
  Physical Line(PhysLab) = {PC1, PC2, PC3, PC4};
  PS = newreg;
  Plane Surface(PS) = {PhysLab};
  PSstore[]={PSstore[],PS};
  If( isPhysical == 1 )
    Physical Surface(PhysLab) = {PS};
  EndIf
Return

Function CreateRectangle
  // Points Bottom-left (BLx,BLy) and Top-right (TRx,TRy) 
  // PhysLab is the physical label of the boundary
  // h
  PF1 = newp; Point(PF1) = {BLx, BLy, 0, h}; 
  PF2 = newp; Point(PF2) = {TRx, BLy, 0, h};
  PF3 = newp; Point(PF3) = {TRx, TRy, 0, h};
  PF4 = newp; Point(PF4) = {BLx, TRy, 0, h};
  PL1 = newreg; Line(PL1) = {PF1, PF2};
  PL2 = newreg; Line(PL2) = {PF2, PF3};
  PL3 = newreg; Line(PL3) = {PF3, PF4};
  PL4 = newreg; Line(PL4) = {PF4, PF1};
  Line Loop(PhysLab) = {PL1,PL2,PL3,PL4};
  Physical Line(PhysLab) = {PL1,PL2,PL3,PL4};
  PS = newreg;Plane Surface(PS) = {PhysLab};
  PSstore[]={PSstore[],PS};
  If(isPhysical == 1)
    Physical Surface(PhysLab) = {PS};
  EndIf
Return

Function CreateRectangle4Bounds
  // Points Bottom-left (BLx,BLy) and Top-right (TRx,TRy) 
  // PhysLab+1 is the physical label of the boundary x==BLx
  // PhysLab+2 is the physical label of the boundary x==TRx
  // PhysLab+3 is the physical label of the boundary y==BLy
  // PhysLab+4 is the physical label of the boundary y==TRy
  // h
  PF1 = newp; Point(PF1) = {BLx, BLy, 0, h}; 
  PF2 = newp; Point(PF2) = {TRx, BLy, 0, h};
  PF3 = newp; Point(PF3) = {TRx, TRy, 0, h};
  PF4 = newp; Point(PF4) = {BLx, TRy, 0, h};
  Line(PhysLab+3) = {PF1, PF2};
  Line(PhysLab+2) = {PF2, PF3};
  Line(PhysLab+4) = {PF3, PF4};
  Line(PhysLab+1) = {PF4, PF1};
  Line Loop(PhysLab+1) = {PhysLab+1};
  Line Loop(PhysLab+2) = {PhysLab+2};
  Line Loop(PhysLab+3) = {PhysLab+3};
  Line Loop(PhysLab+4) = {PhysLab+4};
  Physical Line(PhysLab+1) = {PhysLab+1};
  Physical Line(PhysLab+2) = {PhysLab+2};
  Physical Line(PhysLab+3) = {PhysLab+3};
  Physical Line(PhysLab+4) = {PhysLab+4};
  PS = newreg;Plane Surface(PS) = {PhysLab+1,PhysLab+2,PhysLab+3,PhysLab+4};
  PSstore[]={PSstore[],PS};
  If(isPhysical == 1)
    Physical Surface(PhysLab) = {PS};
  EndIf
Return
