DefineConstant[
  N = {10, Name "Input/1Points "}
];
L=1;
h=L/N; 
Point (1) = {0, 0, 0, h};
Point (2) = {L, 0, 0, h};
Point (3) = {L, L, 0, h};
Point (4) = {0, L, 0, h};
Line (3)  = {1, 2};
Line (2)  = {2, 3};
Line (4)  = {3, 4};
Line (1)  = {4, 1};
Line Loop (100) = { 1,   2,   3,   4};
Plane Surface (1) = {100};
Physical Line(1) = {1};
Physical Line(2) = {2};
Physical Line(3) = {3};
Physical Line(4) = {4};
Physical Surface(1) = {1};
Physical Point(101) = {1};
Physical Point(102) = {2};
Physical Point(103) = {3};
Physical Point(104) = {4};
