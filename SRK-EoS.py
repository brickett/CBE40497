# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 08:45:16 2017

@author: Bryan Ricketts
"""

import numpy as np
import scipy as sci

print("Calculate molar volume of propane")
print("Input Parameters")
# The function takes inputs of temperature (K) and pressure (bar)
temp=input("Temperature in K = ")
pres=input("Pressure in bar = ")
# convert to float
temp=float(temp)
pres=float(pres)

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
Z = sci.optimize.fsolve(srk, 0.1)

if len(Z)>1:
    print("long")
else:
    print("short")


                