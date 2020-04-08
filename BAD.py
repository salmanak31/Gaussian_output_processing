import os
import numpy as np
import math
from numpy.linalg import norm
import sys
import string as str

def dihedralAngle(a, b, c, d):
    # Dihedral angle between atoms a, b, c, and d
    b1 = b-a
    b2 = c-b
    b3 = d-c
    n1 = np.cross(b1/norm(b1), b2/norm(b2))
    n2 = np.cross(b2/norm(b2), b3/norm(b3))
    return np.arctan2(np.dot(np.cross(n1, n2), b2/norm(b2)), np.dot(n1, n2))*180/np.pi

def Angle(a,b,c):
    # angle between vectors a and a (which will be 3 different atoms)
    # A small number is either added or subtracted since we deal with numbers very close to -1 and roundoff error from
    # Gaussian can make it out of the domain of arccos
    a = a - b
    b = c - b	
    dot_norm = np.dot(a, b)/(norm(a)*norm(b))
    if dot_norm < -1:
        return np.arccos(dot_norm + 0.000000000001)*180/np.pi
    elif dot_norm > 1:
        return np.arccos(dot_norm - 0.000000000001)*180 / np.pi
    else:
        return np.arccos(dot_norm) * 180 / np.pi

def dist(a,b):
    return norm(a-b)


# temporay function
def Triangle_Angle(a,b,c,d):
    A1 = Angle(a,b,c)
    A2 = Angle(d,c,b)
    return 180 - (A1+A2)

def d_old(a,b,c,d):
    M1 = (a+b)/2
    M2 = (c+d)/2
    return dist(M1,M2)
