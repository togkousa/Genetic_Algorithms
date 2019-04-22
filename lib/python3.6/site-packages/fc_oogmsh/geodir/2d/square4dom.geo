Include "options01_data.geo";
h=1/N;
Point(1) = {0, 0, 0, h}; 
Point(2) = {1, 0, 0, h};
Point(3) = {1, 1, 0, h};
Point(4) = {0, 1, 0, h};

Point(10) = {1/2, 0, 0, h};
Point(11) = {1, 1/2, 0, h};
Point(12) = {1/2, 1, 0, h};
Point(13) = {0, 1/2, 0, h};    

Point(20) = {1/2, 1/2, 0, h};    Line(1) = {1, 10};
Line(2) = {10, 2};
Line(3) = {2, 11};
Line(4) = {11, 3};
Line(5) = {3, 12};
Line(6) = {12, 4};
Line(7) = {4, 13};
Line(8) = {13, 1};
Line(9) = {10, 20};
Line(10) = {20, 12};
Line(11) = {13, 20};
Line(12) = {20, 11};
Line Loop(13) = {8, 1, 9, -11};
Plane Surface(14) = {13};
Line Loop(15) = {2, 3, -12, -9};
Plane Surface(16) = {15};
Line Loop(17) = {12, 4, 5, -10};
Plane Surface(18) = {17};
Line Loop(19) = {11, 10, 6, 7};
Plane Surface(20) = {19};
// Bords physiques
Physical Line(1) = {1};
Physical Line(2) = {2};
Physical Line(3) = {3};
Physical Line(4) = {4};
Physical Line(5) = {5};
Physical Line(6) = {6};
Physical Line(7) = {7};
Physical Line(8) = {8};
// Interfaces
Physical Line(1001) = {9};
Physical Line(1002) = {12};
Physical Line(1003) = {10};
Physical Line(1004) = {11};
// Partitions
Physical Surface(1) = {14};
Physical Surface(2) = {16};
Physical Surface(3) = {18};
Physical Surface(4) = {20};
