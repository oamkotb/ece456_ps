## -- FOR CALCULATING U FOR PROBLEM 1 PART C PART 3 -- ##

import matplotlib.pyplot as plt
import numpy as np

# -----------------------------
# Physical constants in MKS units
# -----------------------------
hbar = 1.054e-34  # [J*s] reduced Planck constant
q = 1.602e-19  # [C] elementary charge

# -----------------------------
# Energy parameters in eV
# -----------------------------
U0 = 0.25  # [eV] single-electron charging energy
kBT = 0.025  # [eV] thermal energy (k_B*T)
mu = 0.0  # [eV] equilibrium Fermi level (chemical potential)
cal_E = 0.2  # [eV] energy level (center of DOS)

# -----------------------------
# Capacitance / coupling factors (dimensionless)
# -----------------------------
alpha_G = 0.5  # [-] gate coupling
alpha_D = 0.5  # [-] drain coupling
alpha_S = 1.0 - alpha_G - alpha_D  # [-] source coupling (so alphas sum to 1)

# -----------------------------
# Energy grid in eV
# -----------------------------
NE = 501  # [-] number of energy points

E = np.array([(-1.0 + 2.0 * i / (NE - 1)) for i in range(NE)])  # [eV] from -1 to +1
dE = E[1] - E[0]  # [eV] energy step

# -----------------------------
# Gamma parameters (eV)
# -----------------------------
gamma_1 = 0.005  # [eV] coupling/broadening from contact 1
gamma_2 = 0.005  # [eV] coupling/broadening from contact 2
gamma = gamma_1 + gamma_2  # [eV] total broadening

# -----------------------------
# Lorentzian density of states D(E) (normalized)
# -----------------------------
D = np.array([(gamma / (2 * np.pi)) / ((e - cal_E) ** 2 + (gamma / 2) ** 2) for e in E])

# Normalize so that sum(D)*dE = 1
norm = dE * sum(D)
D = np.array([d / norm for d in D])  # [1/eV] normalized DOS

# -----------------------------
# Reference electron number (dimensionless count)
# -----------------------------
N0 = 0  # [-] reference number of electrons in channel

# -----------------------------
# Voltage sweep (V)
# -----------------------------
NV = 101  # [-] number of voltage points
VV = [0.0 + 1.0 * i / (NV - 1) for i in range(NV)]  # [V] from 0 to 1
dV = VV[1] - VV[0]  # [V] voltage step

# Loop over the voltage values and compute number of electrons
# and current for each voltage value in a self-consistent manner
N = np.zeros(NV)

# Current that we are solving for
I = np.zeros(NV)

for count in range(1, NV):
    # Set terminal voltages
    VG = 0.0  # [V] gate voltage
    VD = VV[count]  # [V] drain voltage (from the sweep array)
    VS = 0.0  # [V] source voltage

    # Chemical potentials (energy in eV)
    mu1 = 0.3760  # [eV] chemical potential of contact 1 (source-side)
    mu2 = 0.6240  # [eV] chemical potential of contact 2 (drain-side)

    # Laplace potential contribution (energy shift in eV)
    UL = -(alpha_G * VG) - (alpha_D * VD) - (alpha_S * VS)  # [eV]

    # Initial Poisson (self-consistent) potential contribution
    UP = 0.0  # [eV] initial guess for Poisson part

    # (Often the total potential shift used later is:)
    U = UL + UP  # [eV] total potential energy shift (if needed)

    dUP = 1
    f1 = np.array(NV)
    f2 = np.zeros(NV)

    while dUP > 1e-6:
        U = UL + UP
        # Compute source and drain Fermi function
        f1 = np.array([1 / (1 + np.exp((E + U - mu1) / kBT)) for E in E])  # source
        f2 = np.array([1 / (1 + np.exp((E + U - mu2) / kBT)) for E in E])  # drain

        # Compute number of channel electrons
        N[count] = dE * np.sum((gamma_1 * f1 + gamma_2 * f2) * D) / gamma

        # Newly calculated Poisson part of the self-consistent potential
        UPnew = U0 * (N[count] - N0)

        # Change in Poisson part
        dUP = abs(UP - UPnew)

        # Change in Poisson part between iterations
        UP += 0.1 * (UPnew - UP)

    # Compute the current after the self-consistent potential
    # I[count] = q * (q / hbar) * (gamma_1 * gamma_2) / gamma * dE * np.sum((f1 - f2) * D)
    print(UL + UP)
