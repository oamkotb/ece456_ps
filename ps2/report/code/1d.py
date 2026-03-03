#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np

# Physical constants in MKS units
hbar = 1.054e-34  # Reduced Planck constant [J*s]
q = 1.602e-19  # Elementary charge [C]
m = 9.110e-31  # Free-electron mass [kg]

# Lattice data
N = 100  # Total number of internal lattice points [unitless integer]
n = np.linspace(1, N, N)  # Array of lattice point indices/eigenvalue numbers [unitless]
a = 1e-10  # Lattice constant or distance between grid points [m]
x = a * np.linspace(1, N, N)  # Discretized position grid [m]
t0 = (
    (hbar**2) / (2 * m * a**2) / q
)  # Hopping parameter / coupling energy, divided by q to convert to [eV]
L = a * (N + 1)  # Total length of the 1D lattice (infinite square well) [m]
lattice_points = np.linspace(0, N + 1) * a
U = np.zeros(len(x))
diag1 = np.diag(np.array([-t0 for i in range(N - 1)]), -1)
diag2 = np.diag(np.array([2 * t0 for i in range(N)]) + U, 0)
diag3 = np.diag(np.array([-t0 for i in range(N - 1)]), 1)
H = diag1 + diag2 + diag3

# Periodic boundary conditions
H[0, -1] = -t0
H[-1, 0] = -t0

evals, evecs = np.linalg.eigh(H)
pd1 = evecs[:, 1 - 1] ** 2
pd50 = evecs[:, 50 - 1] ** 2
pd4 = evecs[:, 4 - 1] ** 2
pd5 = evecs[:, 5 - 1] ** 2
print(f"Eigenvalue 1: {evals[1 - 1]} eV")
print(f"Eigenvalue 2: {evals[2 - 1]} eV")
print(f"Eigenvalue 3: {evals[3 - 1]} eV")
print(f"Eigenvalue 4: {evals[4 - 1]} eV")
print(f"Eigenvalue 5: {evals[5 - 1]} eV")

plt.figure()
plt.plot(x, pd4, "k-", label="Eigenvalue 4")
plt.plot(x, pd5, "r-", label="Eigenvalue 5")
plt.xlabel("Grid Position [m]")
plt.ylabel("Probability Density")
plt.legend()
plt.grid()
plt.show()

plt.figure()
plt.plot(n, evals, "m-", label="Numerical")
plt.xlabel("Eigenvalue Number")
plt.ylabel("Energy [eV]")
plt.legend()
plt.grid()
plt.show()
