Include "options01_data.geo";
h = 1/N;
R=1.;
r=0.3;
r1=0.1;
c=0.7;
theta3=Pi/8;
l=0.5;
// Center Points of circle
Point(1) = {0, 0, 0, h}; 
Point(2) = {0,R, 0, h};
Point(3) = {0,-R, 0, h};
Point(10) = {R,0, 0, h};
Point(11) = {-R,0, 0, h};

// Points on circles
angle=Pi/4;
Point(100) = {c*Cos(angle) ,c*Sin(angle), 0, h};
Point(101) = {(c+r1)*Cos(angle) ,(c+r1)*Sin(angle), 0, h};
Point(102) = {(c-r1)*Cos(angle) ,(c-r1)*Sin(angle), 0, h};
Point(103) = {c*Cos(angle)+r1 ,c*Sin(angle), 0, h};
angle=angle+Pi/2;
Point(110) = {c*Cos(angle) ,c*Sin(angle), 0, h};
Point(111) = {(c+r1)*Cos(angle) ,(c+r1)*Sin(angle), 0, h};
Point(112) = {(c-r1)*Cos(angle) ,(c-r1)*Sin(angle), 0, h};
Point(113) = {c*Cos(angle)-r1 ,c*Sin(angle), 0, h};
angle=angle+Pi/2;
Point(120) = {c*Cos(angle) ,c*Sin(angle), 0, h};
Point(121) = {(c+r1)*Cos(angle) ,(c+r1)*Sin(angle), 0, h};
Point(122) = {(c-r1)*Cos(angle) ,(c-r1)*Sin(angle), 0, h};
Point(123) = {c*Cos(angle)-r1 ,c*Sin(angle), 0, h};
angle=angle+Pi/2;
Point(130) = {c*Cos(angle) ,c*Sin(angle), 0, h};
Point(131) = {(c+r1)*Cos(angle) ,(c+r1)*Sin(angle), 0, h};
Point(132) = {(c-r1)*Cos(angle) ,(c-r1)*Sin(angle), 0, h};
Point(133) = {c*Cos(angle)+r1 ,c*Sin(angle), 0, h};


Circle(5) = {121, 120, 123};
Circle(8) = {123, 120, 122};
Circle(6) = {122, 1, 132};
Circle(7) = {121, 1, 131};

Circle(14) = {102, 1, 112};
Circle(15) = {101, 1, 111};
Circle(16) = {111, 110, 113};
Circle(13) = {113, 110, 112};
Circle(17) = {131, 130, 133};
Circle(18) = {133, 130, 132};
Circle(19) = {101, 100, 103};
Circle(20) = {103, 100, 102};


Circle(21) = {3, 1, 10};
Circle(22) = {10, 1, 2};
Circle(23) = {2, 1, 11};
Circle(24) = {11, 1, 3};



Translate {0, 0, 2} {
  Duplicata { Point{11, 3, 10, 2, 1, 120, 122, 121, 123, 130, 132, 131, 133, 100, 102, 103, 101, 111, 113, 110, 112}; }
}
Circle(25) = {134, 138, 135};
Circle(26) = {135, 138, 136};
Circle(27) = {136, 138, 137};
Circle(28) = {137, 138, 134};
Circle(29) = {154, 138, 148};
Circle(30) = {150, 138, 151};
Circle(31) = {151, 153, 152};
Circle(32) = {152, 153, 154};
Circle(33) = {148, 147, 149};
Circle(34) = {149, 147, 150};
Circle(35) = {140, 138, 144};
Circle(36) = {145, 138, 141};
Circle(37) = {141, 139, 142};
Circle(38) = {142, 139, 140};
Circle(39) = {145, 143, 146};
Circle(40) = {146, 143, 144};
Line(41) = {11, 134};
Line(42) = {2, 137};
Line(43) = {10, 136};
Line(44) = {3, 135};
Line Loop(45) = {38, 35, -40, -39, 36, 37};
Plane Surface(46) = {45};
Line Loop(47) = {30, 31, 32, 29, 33, 34};
Plane Surface(48) = {47};
Line Loop(49) = {27, 28, 25, 26};
Plane Surface(50) = {45, 47, 49};
Line Loop(51) = {5, 8, 6, -18, -17, -7};
Plane Surface(52) = {51};
Line Loop(53) = {16, 13, -14, -20, -19, 15};
Plane Surface(54) = {53};
Line Loop(55) = {23, 24, 21, 22};
Plane Surface(56) = {51, 53, 55};
Line Loop(57) = {44, 26, -43, -21};
Line(58) = {145, 131};
Line(59) = {133, 146};
Line(60) = {144, 132};
Line(61) = {140, 122};
Line(62) = {123, 142};
Line(63) = {121, 141};
Line(64) = {150, 101};
Line(65) = {103, 149};
Line(66) = {148, 102};
Line(67) = {112, 154};
Line(68) = {152, 113};
Line(69) = {111, 151};
Line Loop(70) = {58, 17, 59, -39};
Ruled Surface(71) = {70};
Line Loop(72) = {18, -60, -40, -59};
Ruled Surface(73) = {72};
Line Loop(74) = {34, 64, 19, 65};
Ruled Surface(75) = {74};
Line Loop(76) = {65, -33, 66, -20};
Ruled Surface(77) = {76};
Line Loop(78) = {38, 61, -8, 62};
Ruled Surface(79) = {78};
Line Loop(80) = {62, -37, -63, 5};
Ruled Surface(81) = {80};
Line Loop(82) = {13, 67, -32, 68};
Ruled Surface(83) = {82};
Line Loop(84) = {16, -68, -31, -69};
Ruled Surface(85) = {84};
Line Loop(86) = {29, 66, 14, 67};
Ruled Surface(87) = {86};
Line Loop(88) = {64, 15, 69, -30};
Ruled Surface(89) = {88};
Line Loop(90) = {6, -60, -35, 61};
Ruled Surface(91) = {90};
Line Loop(92) = {36, -63, 7, -58};
Ruled Surface(93) = {92};
Ruled Surface(94) = {57};
Line Loop(95) = {27, -42, -22, 43};
Ruled Surface(96) = {95};
Line Loop(97) = {42, 28, -41, -23};
Ruled Surface(98) = {97};
Line Loop(99) = {24, 44, -25, -41};
Ruled Surface(100) = {99};
Surface Loop(101) = {94, 100, 56, 96, 50, 98, 91, 73, 71, 93, 81, 79, 87, 77, 75, 89, 85, 83};
Volume(102) = {101};
Surface Loop(103) = {46, 91, 73, 71, 93, 81, 79, 52};
Volume(104) = {103};
Surface Loop(105) = {48, 87, 77, 75, 89, 85, 83, 54};
Volume(106) = {105};
Physical Volume(11) = {104};
Physical Volume(10) = {106};
Physical Volume(1) = {102};
Physical Surface(110) = {94, 96, 98, 100};
Physical Surface(111) = {50};
Physical Surface(112) = {56};
Physical Surface(113) = {46};
Physical Surface(114) = {48};
Physical Surface(115) = {52};
Physical Surface(116) = {54};
Physical Surface(117) = {89, 75, 77, 87, 85, 83};
Physical Surface(118) = {79, 81, 91, 93, 73, 71};
//+
Physical Line(119) = {30, 31, 32, 29, 33, 34};
//+
Physical Line(120) = {38, 37, 36, 40, 39, 35};
//+
Physical Line(121) = {13, 16, 15, 19, 20, 14};
//+
Physical Line(122) = {6, 18, 17, 7, 5, 8};
//+
Physical Line(123) = {26, 27, 28, 25};
//+
Physical Line(124) = {23, 24, 21, 22};
