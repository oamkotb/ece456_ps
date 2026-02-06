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
    mu1 = mu - VS  # [eV] chemical potential of contact 1 (source-side)
    mu2 = mu - VD  # [eV] chemical potential of contact 2 (drain-side)

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
    I[count] = q * (q / hbar) * (gamma_1 * gamma_2) / gamma * dE * np.sum((f1 - f2) * D)

    # Code to create the required plots for Problem Set 1, Problem 1(c)

    # If you've used the same variable names as in the sample code, then you
    # should be able to simply insert this into the appropriate spot in your
    # own code; otherwise, you'll have to modify this accordingly, which
    # should be easy to do---if disaster strikes and it doesn't work, then
    # please ask for help

    # Python code cares about how the code is indented. Make sure the code being
    # inserted is indented consistently with respect to the code it is being
    # inserted into.

    # The "if" statement is used to choose VD values closest to the required
    # values of 0.0, 0.2, 0.5, 0.8, and 1.0 V, and you don't need to worry
    # about how this works

    if abs(VD - 0.0) <= dV / 2:
        plt.figure(3, figsize=(8, 6))

        plt.subplot(2, 3, 1)
        plt.plot(f1, E, "k-")
        plt.xlim([-0.1, 1.1])
        plt.ylim([-1, 1])
        plt.xlabel("f1(E+U)")
        plt.ylabel("ENERGY  [eV]")
        plt.title("VD = 0.0 V")

        plt.subplot(2, 3, 2)
        plt.plot(D / 100, E, "k-")
        plt.xlim([-0.1, 1.1])
        plt.ylim([-1, 1])
        plt.xlabel("D(E)/100")
        plt.ylabel("ENERGY  [eV]")
        plt.title("VD = 0.0 V")

        plt.subplot(2, 3, 3)
        plt.plot(f2, E, "k-")
        plt.xlim([-0.1, 1.1])
        plt.ylim([-1, 1])
        plt.xlabel("f2(E+U)")
        plt.ylabel("ENERGY  [eV]")
        plt.title("VD = 0.0 V")

        plt.subplot(2, 3, 5)
        plt.plot(f1 - f2, E, "b--", D / 100, E, "k-")
        plt.xlim([-0.1, 1.1])
        plt.ylim([-1, 1])
        plt.xlabel("f1(E+U)-f2(E+U), D(E)/100")
        plt.ylabel("ENERGY  [eV]")
        plt.title("VD = 0.0 V")

        plt.subplots_adjust(wspace=0.5, hspace=0.4)

    elif abs(VD - 0.2) <= dV / 2:
        plt.figure(4, figsize=(8, 6))

        plt.subplot(2, 3, 1)
        plt.plot(f1, E, "k-")
        plt.xlim([-0.1, 1.1])
        plt.ylim([-1, 1])
        plt.xlabel("f1(E+U)")
        plt.ylabel("ENERGY  [eV]")
        plt.title("VD = 0.2 V")

        plt.subplot(2, 3, 2)
        plt.plot(D / 100, E, "k-")
        plt.xlim([-0.1, 1.1])
        plt.ylim([-1, 1])
        plt.xlabel("D(E)/100")
        plt.ylabel("ENERGY  [eV]")
        plt.title("VD = 0.2 V")

        plt.subplot(2, 3, 3)
        plt.plot(f2, E, "k-")
        plt.xlim([-0.1, 1.1])
        plt.ylim([-1, 1])
        plt.xlabel("f2(E+U)")
        plt.ylabel("ENERGY  [eV]")
        plt.title("VD = 0.2 V")

        plt.subplot(2, 3, 5)
        plt.plot(f1 - f2, E, "b--", D / 100, E, "k-")
        plt.xlim([-0.1, 1.1])
        plt.ylim([-1, 1])
        plt.xlabel("f1(E+U)-f2(E+U), D(E)/100")
        plt.ylabel("ENERGY  [eV]")
        plt.title("VD = 0.2 V")

        plt.subplots_adjust(wspace=0.5, hspace=0.4)

    elif abs(VD - 0.5) <= dV / 2:
        plt.figure(5, figsize=(8, 6))

        plt.subplot(2, 3, 1)
        plt.plot(f1, E, "k-")
        plt.xlim([-0.1, 1.1])
        plt.ylim([-1, 1])
        plt.xlabel("f1(E+U)")
        plt.ylabel("ENERGY  [eV]")
        plt.title("VD = 0.5 V")

        plt.subplot(2, 3, 2)
        plt.plot(D / 100, E, "k-")
        plt.xlim([-0.1, 1.1])
        plt.ylim([-1, 1])
        plt.xlabel("D(E)/100")
        plt.ylabel("ENERGY  [eV]")
        plt.title("VD = 0.5 V")

        plt.subplot(2, 3, 3)
        plt.plot(f2, E, "k-")
        plt.xlim([-0.1, 1.1])
        plt.ylim([-1, 1])
        plt.xlabel("f2(E+U)")
        plt.ylabel("ENERGY  [eV]")
        plt.title("VD = 0.5 V")

        plt.subplot(2, 3, 5)
        plt.plot(f1 - f2, E, "b--", D / 100, E, "k-")
        plt.xlim([-0.1, 1.1])
        plt.ylim([-1, 1])
        plt.xlabel("f1(E+U)-f2(E+U), D(E)/100")
        plt.ylabel("ENERGY  [eV]")
        plt.title("VD = 0.5 V")

        plt.subplots_adjust(wspace=0.5, hspace=0.4)

    elif abs(VD - 0.8) <= dV / 2:
        plt.figure(6, figsize=(8, 6))

        plt.subplot(2, 3, 1)
        plt.plot(f1, E, "k-")
        plt.xlim([-0.1, 1.1])
        plt.ylim([-1, 1])
        plt.xlabel("f1(E+U)")
        plt.ylabel("ENERGY  [eV]")
        plt.title("VD = 0.8 V")

        plt.subplot(2, 3, 2)
        plt.plot(D / 100, E, "k-")
        plt.xlim([-0.1, 1.1])
        plt.ylim([-1, 1])
        plt.xlabel("D(E)/100")
        plt.ylabel("ENERGY  [eV]")
        plt.title("VD = 0.8 V")

        plt.subplot(2, 3, 3)
        plt.plot(f2, E, "k-")
        plt.xlim([-0.1, 1.1])
        plt.ylim([-1, 1])
        plt.xlabel("f2(E+U)")
        plt.ylabel("ENERGY  [eV]")
        plt.title("VD = 0.8 V")

        plt.subplot(2, 3, 5)
        plt.plot(f1 - f2, E, "b--", D / 100, E, "k-")
        plt.xlim([-0.1, 1.1])
        plt.ylim([-1, 1])
        plt.xlabel("f1(E+U)-f2(E+U), D(E)/100")
        plt.ylabel("ENERGY  [eV]")
        plt.title("VD = 0.8 V")

        plt.subplots_adjust(wspace=0.5, hspace=0.4)

    elif abs(VD - 1.0) <= dV / 2:
        plt.figure(7, figsize=(8, 6))

        plt.subplot(2, 3, 1)
        plt.plot(f1, E, "k-")
        plt.xlim([-0.1, 1.1])
        plt.ylim([-1, 1])
        plt.xlabel("f1(E+U)")
        plt.ylabel("ENERGY  [eV]")
        plt.title("VD = 1.0 V")

        plt.subplot(2, 3, 2)
        plt.plot(D / 100, E, "k-")
        plt.xlim([-0.1, 1.1])
        plt.ylim([-1, 1])
        plt.xlabel("D(E)/100")
        plt.ylabel("ENERGY  [eV]")
        plt.title("VD = 1.0 V")

        plt.subplot(2, 3, 3)
        plt.plot(f2, E, "k-")
        plt.xlim([-0.1, 1.1])
        plt.ylim([-1, 1])
        plt.xlabel("f2(E+U)")
        plt.ylabel("ENERGY  [eV]")
        plt.title("VD = 1.0 V")

        plt.subplot(2, 3, 5)
        plt.plot(f1 - f2, E, "b--", D / 100, E, "k-")
        plt.xlim([-0.1, 1.1])
        plt.ylim([-1, 1])
        plt.xlabel("f1(E+U)-f2(E+U), D(E)/100")
        plt.ylabel("ENERGY  [eV]")
        plt.title("VD = 1.0 V")

        plt.subplots_adjust(wspace=0.5, hspace=0.4)


# Plot results
plt.figure(figsize=(8, 6))

# First subplot: Number of Electrons vs Drain Voltage
plt.subplot(2, 1, 1)
plt.plot(VV, N, color="b", linestyle="-", linewidth=2)  # Blue solid line
plt.title("Number of Electrons vs Drain Voltage", fontsize=14)
plt.xlabel("Drain Voltage [V]", fontsize=12)
plt.ylabel("Number of Electrons", fontsize=12)
plt.grid(True, which="both", linestyle="--", linewidth=0.5)
plt.tick_params(axis="both", labelsize=10)

# Second subplot: Current vs Drain Voltage
plt.subplot(2, 1, 2)
plt.plot(VV, I, color="r", linestyle="-", linewidth=2)  # Red solid line
plt.title("Current vs Drain Voltage", fontsize=14)
plt.xlabel("Drain Voltage [V]", fontsize=12)
plt.ylabel("Current [A]", fontsize=12)
plt.grid(True, which="both", linestyle="--", linewidth=0.5)
plt.tick_params(axis="both", labelsize=10)

plt.tight_layout()
plt.show()
