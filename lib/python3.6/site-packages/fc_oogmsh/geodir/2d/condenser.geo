Include "options01_data.geo";
h = 1/N;

// Points for circle
Point(1) = {0, 0, 0, h};
Point(2) = {5, 0, 0, h};
Point(3) = {-5, 0, 0, h};
// Points for left rectangle
Point(4) = {-2, -3, 0, h};
Point(5) = {-1, -3, 0, h};
Point(6) = {-2, 3, 0, h};
Point(7) = {-1, 3, 0, h};
// Points for right rectangle
Point(8) = {2, -3, 0, h};
Point(9) = {1, -3, 0, h};
Point(10) = {2, 3, 0, h};
Point(11) = {1, 3, 0, h};

Circle(1) = {2, 1, 3};
Circle(2) = {3, 1, 2};
Line(3) = {5, 4};
Line(4) = {4, 6};
Line(5) = {6, 7};
Line(6) = {7, 5};
Line(7) = {9, 8};
Line(8) = {8, 10};
Line(9) = {10, 11};
Line(10) = {11, 9};
Line Loop(11) = {1, 2};
Line Loop(12) = {4, 5, 6, 3};
Line Loop(13) = {10, 7, 8, 9};
Plane Surface(14) = {11, 12, 13};


Physical Point(1) = {4};
Physical Point(2) = {5};
Physical Point(3) = {6};
Physical Point(4) = {7};
Physical Point(5) = {8};
Physical Point(6) = {9};
Physical Point(7) = {10};
Physical Point(8) = {11};

Physical Line(1) = {1, 2};
Physical Line(98) = {5, 6, 3, 4};
Physical Line(99) = {9, 8, 7, 10};
Physical Surface(1) = {14};
