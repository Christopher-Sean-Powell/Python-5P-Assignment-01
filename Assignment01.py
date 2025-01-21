__author__ = 'Chris'

# Christopher Powell

#cspowell@ucsc.edu

# Assignment 01: Fun with Triangles

# This first function calculates the perimeter of a triangle given the 3 side lengths



def triangle_perimeter (side_a, side_b, side_c):
    perimeter = side_a + side_b + side_c
    return (perimeter)

side_a = float(raw_input("Please enter a side of your triangle" ))

side_b = float(raw_input("Please enter another side of your triangle" ))

side_c = float(raw_input("Please enter the third side of your triangle" ))

perimeter = triangle_perimeter(side_a, side_b, side_c)

# This function calculates the area of a triangle given the side lengths

# I used Heron's formula to calculate the area, which I found at http://mathworld.wolfram.com/HeronsFormula.html

def triangle_area (side_a, side_b, side_c):
    semi_perimeter = .5*(side_a + side_b + side_c)
    sp = semi_perimeter
    area = (sp*(sp-side_a)*(sp-side_b)*(sp-side_c)) ** .5
    return (area)

area = triangle_area(side_a, side_b, side_c)

# This last function calculates the angles of a triangle given the side lengths

# I used the law of cosines, which I got from http://www.mathsisfun.com/algebra/trig-solving-sss-triangles.html

import math

def triangle_angle_a(side_a, side_b, side_c):
    angle_a = math.acos((side_b ** 2 + side_c ** 2 - side_a ** 2)/(2 * side_b * side_c))
    return (angle_a)

angle_a = triangle_angle_a(side_a, side_b, side_c)*(180/3.14159265)

angle_b = (triangle_angle_a(side_b, side_c, side_a))*(180/3.14159265)

angle_c = (triangle_angle_a(side_c, side_a, side_b))*(180/3.14159265)

# ^^ This part above is to reference the angle function 3 times, with different input parameters, in order to
# produce all 3 angles.

print "The perimeter of the triangle with sides {0}, {1}, {2} is {3} and the area is {4:.4g}.".format (side_a, side_b, side_c, perimeter, area)

print "The angle across from the side of length {0} is {1:.4g}, the angle across from the side of length {2} is {3:.4g},and the angle across from the side of length {4} is {5:.4g}.".format(side_a, angle_a, side_b, angle_b, side_c, angle_c)
