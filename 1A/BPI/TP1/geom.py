#!/usr/bin/env python3

from collections import namedtuple

Point = namedtuple("Point", "x y") 

Triangle = namedtuple("Triangle", "p1 p2 p3")

def affiche_triangle(triangle: Triangle): 
    """Affiche un triangle"""

    print(f"Triangle({triangle.p1}, {triangle.p2}, {triangle.p3})")

tri = Triangle(Point(1, 2), Point(3, 4), Point(5, 6))
affiche_triangle(tri)

