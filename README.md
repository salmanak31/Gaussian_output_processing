# Code to process gaussian output
This repository contains code to get optimized coordinates, energies, masses etc from files generated from Gaussian. It also contains code to calculate geometric parameters: distances, angles and dihedrals.

gaussian_analysis_module.py contains the Gaussian class with functions to extract coordinates, energies, masses etc from gaussian output. BAD.py contains functions to calculate distances, angles, and dihedrals. get_geom.py is an example file extracting geometric information from the opt.log file.
