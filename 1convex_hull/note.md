# Convex hull   

## Orientation point segment 

### Dot product

<AB,AP> = AB * AP * cos(a)

### Cross product (2D => determinent)

det(AB, AP) = AB * AP * sin(a) (coord on z of the cross product with an extra 0 z coord)

### Usage

- det product => left or right of the segment
- dot product => before or after A (and before or after the segment)

## Polygone

- closed => connected sequence of line segment
- simple => doesn't intersect itself 

segment cross: check if line cross, if not stop. find the intersection point and check if in segment. 

## Convex 

convex if for all A, B in the polygon, AB is in the polygone

check convex: for every segment, the next vertex is every time on the same side

inside test convex: for every segment, the vertex is on the same side

inside test concave: sum the angle between every vertex, if it's equal to 2PI, it's inside (work for convex too), if it's equals to 0 it's outside

