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

evals, evecs = np.linalg.eigh(H)

pd1 = evecs[:, 1 - 1] ** 2
pd50 = evecs[:, 50 - 1] ** 2
plt.figure()
plt.plot(x, pd1, "k-", label="Eiganvalue 1")
plt.plot(x, pd50, "r-", label="Eigenvalue 50")
plt.xlabel("Grid Position [m]")
plt.ylabel("Probability Density")
plt.legend()
plt.grid()
plt.show()

E = (hbar * np.pi * n) ** 2 / (2 * m * L**2) / q
plt.figure()
plt.plot(n, E, "g-", label="Analytical")
plt.plot(n, evals, "m-", label="Numerical")
plt.plot(
    n,
    2 * t0 * (1 - np.cos(n * np.pi * a / L)),
    "o",
    markerfacecolor="none",
    label="Discrete",
)
plt.xlabel("Eigenvalue Number")
plt.ylabel("Energy [eV]")
plt.legend()
plt.grid()
plt.show()

with np.printoptions(precision=3, suppress=True):
    print(np.linalg.eigh(H))
