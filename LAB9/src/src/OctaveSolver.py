import dataManager as dm
import numpy as np
from scipy.optimize import linprog, OptimizeWarning
import warnings

warnings.simplefilter("error", OptimizeWarning)

# class which provide all managment with 'Octave' scripts and thier result
# (in fact - only file opening)
class LinearSolutionManager:
    def __init__(self):
        return

    def openLinearSolution(self, fileName : str):
        tau = list()
        w = list()

        with open(fileName) as file:
            tau = [float(t) for t in file.readline().split()]
            for line in file.readlines():
                w.append(float(line))
        return tau, w
