translate([0,0,-10])cube([70,150,15]);
cube([10,10,120]);
translate([0,90,0]) cube([10,10,120]);
translate([60,0,0]) cube([10,10,120]);
translate([60,90,0]) cube([10,10,120]);
cube([70,10,15]);
cube([10,50,15]);
translate([60,0,0]) cube([10,50,15]);
translate([10,30,0]) rotate([315,0,0]) cube([50,10,50]);
difference() {
    translate([35,50,40]) cylinder(h = 5, r = 25);
    translate([22,37.5,39]) cylinder(h = 10, r = 5);
}
$fn = 100;
translate([35,50,40]) cylinder(h = 25
, r = 2.5);
translate([0,45,60]) cube([70,10,2.5]);
translate([35,50,62]) cylinder(h = 3, r = 5);
translate([0,45,0]) cube([10,10,120]);
translate([60,45,0]) cube([10,10,120]);
difference() {
    translate([35,50,70]) cylinder(h = 5, r = 25);
    translate([22,37.5,69]) cylinder(h = 10, r = 5);
}
translate([0,45,110]) cube([70,10,2.5]);
translate([32.5,25.5,71]) cube([5,49,39]);
translate([59.5,47.5,71]) rotate([0,0,90]) cube([5,49,39]);
//5translate([49.5,29.5,71]) rotate([0,0,42.5]) cube([5,50,39]);
difference() {
    translate([0,0,120]) cube([70,100,5]);
    translate([35,50,110]) cylinder(h = 30, r = 25);
}
difference() {
    translate([35,50,45.5]) cylinder(h = 80, r = 35);
    translate([35,50,40]) cylinder(h = 100, r = 25);
    translate([35,75,69]) cylinder(h = 7.5, r = 25);
    
    
}
$fn = 100;
translate([35,85,70]) cylinder(h = 5
, r = 10);
translate([35,85,40]) cylinder(h = 5
, r = 10);
translate([30,80,40]) cube(10, 10,20);
translate([30,80,70]) cube(10, 10,20);
translate([0,140,0]) cube([10,10,120]);
translate([60,140,0]) cube([10,10,120]);
translate([0,140,50]) cube([70,10,10]);
translate([0,90,50]) cube([70,10,10]);
translate([0,140,10]) cube([70,10,10]);
translate([0,90,10]) cube([70,10,10]);
difference() {
    translate([0,50,10]) cube([70,100,10]);
    translate([10,90,10]) cube([10,50,11]);
    translate([30,90,10]) cube([10,50,11]);
    translate([50,90,10]) cube([10,50,11]);
}
difference() {
    translate([0,50,50]) cube([70,100,10]);
    translate([10,90,50]) cube([10,50,11]);
    translate([30,90,50]) cube([10,50,11]);
    translate([50,90,50]) cube([10,50,11]);
}
difference() {
    translate([0,70,50]) cube([70,80,10]);
    translate([10,90,50]) cube([10,50,11]);
    translate([30,90,50]) cube([10,50,11]);
    translate([50,90,50]) cube([10,50,11]);
}
difference() {
    translate([0,70,120]) cube([70,80,5]);
    translate([10, 100,119]) cube([10,40,8]);
    translate([30,100,119]) cube([10,40,8]);
    translate([50,100,119]) cube([10,40,8]);
}
//крышка справа
translate([-15, 0, 0]) cube([10, 150, 120]);
translate([-15, 0, 0]) cube([15, 10, 120]);
translate([-15, 140, 0]) cube([15, 10, 120]);
translate([-15, 0, 0]) cube([15, 150, 10]);
translate([-15, 0, 110]) cube([15, 150, 10]);
translate([-15, 50.5, 5]) cube([30, 39, 5]);
translate([-15, 100.5, 5]) cube([30, 38, 5]);
//крышка слева
translate([70, 0, 0]) cube([15, 10, 120]);
translate([70, 140, 0]) cube([15, 10, 120]);
translate([70, 140, 0]) cube([15, 10, 120]);
translate([70, 0, 0]) cube([15, 150, 10]);
translate([70, 0, 110]) cube([15, 150, 10]);
translate([55, 50.5, 5]) cube([30, 39, 5]);
translate([55, 100.5, 5]) cube([30, 38, 5]);
translate([75, 0, 0]) cube([10, 150, 120]);
//крышка сзади
translate([10, 140, 5]) cube([50, 20, 5]);
translate([0, 150, 0]) cube([70, 10, 120]);
//полка для ардуиши
translate([0, 0, 45]) cube([70, 30, 5]);
translate([0, 0, 90]) cube([70, 30, 30]);