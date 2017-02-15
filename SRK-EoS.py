# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 08:45:16 2017

@author: Bryan Ricketts
"""

import numpy as np
#import scipy.optimize as sci
#import scipy.optimize as sci #import just the optimize library
from scipy.optimize import fsolve # imports just the function you need

print("Calculate molar volume of propane")

print("Input Parameters")
# The function takes inputs of temperature (K) and pressure (bar)
temp=input("Temperature in K = ")
pres=input("Pressure in bar = ")
# convert to float
temp=float(temp)
pres=float(pres)
"""
To make this section more robust, make sure that the string looks like a number
"""

#temp=300.
#pres=0.01

# set critical properties (source: NIST WebBook)
Tc=369.9 #K 
Pc=42.5  #bar
omega=0.1524
R=0.08314 #L*bar/(K*mol)

# Calculate Soave-Redlich-Kwong EoS parameters
Tr=temp/Tc  #reduced temperature
capOmega = 0.480 + 1.574*omega-0.176*omega**2
a=0.42748*R**2*Tc**2/Pc*(1+capOmega*(1-Tr**0.5))**2
b=0.08664*R*Tc/Pc

# Calculate second round SRK parameters
Aprime = a*pres/(R*temp)**2
Bprime = b*pres/(R*temp)

# Make SRK function
def srk(z):
    y = z**3 - z**2 + (Aprime - Bprime - Bprime**2)*z - Aprime*Bprime
    return y

#solve for roots
Z = fsolve(srk, 0.1) 
"""the function is a first class variable - it's an object
including parentheses and an input only evaluates the return of the function
"""

if temp>Tc:  #condition in which T is above Tc means only one real solution
    V=Z*R*temp/pres
    print('\nV = {0:0.3f} L/mol\n'.format(V[0]))
else:
    # Use Antoine equation to determine saturation pressure
    # Select proper range of coefficients from NIST WebBook
    if temp<=230:
        A = 4.01158
        B = 834.26
        C = -22.763
    elif temp<=320:
        A = 3.98292
        B = 819.296
        C = -24.417
    else:
        A = 4.53678
        B = 1149.36
        C = -24.906
    Psat = np.exp(A - B/(C+temp))
    Psat = round(Psat, 2)
    # Select the proper number of roots by comparing pres to Psat
    if abs(Psat-pres)<0.01:    #could also use numpy.allclose
        #saturated system -> smallest=saturated liquid, largest=saturated vapor
         V=Z*R*temp/pres
         print('\nV = {0:1.3f} L/mol, saturated liquid\n'.format(V[0]))
         print('\nV = {0:1.3f} L/mol\n'.format(V[-1]))
         print("saturated")
    
    elif pres>Psat:
        #compressed liquid -> smallest root
         V=Z*R*temp/pres
         print('\nV = {0:1.3f} L/mol\n'.format(V[0]))
         print("compressed")
         
    elif pres<Psat:
        #superheated vapor -> largest root
         V=Z*R*temp/pres
         print('\nV = {0:1.3f} L/mol\n'.format(V[-1]))
         print("superheated")


                