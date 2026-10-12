"""
Silicon Nanopore Membrane - Filtration Simulation
B.E. Mechanical Engineering - Sathya jothi 
For MSc Mathematical Modelling & Computational Sciences
University of Luxembourg
"""

import numpy as np
import matplotlib.pyplot as plt

# Constants
mu = 0.0035
L = 10e-6
r = 5e-9
w = 20e-9
h = 5e-9
n_pores = 1e10
area = 1e-4

mmHg_to_Pa = 133.322
pressures_mmHg = np.linspace(80, 180, 100)
delta_P = pressures_mmHg * mmHg_to_Pa

# Hydraulic resistance - Hagen-Poiseuille
R_circular = (8 * mu * L) / (np.pi * r**4) / n_pores
R_slit = (12 * mu * L) / (w * h**3 * (1 - 0.63*h/w)) / n_pores

Q_circular = delta_P / R_circular * 1e9 * 60
Q_slit = delta_P / R_slit * 1e9 * 60

plt.figure(figsize=(8,5))
plt.plot(pressures_mmHg, Q_circular, label='Circular Pore', linewidth=2)
plt.plot(pressures_mmHg, Q_slit, label='Slit Pore', linewidth=2)
plt.xlabel('Mean Arterial Pressure (mmHg)')
plt.ylabel('Filtrate Flow Rate (mL/min)')
plt.title('Filtration Comparison: Slit vs Circular')
plt.legend()
plt.grid(True)
plt.savefig('filtration_comparision.png', dpi=300)
plt.show()

print(f"At 120 mmHg: Circular={Q_circular[40]:.2f}, Slit={Q_slit[40]:.2f} mL/min")
