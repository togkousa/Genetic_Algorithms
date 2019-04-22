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
Point(4) = {0,r, 0, h};
Point(5) = {0,-r, 0, h};
Point(6) = {r*Cos(theta3),r*Sin(theta3), 0, h};
Point(56) = {r*Cos(theta3)+l,r*Sin(theta3), 0, h};
Point(7) = {r*Cos(theta3),-r*Sin(theta3), 0, h};
Point(57) = {r*Cos(theta3)+l,-r*Sin(theta3), 0, h};
Point(8) = {r*Cos(Pi-theta3),r*Sin(Pi-theta3), 0, h};
Point(58) = {r*Cos(Pi-theta3)-l,r*Sin(Pi-theta3), 0, h};
Point(9) = {r*Cos(Pi-theta3),-r*Sin(Pi-theta3), 0, h};
Point(59) = {r*Cos(Pi-theta3)-l,-r*Sin(Pi-theta3), 0, h};

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


Circle(3) = {6, 1, 8};
Circle(4) = {9, 1, 7};
Circle(5) = {121, 120, 123};
Circle(1005) = {122, 120, 123};
Circle(6) = {122, 1, 132};
Circle(7) = {121, 1, 131};


Line(8) = {8, 58};
Line(9) = {59, 58};
Line(10) = {59, 9};
Line(11) = {7, 57};
Line(12) = {57, 56};
Line(13) = {56, 6};
Circle(14) = {102, 1, 112};
Circle(15) = {101, 1, 111};
Circle(16) = {111, 110, 112};
Circle(17) = {131, 130, 133};
Circle(18) = {133, 130, 132};
Circle(19) = {101, 100, 103};
Circle(20) = {103, 100, 102};

Line Loop(21) = {15, 16, -14, -20, -19};
Line Loop(23) = {1005, -5, 7, 17, 18, -6};
Line Loop(25) = {2, 1};
Line Loop(26) = {10, 4, 11, 12, 13, 3, 8, -9};
Plane Surface(27) = {21};
Plane Surface(28) = {23};

Circle(29) = {2, 1, 11};
Circle(30) = {11, 1, 3};
Circle(31) = {3, 1, 10};
Circle(32) = {10, 1, 2};
Line Loop(33) = {29, 30, 31, 32};
Plane Surface(34) = {21, 23, 26, 33};
Translate {0, 0, 2} {
  Duplicata { Surface{34, 27, 28}; }
}
Line(65) = {190, 58};
Line(66) = {189, 59};
Line(67) = {194, 8};
Line(68) = {216, 9};
Line(69) = {211, 7};
Line(70) = {199, 6};
Line(71) = {203, 56};
Line(72) = {207, 57};
Line(73) = {223, 2};
Line(74) = {235, 11};
Line(75) = {230, 3};
Line(76) = {225, 10};
//+
Line Loop(1037) = {12, -71, 1022, 72};
//+
Plane Surface(1038) = {1037};
//+
Line Loop(1039) = {1023, 69, 11, -72};
//+
Plane Surface(1040) = {1039};
//+
Line Loop(1041) = {13, -70, 1021, 71};
//+
Plane Surface(1042) = {1041};
//+
Line Loop(1043) = {9, -65, -1018, 66};
//+
Plane Surface(1044) = {1043};
//+
Line Loop(1045) = {10, -68, 1025, 66};
//+
Plane Surface(1046) = {1045};
//+
Line Loop(1047) = {1019, 67, 8, -65};
//+
Plane Surface(1048) = {1047};
//+
Line Loop(1049) = {76, -31, -75, -1027};
//+
Ruled Surface(1050) = {1049};
//+
Line Loop(1051) = {1026, 76, 32, -73};
//+
Ruled Surface(1052) = {1051};
//+
Line Loop(1053) = {74, -29, -73, -1029};
//+
Ruled Surface(1054) = {1053};
//+
Line Loop(1055) = {1028, 74, 30, -75};
//+
Ruled Surface(1056) = {1055};
//+
Line Loop(1057) = {1024, 68, 4, -69};
//+
Ruled Surface(1058) = {1057};
//+
Line Loop(1059) = {1020, 70, 3, -67};
//+
Ruled Surface(1060) = {1059};
//+
Surface Loop(1061) = {1036, 1006, 1030, 1044, 34, 27, 28, 1048, 1060, 1042, 1038, 1040, 1058, 1046, 1052, 1050, 1056, 1054};
//+
Volume(1062) = {1061};
//+
Physical Volume(1) = {1062};
//+
Physical Surface(1) = {1052, 1054, 1056, 1050};
//+
Physical Surface(1021) = {1030};
//+
Physical Surface(1020) = {1036};
//+
Physical Surface(1000) = {1006};
//+
Physical Surface(2020) = {28};
//+
Physical Surface(2021) = {27};
//+
Physical Surface(2000) = {34};
//+
//Physical Surface(1071) = {1044, 1048, 1046};
//+
Physical Surface(31) = {1040, 1038, 1042,1044, 1048, 1046};
//+
Physical Surface(11) = {1058};
//+
Physical Surface(10) = {1060};
//+
Physical Line(1075) = {1026, 1027, 1028, 1029};
//+
Physical Line(1076) = {31, 32, 29, 30};
//+
Physical Line(1077) = {1013, 1014, 1015, 1012, 1017, 1016};
//+
Physical Line(1078) = {1011, 1010, 1009, 1008, 1007};
//+
Physical Line(1079) = {19, 20, 14, 16, 15};
//+
Physical Line(1080) = {17, 18, 6, 1005, 5, 7};
//+
Physical Line(1081) = {1018, 1025, 1024, 1023, 1022, 1021, 1020, 1019};
//+
Physical Line(1082) = {8, 9, 10, 4, 11, 12, 13, 3};
//+
Physical Line(1083) = {71, 72, 70, 69, 67, 68, 65, 66};
