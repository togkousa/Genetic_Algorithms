// N=4;
h = 1/N;
L=10; // [0,L]x[-1,1]
r=0.3;

Point(1) = {0, -1, 0, h}; 
Point(2) = {L, -1, 0, h};
Point(3) = {L, 1, 0, h};
Point(4) = {0,1, 0, h};

ip=newp;
For t In {1:4}
  ip=10*t;
  Point(ip) = {2*t, 0, 0, h};
  ip+=1;
  Point(ip) = {2*t, -r, 0, h};
  ip+=1;
  Point(ip) = {2*t, +r, 0, h};
EndFor  
Line(1) = {1, 2};
Line(2) = {2, 3};
Line(3) = {3, 4};
Line(4) = {4, 1};
Circle(5) = {12, 10, 11};
Circle(6) = {11, 10, 12};
Circle(7) = {22, 20, 21};
Circle(8) = {21, 20, 22};
Circle(9) = {32, 30, 31};
Circle(10) = {31, 30, 32};
Circle(11) = {42, 40, 41};
Circle(12) = {41, 40, 42};
Line Loop(13) = {3, 4, 1, 2};
Line Loop(14) = {5, 6};
Line Loop(15) = {7, 8};
Line Loop(16) = {9, 10};
Line Loop(17) = {11, 12};
Plane Surface(18) = {13, 14, 15, 16, 17};
Physical Line(1) = {4};
Physical Line(2) = {1};
Physical Line(3) = {2};
Physical Line(4) = {3};
Physical Line(12) = {6, 5};
Physical Line(14) = {8, 7};
Physical Line(16) = {10, 9};
Physical Line(18) = {12, 11};
Physical Surface(1) = {18};
