import numpy as np
import streamlit as st
import scipy as smp 
import sympy as sp
import matplotlib.pyplot as plt
from scipy.integrate import quad
from scipy.integrate import odeint

import sympy as sp

# define symbolic variable
Xa = sp.Symbol('Xa')

# define constants (you can use numerical values or keep them symbolic)
CaO = 0.00003  # initial concentration of A
CbO = 0.1   # initial concentration of B
k = 14  # rate constant
a = 1      # stoichiometric coefficient for A
b = 1     # stoichiometric coefficient for B

# define the rate equation symbolically
Ca = sp.factor((CaO * (1 - Xa)) ** a) # concentration of component a to the poower of the stoichometric coefficent 
Cb = sp.factor((CbO - ((b/a) * CaO * Xa)) ** b) # concentration of component b to the poower of the stoichometric coefficent 
rate = k * Ca

# simplify the expression
rate_simplified = sp.simplify(rate)
rate_inv = 1 / rate_simplified
f_numeric = sp.lambdify(Xa, rate_inv, modules='numpy')

print("Cb in terms of Xa")
print(Cb)
print("Ca in terms of Xa")
print(Ca)

# define integration limits
Xa_lower = 0.0  # Lower limit (typically 0 for no conversion)
Xa_upper = 0.97  # Upper limit (example: 80% conversion)

# perform numerical integration
integral_result, _ = quad(f_numeric, Xa_lower, Xa_upper)

# multiply by CA0 to get actual time
residence_time = CaO * integral_result

# output
print(f"\nTime to reach {Xa_upper*100:.1f}% conversion = {time_required:.4f} hours")

Volume = 150
Volumetric_flowrate = Volume/residence_time 
print("volumetric flowrate (m^3/hr)")
print(Volumetric_flowrate)
