Include "options01_data.geo";
//N=1;
R=1;
//N=10;
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
Line Loop(9) = {8, -3, 5};
Ruled Surface(1) = {9};
Line Loop(11) = {4, -6, 8};
Ruled Surface(2) = {11};
Line Loop(13) = {6, 1, 7};
Ruled Surface(3) = {13};
Line Loop(15) = {7, -5, -2};
Ruled Surface(4) = {15};

Physical Line(5) = {5};
Physical Line(8) = {8};
Physical Line(6) = {6};
Physical Line(7) = {7};
Physical Line(4) = {4};
Physical Line(1) = {1};
Physical Line(2) = {2};
Physical Line(3) = {3};

Physical Surface(1) = {1};
Physical Surface(2) = {2};
Physical Surface(3) = {3};
Physical Surface(4) = {4};
