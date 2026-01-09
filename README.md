# N-Body Gravitational Simulation (Python)
A 3D Newtonian N-body gravitational simulation implemented from scratch in Python using NumPy and Matplotlib.  
The project demonstrates the numerical evolution of a self-gravitating particle system and real-time visualization of emergent dynamics.

## Overview
This simulation models the motion of `N = 1000` particles interacting via Newtonian gravity.  
Each particle experiences the gravitational force from every other particle, with force softening applied to avoid singularities at small separations.
The system is evolved in time using a **symplectic Euler integrator**, which offers better stability than forward Euler for Hamiltonian systems.
The primary goal of this project is **conceptual clarity and numerical understanding**, not performance optimization.

<img width="827" height="815" alt="Screenshot 2026-01-10 012411" src="https://github.com/user-attachments/assets/f43dbbbd-647b-4b17-b141-347eff17302f" />

## Features
- 3D Newtonian gravitational dynamics
- Softened gravity to prevent numerical divergence
- Equal-mass particles
- Spherically distributed initial conditions
- Approximate tangential velocities for orbital motion
- Real-time 3D visualization using Matplotlib
- Camera rotation for improved visual intuition


## Numerical Method
- **Integrator:** Symplectic Euler  
- **Time step:** `dt = 0.01`
- **Force complexity:** \( O(N^2) \)
This implementation prioritizes transparency over efficiency.  
For large-scale or long-term simulations, more advanced methods (e.g., Barnes–Hut, leapfrog integration) would be required.



## Requirements
- Python 3.8+
- NumPy
- Matplotlib

Install dependencies using:
```bash
pip install numpy matplotlib
