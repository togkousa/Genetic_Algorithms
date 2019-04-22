//N=1;
R=1;
N=10;
h=R/N;
// h=5;
// R=5;
// 2/ Points :

Point(1) = {0,0,0,h};
Point(2) = {R,0,0,h};
Point(3) = {0,R,0,h};
Point(4) = {0,0,R,h};
Point(5) = {-R,0,0,h};
Point(6) = {0,-R,0,h};

// 3/ Arcs :


Circle(1) = {2,1,3};
Circle(2) = {3,1,5};
Circle(3) = {5,1,6};
Circle(4) = {6,1,2};
Circle(5) = {5,1,4};
Circle(6) = {4,1,2};
Circle(7) = {3,1,4};
Circle(8) ={4,1,6};


// 4/ Contours :
Line Loop(9) = {2, 3, 4, 1};
Plane Surface(1) = {9};
Line Loop(12) = {6, -4, -8};
Ruled Surface(10) = {12};
Line Loop(14) = {1, 7, 6};
Ruled Surface(11) = {14};
Line Loop(16) = {7, -5, -2};
Ruled Surface(12) = {16};
Line Loop(18) = {3, -8, -5};
Ruled Surface(13) = {18};


Physical Surface(1) = {1};
Physical Surface(10) = {10};
Physical Surface(11) = {11};
Physical Surface(12) = {12};
Physical Surface(13) = {13};
Physical Line(7) = {7};
Physical Line(6) = {6};
Physical Line(8) = {8};
Physical Line(5) = {5};
Physical Line(2) = {2};
Physical Line(3) = {3};
Physical Line(4) = {4};
Physical Line(1) = {1};
Physical Point(10) = {2};
Physical Point(11) = {3};
Physical Point(12) = {5};
Physical Point(13) = {6};
Physical Point(1) = {4};
