# Chemical-Reactor-modelling
# Chemical Reactor Simulations

This repository contains Python-based simulations of chemical reactors, including:

- Reversible Plug Flow Reactor (PFR)
- Reversible Continuous Stirred-Tank Reactor (CSTR)
- Irreversible Plug Flow Reactor (PFR)

The models are implemented using a combination of symbolic computation and numerical integration to simulate reaction kinetics and reactor performance under ideal flow conditions.

---

## Features

- Symbolic rate expression generation
- Conversion-based reactor design
- Numerical integration for residence time and volumetric flowrate
- Support for variable stoichiometry and rate constants
- Easy-to-modify code for adding more reactions or reactor types

---

## Reactor Models

### 1. Reversible PFR
- Uses equilibrium constant `Kc`
- Computes conversion, concentration profiles, residence time and the required reactor volume

### 2. Reversible CSTR
- Solves algebraic expression for conversion using equilibrium and reaction rate
- Calculates reactor volume/volumetric flowrate and residence time
  
### 3. Irreversible PFR
- Assumes single-direction reaction
- Simplified rate expression with integration over conversion
