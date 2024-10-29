#!/usr/bin/env python
# ray_ellipsoid_intersection.py
#
# Calculates the intersection point (if it exists) between a ray and the Earth
#   reference ellipsoid
#
# Usage: python3 ray_ellipsoid_intersection.py d_l_x d_l_y d_l_z c_l_x
#                                              c_l_y c_l_z
#
# Written by Blake Batchelor, batchelorbh@vt.edu
# Other contributors: none
#
# Parameters:
#    d_l_x               x-component of origin-referenced ray direction
#    d_l_y               y-component of origin-referenced ray direction
#    d_l_z               z-component of origin-referenced ray direction
#    c_l_x               x-component offset of ray origin
#    c_l_y               y-component offset of ray origin
#    c_l_z               z-component offset of ray origin
#
# Output:
#    Print output x, y, and z components of the intersection point if it exists
#
# Revision history:
#    10/22/2024          Script created
#
###############################################################################

#Import relevant modules
import sys
from math import sqrt

#Constants
R_E_KM = 6378.137
E_E = 0.081819221456

#Scalar multiplication
def smul(s,v):
   return [s*e for e in v]

#Vector addition
def add(v1,v2):
   if len(v1) != len(v2):
       return None
   else:
       v3 = []
       for i in range(0, len(v1)):
           v3.append(v1[i] + v2[i])
       return v3

#Pre-initialize input parameters
d_l_x = float('nan') #x-component of origin-referenced ray direction
d_l_y = float('nan') #y-component of origin-referenced ray direction
d_l_z = float('nan') #z-component of origin-referenced ray direction
c_l_x = float('nan') #x-component offset of ray origin
c_l_y = float('nan') #y-component offset of ray origin
c_l_z = float('nan') #z-component offset of ray origin

#Arguments are strings by default
if len(sys.argv) == 7:
   d_l_x = float(sys.argv[1])
   d_l_y = float(sys.argv[2])
   d_l_z = float(sys.argv[3])
   c_l_x = float(sys.argv[4])
   c_l_y = float(sys.argv[5])
   c_l_z = float(sys.argv[6])
else:
   print(('Usage: ray_ellipsoid_intersection.py d_l_x d_l_y d_l_z c_l_x ' \
          'c_l_y c_l_z'))
   sys.exit()

#Main body of script
d_l = [d_l_x, d_l_y, d_l_z] #Must be a unit vector
c_l = [c_l_x, c_l_y, c_l_z]

#Calculate discriminant
a = d_l[0]**2 + d_l[1]**2 + d_l[2]**2 / (1-E_E**2)
b = 2 * (d_l[0]*c_l[0] + d_l[1]*c_l[1] + d_l[2]*c_l[2] / (1 - E_E**2))
c = c_l[0]**2 + c_l[1]**2 + c_l[2]**2 / (1-E_E**2) - R_E_KM**2

discr = b**2 - 4.0 * a * c

#Calculate intersection point
if discr >= 0.0:
    d = (-b - sqrt(discr)) / (2 * a)
    if d < 0.0:
        d = (-b + sqrt(discr)) / (2 * a)
    if d >= 0.0:
        l_d = add(smul(d, d_l), c_l)
        print(l_d[0]) # x-component of intersection point
        print(l_d[1]) # y-component of intersection point
        print(l_d[2]) # z-component of intersection point
        