import sys
# import tamkin as tk
# from molmod import centimeter, lightspeed
import os
# from molmod import centimeter, lightspeed


import numpy as np
import BAD
import gaussian_analysis_module
import matplotlib.pyplot as plt



file_obj = gaussian_analysis_module.Gaussian_module("opt.log")
opt_coords = file_obj.getOptcoords()

with open("Report.txt",'w') as f:
    f.write("Distance between atom 5 and 8 ="+str(BAD.dist(opt_coords[4],opt_coords[8]))+"\n")
    f.write("Angle containing atoms 1, 13, and 12 ="+str(BAD.Angle(opt_coords[0],opt_coords[12],opt_coords[11]))+"\n")
    f.write("Dihedral angle involving atoms 10, 9, 12, and 13 ="+str(BAD.dihedralAngle(opt_coords[9],opt_coords[8],opt_coords[11],opt_coords[12])))


