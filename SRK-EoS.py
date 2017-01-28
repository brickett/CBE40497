# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 08:45:16 2017

@author: Bryan Ricketts
"""
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
capOmega = 0.480 + 1.574*omega-0.176*omega^2
a=0.42748*R^2*Tc^2/Pc*(1+capOmega*(1-Tr^0.5))^2
b=0.08664*R*Tc/Pc

