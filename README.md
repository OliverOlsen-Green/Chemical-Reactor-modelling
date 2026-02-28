# Chemical-Reactor-modelling
This repository contains Python-based simulations for simplifed reactor models, including:

- Reversible Plug Flow Reactor (PFR)
- Reversible Continuous Stirred-Tank Reactor (CSTR)
- Irreversible Plug Flow Reactor (PFR)

The models are implemented using a combination of symbolic computation and numerical integration to simulate reaction kinetics and reactor performance under ideal flow conditions.

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
