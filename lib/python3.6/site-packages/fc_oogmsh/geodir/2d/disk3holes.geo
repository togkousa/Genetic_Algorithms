// In FreeFEM, meshes.idp : FlowVelocity2d01Mesh
Include "options01_data.geo";
h = 1/N;
R=1.;
r=0.3;
r1=0.1;
c=0.7;
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
Plane Surface(1) = {11, 12, 13, 14};
Physical Line(10) = {6, 5};
Physical Line(21) = {2, 1};
Physical Line(20) = {4, 3};
Physical Line(1) = {7};
Physical Line(2) = {8};
Physical Line(3) = {9};
Physical Line(4) = {10};
Physical Surface(1) = {1};
