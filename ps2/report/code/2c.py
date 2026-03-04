#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np

# Physical constants in MKS units
hbar = 1.054e-34  # Reduced Planck constant [J*s]
q = 1.602e-19  # Elementary charge [C]
m = 9.110e-31  # Free-electron mass [kg]
e0 = 8.854e-12  # Permitivity of Free Space [F/m]

# Lattice data
N = 100  # Total number of internal lattice points [unitless integer]
n = np.linspace(1, N, N)  # Array of lattice point indices/eigenvalue numbers [unitless]
a = 1e-11  # Lattice constant or distance between grid points [m]
r = a * np.linspace(1, N, N)  # Discretized radial grid [m]
t0 = (
    (hbar**2) / (2 * m * a**2) / q
)  # Hopping parameter / coupling energy, divided by q to convert to [eV]
L = a * (N + 1)  # Total length of the 1D lattice (infinite square well) [m]
lattice_points = np.linspace(0, N + 1) * a
U = (-(q**2) / (4 * np.pi * e0 * r)) / q
diag1 = np.diag(np.array([-t0 for i in range(N - 1)]), -1)
diag2 = np.diag(np.array([2 * t0 for i in range(N)]) + U, 0)
diag3 = np.diag(np.array([-t0 for i in range(N - 1)]), 1)
H = diag1 + diag2 + diag3

evals, evecs = np.linalg.eigh(H)

pd1 = evecs[:, 1 - 1] ** 2
pd2 = evecs[:, 2 - 1] ** 2
print(f"Eigenvalue 1: {evals[1 - 1]} eV")
print(f"Eigenvalue 2: {evals[2 - 1]} eV")

plt.figure()
plt.title("Eigenvalue 1")
plt.plot(r, pd1, "k-", label="Numerical")
plt.plot(
    r,
    a * (2 * r / 0.0529e-9 ** (3 / 2) * np.exp(-r / 0.0529e-9)) ** 2,
    "o",
    markerfacecolor="none",
    label="Analytical",
)
plt.xlabel("Grid Position [m]")
plt.ylabel("Probability Density")
plt.legend()
plt.grid()
plt.show()

plt.figure()
plt.title("Eigenvalue 2")
plt.plot(r, pd2, "r-", label="Numerical")
plt.xlabel("Grid Position [m]")
plt.ylabel("Probability Density")
plt.legend()
plt.grid()
plt.show()

E = (hbar * np.pi * n) ** 2 / (2 * m * L**2) / q
