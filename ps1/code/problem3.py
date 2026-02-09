import matplotlib.pyplot as plt
import numpy as np

# -----------------------------
# Physical constants in MKS units
# -----------------------------
hbar = 1.054e-34  # [J*s] reduced Planck constant
q = 1.602e-19  # [C] elementary charge

# -----------------------------
# Thermal Energy parameters in eV
# -----------------------------
kBT1 = 0.025  # [eV] thermal energy of contact 1 (source)
kBT2 = 0.026  # [eV] thermal energy of contact 2 (drain)
mu = 0.0  # [eV] equilibrium Fermi level (chemical potential)

# -----------------------------
# Gamma parameters in eV
# -----------------------------
gamma_1 = 0.005  # [eV] coupling/broadening from contact 1
gamma_2 = 0.005  # [eV] coupling/broadening from contact 2
gamma = gamma_1 + gamma_2  # [eV] total broadening

# -----------------------------
# Energy grid for integration (eV)
# -----------------------------
NE = 501  # [-] number of energy points for the grid
E = np.linspace(-1, 1, NE)  # [eV] energy range from -1 to +1
dE = E[1] - E[0]  # [eV] energy step

# -----------------------------
# Channel Energy Sweep (cal_E) in eV
# -----------------------------
N_cal_E = 101  # [-] number of points for channel level sweep
cal_E = np.linspace(-0.25, 0.25, N_cal_E)  # [eV] epsilon range from -0.25 to 0.25
dcal_E = cal_E[1] - cal_E[0]  # [eV] step size for epsilon

# -----------------------------
# Output Arrays
# -----------------------------
N = np.zeros(N_cal_E)  # [-] number of electrons for each epsilon
I = np.zeros(N_cal_E)  # [A] current for each epsilon

# -----------------------------
# Source and Drain Fermi functions
# -----------------------------
f1 = 1 / (1 + np.exp((E - mu) / kBT1))
f2 = 1 / (1 + np.exp((E - mu) / kBT2))


# # from problem 1
# while dUP > 1e-6:
#     U = UL + UP
#     # Compute source and drain Fermi function
#     f1 = np.array([1 / (1 + np.exp((E + U - mu1) / kBT)) for E in E])  # source
#     f2 = np.array([1 / (1 + np.exp((E + U - mu2) / kBT)) for E in E])  # drain

#     # Compute number of channel electrons
#     N[count] = dE * np.sum((gamma_1 * f1 + gamma_2 * f2) * D) / gamma

#     # Newly calculated Poisson part of the self-consistent potential
#     UPnew = U0 * (N[count] - N0)

#     # Change in Poisson part
#     dUP = abs(UP - UPnew)

#     # Change in Poisson part between iterations
#     UP += 0.1 * (UPnew - UP)

# # Compute the current after the self-consistent potential
# I[count] = q * (q / hbar) * (gamma_1 * gamma_2) / gamma * dE * np.sum((f1 - f2) * D)

# q3c
n005 = -1
zero = -1

for count in range(0, N_cal_E):
    # Compute
    D = (gamma / (2 * np.pi)) / ((E - cal_E[count]) ** 2 + (gamma / 2) ** 2)
    N[count] = dE * np.sum((gamma_1 * f1 + gamma_2 * f2) * D) / gamma
    I[count] = q * (q / hbar) * (gamma_1 * gamma_2) / gamma * dE * np.sum((f1 - f2) * D)

    if np.isclose(cal_E[count], -0.05, atol=1e-4):
        n005 = count
        D_n005 = D
    if np.isclose(cal_E[count], 0, atol=1e-4):
        zero = count
        D_zero = D

    # q3c
if n005 != -1:
    plt.figure()
    plt.subplot(1, 2, 1)
    plt.plot(f1 - f2, E, "kx", label="f1 - f2")
    plt.plot(D_n005 / 2500, E, "r-", label="DOS / 2500")
    plt.legend()
    plt.ylabel("Energy (eV)")
    plt.title("Channel Level = -0.05 eV")
    plt.grid()
if zero != -1:
    plt.subplot(1, 2, 2)
    plt.plot(f1 - f2, E, "kx", label="f1 - f2")
    plt.plot(D_zero / 2500, E, "r-", label="DOS / 2500")
    plt.legend()
    plt.ylabel("Energy (eV)")
    plt.title("Channel Level = 0.0 eV")
    plt.grid()
plt.show()


# q3b
plt.figure()
plt.subplot(1, 2, 1)
plt.plot(cal_E, N, linewidth=2)
plt.xlabel("Channel Energy Level")
plt.ylabel("Number of Electrons")
plt.grid()
plt.title("Number of Electrons")

plt.subplot(1, 2, 2)
plt.plot(cal_E, I, linewidth=2)
plt.xlabel("Channel Energy Level")
plt.ylabel("Current")
plt.grid()
plt.title("Thermoelectric Current")

plt.show()
