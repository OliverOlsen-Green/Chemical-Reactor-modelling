import numpy as np
import streamlit as st
import scipy as smp 
import sympy as sp
import matplotlib.pyplot as plt
from scipy.integrate import quad
from scipy.integrate import odeint
from scipy.optimize import fsolve
import sympy as sp
import numpy as np
import pandas as pd

Xa_val = sp.Symbol('X_val')

# Define constants (you can use numerical values or keep them symbolic)
CaO = 1.5  # Initial concentration of A
CbO = 1 #initial concentration of B
CcO = 0 #initial concentration of C
CdO = 0  # initial concentration of D
a = 2 # Stoichiometric coefficient for A
b = 1 # Stoichiometric coefficient for B
c = 1 # Stoichiometric coefficient for C
d = 1 # Stoichiometric coefficient for D
XO = 0.00 
K2 = 5 # reversible reaction rate 
Kc = 16 # equilbrium reaction rate
K1 = 10 # forward reaction rate 
fraction_of_XaEq = 0.8 # fraction of the equilbrium conversion thats desired
# equilibrium concentrations for finding equilibrium conversion 
Ca = (CaO * (1 - Xa_val)) 
Cb = (CbO - (b / a) * CaO * Xa_val) 
Cc = (CcO + (c / a) * CaO * Xa_val)
Cd = (CdO + (d / a) * CaO * Xa_val)

lhs = (Cc**c) * (Cd**d)
rhs = (Ca**a) * (Cb **b) 
    

eqn = sp.Eq(lhs / rhs, Kc)

# Solve symbolically
Xa_solutions = sp.solve(eqn, Xa_val)

# Filter out non-physical or complex results (e.g. Xa < 0 or > 1)
real_solutions = [sol.evalf() for sol in Xa_solutions if sol.is_real and 0 <= sol.evalf() <= 1]

# Display the results
print("Possible equilibrium conversions Xa (real, physical):")
for sol in real_solutions:
    sol_val = sol.evalf()  # Evaluate the symbolic solution
    print(f"Xa = {sol_val:.6f}")


Xa_eq = real_solutions[0]

Xa = sp.Symbol('Xa')
# Define the rate equation symbolically
Ca = sp.factor((CaO * (1 - Xa)) ** a) # concentration of component a to the power of the stoichometric coefficent 
Cb = sp.factor((CbO - ((b/a) * CaO * Xa)) ** b)# concentration of component b to the power of the stoichometric coefficent 
Cc = sp.factor((CcO + ((c/a) * CaO * Xa)) ** c)
Cd = sp.factor((CdO + ((d/a) * CaO * Xa)) ** d)
rate = (K1 * Ca * Cb) - (K2 * Cc * Cd)

# Simplify the expression
rate_simplified = sp.simplify(rate)
rate_inv = 1 / rate_simplified
f_numeric = sp.lambdify(Xa, rate_inv, modules='numpy')

print("Cb in terms of Xa")
print(Cb)
print("Ca in terms of Xa")
print(Ca)

# Define integration limits
Xa_lower = 0.0  # Lower limit 
Xa_upper = fraction_of_XaEq * Xa_eq  # Upper limit 

# Perform numerical integration
integral_result, _ = quad(f_numeric, Xa_lower, Xa_upper)

# Multiply by CA0 to get Tau 
residence_time = CaO * integral_result

Volume = 150
Volumetric_flowrate = Volume/residence_time 
print("volumetric flowrate (m^3/hr)")
print(Volumetric_flowrate)

Xa_final = Xa_upper
print(Xa_final)

Ca_final = Ca.subs(Xa, Xa_upper)
Cb_final = Cb.subs(Xa, Xa_upper)
Cc_final = Cc.subs(Xa, Xa_upper)
Cd_final = Cd.subs(Xa, Xa_upper)

results = pd.DataFrame({
    "component": [a, b, c, d],
    "Initial concentration (Kmol/m^3hr)": [CaO, CbO, CcO, CdO],
    "Final concentration (Kmol/m^3hr)": [Ca_final, Cb_final, Cc_final, Cd_final]
})
print(results)
