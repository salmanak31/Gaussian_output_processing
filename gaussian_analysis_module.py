import numpy as np
import re

class Gaussian_module:
    def __init__(self, file):
        # self.Temperature = Temperature
        # self.Pressure = Pressure
        self.file = file

    def getElectronic_E(self):
        # get electronic energy
        lookup = "SCF Done"   
        EE = []
        f = open(self.file,"r")
        for line in f:
            if lookup in line:
                EE.append(line.split())
        EE = float(EE[len(EE)-1][4])
        f.close()
        return EE

    def getNum_atoms(self):
        # function to get number of atoms
        lookup = "Charge ="   
        count = 0
        f = open(self.file,"r")
        for line in f:
            if lookup in line:
                for i in range(0,1000000):
                    line = next(f)
                    if len(line.strip()) == 0:
                        break
                    count = count + 1
            if count > 0:
                break
        Num_atoms = count
        f.close()
        return Num_atoms

    def getMasses(self):
        # function to  get masses
        lookup = "- Thermochemistry -"   
        Masses = []
        f = open(self.file,"r")
        for line in f:
            if lookup in line:
                line = next(f)
                line = next(f)
                line = next(f)
                for i in range (0,Gaussian_module.getNum_atoms(self)):
                    if "mass**********" in line.split()[-1]:
                        Masses.append("100000000")
                    else:
                        Masses.append(line.split()[-1])
                    line = next(f)
                break
        f.close()
        return np.asarray(Masses,dtype=np.float32)

    def getAtomlist(self):
        lookup = "Symbolic Z-matrix:"
        Atoms = []
        with open(self.file,"r") as f:
            for line in f:
                if lookup in line:
                    line = next(f)
                    line = next(f)
                    for i in range (0,Gaussian_module.getNum_atoms(self)):
                        Atoms.append(re.split('\(',line)[0].split())
                        line = next(f)
                    break
        for i in range(0,len(Atoms)):
            Atoms[i] = Atoms[i][0]
        return Atoms

    def optComplete(self):
        # function to check if optimization was completed
        # label=0 -> optimization didnt finish
        # label=1 -> optimization completed
        label = 0
        with open(self.file,"r") as f:
            for line in f:
                if " Optimization completed." in line:
                    label = 1
        return label


    def getLastcoords(self):
        # function to get coordinates of input structure
        Coords = []
        with open(self.file,"r") as f:
            for line in f:
                if "Input orientation:" in line:
                    line = f.readline()
                    line = f.readline()
                    line = f.readline()
                    line = f.readline()
                    line = f.readline()
                    for j in range(100000):
                        Coords.append(line.split())
                        line = f.readline()
                        if "---------------------------------------------------------------------" in line:
                            break
        for i in range(0,len(Coords)):
            Coords[i] = Coords[i][3:]
        return np.asarray(Coords[Gaussian_module.getNum_atoms(self)*(len(Coords)/Gaussian_module.getNum_atoms(self)-1):len(Coords)],dtype=np.float32)

    def getOptcoords(self):
        # function to get optimized coordinates
        # add warning if opt complete is not present
        Coords = []
        count = 0
        with open(self.file,"r") as f:
            for line in f:
                if " Optimization completed" in line and count ==0 :
                    count = 1
                    for i in range(0,10000):
                        line = f.readline()
                        if "Input orientation:" in line:
                            line = f.readline()
                            line = f.readline()
                            line = f.readline()
                            line = f.readline()
                            line = f.readline()
                            for j in range(0,100000):
                                Coords.append(line.split())
                                line = f.readline()
                                if "---------------------------------------------------------------------" in line:
                                    break                            
                            break
        for i in range(0,len(Coords)):
            Coords[i] = Coords[i][3:]
        return np.asarray(Coords,dtype=np.float32)