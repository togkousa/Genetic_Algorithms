Include "options01_data.geo";
h=1/N;
Point(1) = {0, 0, 0, h};
Point(2) = {1, 0, 0, h};
Point(3) = {0.8, 0, 0, h};
Point(4) = {0.6, 0, 0, h};
Point(5) = {0.5, 0, 0, h};
Point(6) = {0.4, 0, 0, h};
// Points A et A'
y=Sqrt(0.8^2-0.1^2);
Point(20) = {0.1, y, 0, h};
Point(30) = {-0.1, y, 0, h};
// Points B et B'
y=Sqrt(0.8^2-0.2^2);
Point(21) = {0.2, y, 0, h};
Point(31) = {-0.2, y, 0, h};
// Points C and C'
y=Sqrt(0.6^2-0.1^2);
Point(22) = {0.1, y, 0, h};
Point(32) = {-0.1, y, 0, h};
// Points D et D'
y=Sqrt(0.6^2-0.2^2);
Point(23) = {0.2, y, 0, h};
Point(33) = {-0.2, y, 0, h};
// Points E et E'
y=Sqrt(0.5^2-0.2^2);
Point(24) = {0.2, y, 0, h};
Point(34) = {-0.2, y, 0, h};

Point(36) = {-0.6, 0, 0, h};
Point(37) = {-0.8, 0, 0, h};
Point(38) = {-0.5, 0, 0, h};
Point(39) = {-0.4, 0, 0, h};
Point(100) = {-1, 0, 0, h};
Circle(2) = {21, 1, 20};
Circle(3) = {30, 1, 31};
Circle(4) = {23, 1, 22};
Circle(5) = {32, 1, 33};
Line(6) = {23, 21};
Line(7) = {20, 22};
Line(8) = {32, 30};
Line(9) = {31, 33};
Circle(10) = {34, 1, 24};
Line(11) = {34, 33};
Line(12) = {24, 23};
Circle(13) = {21, 1, 3};
Circle(14) = {31, 1, 37};
Circle(15) = {37, 1, 3};
Circle(145) = {2, 1, 100};
Circle(146) = {100, 1, 2};
Circle(151) = {6, 1, 39};
Circle(152) = {39, 1, 6};
Line Loop(18) = {3, 9, -5, 8};
Plane Surface(18) = {18};
Line Loop(20) = {2, 7, -4, 6};
Plane Surface(20) = {20};
Line Loop(149) = {145, 146, -8, 5, -11, 10, 12, 4, -7, -2, 13, -15, -14, -3};
Plane Surface(149) = {149};
Line Loop(155) = {14, 15, -13, -6, -12, -10, 11, -9, -152, -151};
Plane Surface(155) = {155};
Line Loop(156) = {151, 152};
Plane Surface(156) = {156};
Physical Line(1) = {145, 146};
Physical Surface(1) = {20,18};
Physical Surface(3) = {149};
Physical Surface(4) = {155};
Physical Surface(5) = {156};
