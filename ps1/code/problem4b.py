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


# q4bi
U = -0.25
q_real = 1

step1 = -0.25
step2 = 0.25
mu1 = (0 - step1) + U
mu2 = (0 - step2) + U

Vs = mu1 / q_real
Vd = mu2 / q_real

print("f(E+U)")
print(f"{Vs=} V")
print(f"{Vd=} V\n")

# q4bii
step1 = -0.25
step2 = 0.25
mu1 = 0 - step1
mu2 = 0 - step2

Vs = mu1 / q_real
Vd = mu2 / q_real

print("f(E)")
print(f"{Vs=} V")
print(f"{Vd=} V")
