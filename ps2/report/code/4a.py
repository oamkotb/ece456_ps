import matplotlib.pyplot as plt
import numpy as np

# Physical constants in MKS units, including free-electron mass m

hbar = 1.054e-34
q = 1.602e-19
m = 9.110e-31

# SHO frequency

w0 = 0.2879 * q / hbar

# Lattice data: lattice constant "a"; SHO distance parameter beta;
# a discretized spatial grid x; total number of lattice points N;
# Hamiltonian parameter t0, as introduced in class, but now
# divided by q so that it has units of eV; total length of the lattice,
# L = a*(N+1)

# YOU MUST ENTER AN APPROPRIATE VALUE OF "a"

a = 1e-11
beta = np.sqrt(m * w0 / hbar)
x = np.arange(-6 / beta, 6 / beta, a)
N = np.size(x)
t0 = (hbar**2) / (2 * m * a**2) / q
L = a * (N + 1)

# Set up the Hamiltonian matrix, in pieces, by constructing square
# matrices containing information for the main
# diagonal, lower diagonal, and upper diagonal, and then adding them
# together; you may need to look up the diag command using help
# to see how this works; U is the potential energy

U = (1 / q) * (0.5 * m * w0**2 * x**2)
main_D = np.diag(2 * t0 * np.ones(N) + U, 0)
lower_D = np.diag(-t0 * np.ones(N - 1), -1)
upper_D = np.diag(-t0 * np.ones(N - 1), +1)

H = main_D + lower_D + upper_D

# Find the eigenvectors and eigenvalues of H; V will contain the
# eigenvectors in its columns, and D will contain the corresponding
# eigenvalues on its main diagonal

D, V = np.linalg.eig(H)

# The resulting eigenvalues (and the list of corresponding eigenvectors) are not
# sorted by default, so we will sort them from min to max eigenvalue

index = D.argsort()
D = D[index]
V = V[:, index]
E_numerical = D

# Find the eigenvectors corresponding to sorted eigenvalues 1 and 50;
# we can get these from the matrix V, provided we reference the
# appropriate UNSORTED eigenvalue number

phi_numerical_1 = V[:, 0]
phi_numerical_2 = V[:, 1]

# Find the position-probability densities

P_numerical_1 = phi_numerical_1 * np.conj(phi_numerical_1)
P_numerical_2 = phi_numerical_2 * np.conj(phi_numerical_2)

# Plot out the relevant results

plt.figure(1)
plt.plot(x, P_numerical_1, "k-")
plt.grid(color="grey", linestyle=":")
plt.xlabel("POSITION  [m]")
plt.ylabel("PROBABILITY DENSITY  [1/m]")
plt.legend(["Eigenvector 1"])

plt.figure(2)
plt.plot(x, P_numerical_2, "k-")
plt.grid(color="grey", linestyle=":")
plt.xlabel("POSITION  [m]")
plt.ylabel("PROBABILITY DENSITY  [1/m]")
plt.legend(["Eigenvector 2"])

plt.show()
