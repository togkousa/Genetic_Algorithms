Include "options01_data.geo";
h = 1/N;
R=1.;
r=0.3;
r1=0.1;
c=0.7;
H=2.0;
// Center Points of circle
Point(1) = {0, 0, 0, h}; 
Point(4) = {0,c, 0, h};
Point(5) = {0,-c, 0, h};
// Points on circles
Point(10) = {R, 0, 0, h};
Point(11) = {-R, 0, 0, h};
Point(12) = {0,R, 0, h};
Point(13) = {0,-R, 0, h}; 
Point(16) = {0,c+r1, 0, h};
Point(17) = {0,c-r1, 0, h}; 
Point(18) = {0,-c+r1, 0, h};
Point(19) = {0,-c-r1, 0, h}; 
Point(20) = {r,0, 0, h};
Point(21) = {-r,0, 0, h}; 

// Center Points of circle
Point(101) = {0, 0, H, h}; 
Point(104) = {0,c, H, h};
Point(105) = {0,-c, H, h};
// Points on circles
Point(100) = {R, 0, H, h};
Point(111) = {-R, 0, H, h};
Point(112) = {0,R, H, h};
Point(113) = {0,-R, H, h}; 
Point(116) = {0,c+r1, H, h};
Point(117) = {0,c-r1, H, h}; 
Point(118) = {0,-c+r1, H, h};
Point(119) = {0,-c-r1, H, h}; 
Point(120) = {r,0, H, h};
Point(121) = {-r,0, H, h}; 



Circle(1) = {17, 4, 16};
Circle(2) = {16, 4, 17};
Circle(3) = {19, 5, 18};
Circle(4) = {18, 5, 19};
Circle(5) = {21, 1, 20};
Circle(6) = {20, 1, 21};

Circle(7) = {10, 1, 12};
Circle(8) = {12, 1, 11};
Circle(9) = {11, 1, 13};
Circle(10) = {13, 1, 10};
Line Loop(11) = {8, 9, 10, 7};
Line Loop(12) = {2, 1};
Line Loop(13) = {6, 5};
Line Loop(14) = {4, 3};


Circle(15) = {120, 101, 121};
Circle(16) = {121, 101, 120};
Circle(17) = {117, 104, 116};
Circle(18) = {116, 104, 117};
Circle(19) = {118, 105, 119};
Circle(20) = {119, 105, 118};
Circle(21) = {100, 101, 112};
Circle(22) = {112, 101, 111};
Circle(23) = {111, 101, 113};
Circle(24) = {113, 101, 100};
Line Loop(25) = {23, 24, 21, 22};
Line Loop(26) = {16, 15};
Line Loop(27) = {18, 17};
Line Loop(28) = {19, 20};
Plane Surface(29) = {25, 26, 27, 28};
Plane Surface(30) = {11, 12, 13, 14};
Line(31) = {111, 11};
Line(32) = {113, 13};
Line(33) = {100, 10};
Line(34) = {112, 12};
Line(35) = {116, 16};
Line(36) = {17, 117};
Line(37) = {121, 21};
Line(38) = {120, 20};
Line(39) = {118, 18};
Line(40) = {19, 119};

Line Loop(41) = {5, -38, -16, 37};
Line Loop(43) = {15, 37, -6, -38};
Line Loop(45) = {17, 35, -1, 36};
Line Loop(48) = {24, 33, -10, -32};
Line Loop(50) = {32, -9, -31, 23};
Line Loop(52) = {22, 31, -8, -34};
Line Loop(54) = {21, 34, -7, -33};
Line Loop(59) = {18, -36, -2, -35};
Line Loop(61) = {19, -40, -4, -39};
Line Loop(63) = {3, -39, -20, -40};

Ruled Surface(42) = {41};
Ruled Surface(44) = {43};
Ruled Surface(46) = {45};
// Ruled Surface(47) = {28};
Ruled Surface(49) = {48};
Ruled Surface(51) = {50};
Ruled Surface(53) = {52};
Ruled Surface(55) = {54};
// Ruled Surface(58) = {28};
Ruled Surface(60) = {59};
Ruled Surface(62) = {61};
Ruled Surface(64) = {63};

Physical Surface(1) = {49, 55, 53, 51};
Physical Surface(10) = {42, 44};

Surface Loop(77) = {51, 49, 29, 55, 53, 30, 46, 60, 42, 44, 64, 62};
Volume(1) = {77};

Physical Surface(20) = {60, 46};
Physical Surface(21) = {64, 62};
Physical Surface(100) = {29};
Physical Surface(101) = {30};

Physical Line(20) = {21, 24, 23, 22};
Physical Line(25) = {18, 17};
Physical Line(21) = {15, 16};
Physical Line(26) = {19, 20};
Physical Line(10) = {9, 10, 7, 8};
Physical Line(15) = {2, 1};
Physical Line(11) = {5, 6};
Physical Line(16) = {4, 3};

Physical Volume(1) = {1};
