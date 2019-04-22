// In FreeFEM, meshes.idp : FlowVelocity2d01Mesh
Include "options01_data.geo";
h = 1/N;
R=1.;
r=0.3;
r1=0.1;
c=0.7;
// Center Points of circle
Point(1) = {0, 0, 0, h}; 
Point(2) = {c, 0, 0, h};
Point(3) = {-c, 0, 0, h};
Point(4) = {0,c, 0, h};
Point(5) = {0,-c, 0, h};
// Points on circles
Point(10) = {1, 0, 0, h};
Point(11) = {-1, 0, 0, h}; 
Point(12) = {c+r1, 0, 0, h};
Point(13) = {c-r1, 0, 0, h}; 
Point(14) = {-c+r1, 0, 0, h};
Point(15) = {-c-r1, 0, 0, h}; 
Point(16) = {0,c+r1, 0, h};
Point(17) = {0,c-r1, 0, h}; 
Point(18) = {0,-c+r1, 0, h};
Point(19) = {0,-c-r1, 0, h}; 
Point(20) = {r,0, 0, h};
Point(21) = {-r,0, 0, h}; 


Circle(1) = {10, 1, 11};
Circle(2) = {11, 1, 10};
Circle(3) = {20, 1, 21};
Circle(4) = {21, 1, 20};
Circle(5) = {16, 4, 17};
Circle(6) = {17, 4, 16};
Circle(7) = {14, 3, 15};
Circle(8) = {15, 3, 14};
Circle(9) = {13, 2, 12};
Circle(10) = {12, 2, 13};
Line Loop(11) = {1, 2};
Line Loop(12) = {5, 6};
Circle(13) = {18, 5, 19};
Circle(14) = {19, 5, 18};
Line Loop(15) = {7, 8};
Line Loop(16) = {3, 4};
Line Loop(17) = {10, 9};
Line Loop(18) = {14, 13};
Plane Surface(19) = {11, 12, 15, 16, 17, 18};
Physical Surface(1) = {19};
Physical Line(1) = {1, 2};
Physical Line(22) = {7, 8};
Physical Line(21) = {5, 6};
Physical Line(23) = {10, 9};
Physical Line(10) = {3, 4};
Physical Line(20) = {13, 14};
