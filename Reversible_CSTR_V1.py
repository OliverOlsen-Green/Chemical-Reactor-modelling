import numpy as np
import streamlit as st
import scipy as smp 
import sympy as sp
import matplotlib.pyplot as plt
from scipy.integrate import quad
from scipy.integrate import odeint
from scipy.optimize import fsolve
import sympy as sp

import sympy as sp

# define symbolic variable
Xa_val = sp.Symbol('Xa_val')

# Define constants (you can use numerical values or keep them symbolic)
CaO = 1.5  # initial concentration of A
CbO = 0
CcO = 0  # rate constant
a = 2      # stoichiometric coefficient for A
b = 1
c = 1 # stoichiometric coefficient for B
XO = 0.00
K2 = 0.00
KC = 16
K1 = 10
Volumetric_flowrate = 100 

Ca = (CaO * (1 - Xa_val)) 
Cb = (CbO + (b / a) * CaO * Xa_val) 
Cc = (CcO + (c / a) * CaO * Xa_val)

lhs = (Cc**c) * (Cb**b)
rhs = (Ca**a) 
    

eqn = sp.Eq(lhs / rhs, Kc)

# solve symbolically
Xa_solutions = sp.solve(eqn, Xa_val)

# filter out non-physical or complex results (e.g. Xa < 0 or > 1)
real_solutions = [sol.evalf() for sol in Xa_solutions if sol.is_real and 0 <= sol.evalf() <= 1]

# display the results
print("Possible equilibrium conversions Xa (real, physical):")
for sol in real_solutions:
    sol_val = sol.evalf()  # Evaluate the symbolic solution
    print(f"Xa = {sol_val:.6f}")

Xa =sp.Symbol('Xa')
Xa = 0.8 * 0.888889
Ca = (CaO * (1 - Xa)) ** a
Cb = (CbO + ((b / a) * CaO * Xa)) ** b
Cc = (CcO + ((c / a) * CaO * Xa)) ** c
K2 = K1 / KC
rate = (K1 * Ca) - (K2 * Cb * Cc)
rate_simplified = sp.simplify(rate)
rate_inv = 1 / rate_simplified

CSTR_design_EQ = (Xa - XO) * rate_inv 
print(CSTR_design_EQ)

Volume = CSTR_design_EQ * Volumetric_flowrate * CaO
print("volume m^3")
print(Volume)

Tau = Volume / Volumetric_flowrate
print(Tau)
