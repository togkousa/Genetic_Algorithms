Include "options01_data.geo";
R=1;

h=R/Sqrt(17*N);
// h=5;
// R=5;
// 2/ Points :

Point(1) = {0,0,0,h};
Point(2) = {R,0,0,h};
Point(3) = {0,R,0,h};
Point(4) = {0,0,R,h};
Point(5) = {-R,0,0,h};

Line(1) = {1, 2};
Line(2) = {1, 3};
Line(3) = {1, 4};
Line(4) = {1, 5};
Circle(5) = {2, 1, 3};
Circle(6) = {3, 1, 5};
Circle(7) = {3, 1, 4};
Circle(8) = {2, 1, 4};
Circle(9) = {4, 1, 5};
Line Loop(10) = {1, 8, -3};
Plane Surface(11) = {10};
Line Loop(12) = {3, 9, -4};
Plane Surface(13) = {12};
Line Loop(14) = {2, 7, -3};
Plane Surface(15) = {14};
Line Loop(16) = {7, -8, 5};
Ruled Surface(17) = {16};
Line Loop(18) = {9, -6, 7};
Ruled Surface(19) = {18};
Line Loop(20) = {2, -5, -1};
Plane Surface(21) = {20};
Line Loop(22) = {6, -4, 2};
Plane Surface(23) = {22};
Surface Loop(24) = {23, 19, 13, 15};
Volume(25) = {24};
Surface Loop(26) = {17, 11, 21, 15};
Volume(27) = {26};


Physical Line(1) = {1};
Physical Line(2) = {4};
Physical Line(3) = {3};
Physical Line(4) = {2};
Physical Line(5) = {8};
Physical Line(6) = {9};
Physical Line(7) = {6};
Physical Line(8) = {7};
Physical Line(9) = {5};

Physical Surface(1) = {11};
Physical Surface(2) = {13};
Physical Surface(3) = {15};
Physical Surface(4) = {21};
Physical Surface(5) = {23};
Physical Surface(6) = {19};
Physical Surface(7) = {17};
Physical Volume(1) = {25};
Physical Volume(2) = {27};
