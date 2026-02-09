import matplotlib.pyplot as plt
import numpy as np

# Physical constants in MKS units

hbar = 1.054e-34
q = 1.602e-19
epsilon_0 = 8.854e-12
epsilon_r = 4
mstar = 0.25 * 9.11e-31

# MOSFET dimensions in meters

W = 1.0e-6
L = 10.0e-9
tox = 1.5e-9

# Capacitances and capacitance parameters

CG = epsilon_r * epsilon_0 * W * L / tox
CS = 0.05 * CG
CD = 0.05 * CG
CE = CG + CS + CD
alpha_G = CG / CE
alpha_D = CD / CE
alpha_S = 1 - alpha_G - alpha_D

# Energy parameters in eV

kBT = 0.025
U0 = q / CE

# Energy grid in eV, from -1 eV to 1 eV

NE = 501
E = np.linspace(-1, 1, NE)
dE = E[1] - E[0]

# Escape velocity [m/s] and gamma values [eV]

vR = 1e5
gamma_1 = hbar * vR / (q * L)
gamma_2 = gamma_1
gamma = gamma_1 + gamma_2

# Step-like density of states, stepping from 0 to a finite value at an energy of
# 0 eV

D0 = mstar * q * W * L / (np.pi * hbar * hbar)
D = D0 * np.concatenate((np.zeros(251), np.ones(250)))

# Equilibrium Fermi level in eV

mu = -0.2

# Reference number of channel electrons

f0 = 1 / (1 + np.exp((E - mu) / kBT))
N0 = dE * np.sum(D * f0)

# Voltage values to consider for the final plots

NV = 61
VV = np.linspace(0, 0.6, NV)

# Number of electrons and current values to be calculated

N = np.zeros_like(VV)
ID = np.zeros_like(VV)

# Loop over voltage values and compute number of electrons and current for each
# voltage value in a self-consistent manner

for VG in [0.25, 0.5]:
    for count in range(0, NV):
        # Set terminal voltages

        VD = VV[count]
        VS = 0

        # Values of mu1 and mu2; notice that the usual factor of q multiplying the
        # voltages is omitted, because in this code, energy is in eV

        mu1 = mu - VS
        mu2 = mu - VD

        # Value of Laplace potential in eV

        UL = -(alpha_G * VG) - (alpha_D * VD) - (alpha_S * VS)

        # Initial value of Poisson part in eV

        UP = 0

        # Iterate until self-consistent potential is achieved by monitoring the
        # Poisson part (the Laplace part does not change)

        dUP = 1
        while dUP > 1e-6:
            # Compute source and drain Fermi functions

            f1 = 1 / (1 + np.exp((E + UL + UP - mu1) / kBT))
            f2 = 1 / (1 + np.exp((E + UL + UP - mu2) / kBT))

            # Compute number of channel electrons

            N[count] = dE * np.sum(
                ((gamma_1 / gamma) * f1 + (gamma_2 / gamma) * f2) * D
            )

            # Update Poisson part of self-consistent potential

            UPnew = U0 * (N[count] - N0)
            dUP = abs(UP - UPnew)
            UP = UP + 0.1 * (UPnew - UP)

        # Compute the current in A after the self-consistent potential has been
        # achieved; notice the extra factor of q preceding the equation, which is
        # needed since the gammas are in eV

        ID[count] = (
            q * (q / hbar) * (gamma_1 * gamma_2) / (gamma) * dE * np.sum((f1 - f2) * D)
        )

        if VG == 0.5:
            if VD == 0.0:
                plt.figure(2, figsize=(8, 6))

                plt.subplot(2, 3, 1)
                plt.plot(f1, E, "k-")
                plt.xlim([-0.1, 1.1])
                plt.ylim([-1, 1])
                plt.xlabel("f1(E+U)")
                plt.ylabel("ENERGY  [eV]")
                plt.title("VD = 0.0 V")

                plt.subplot(2, 3, 2)
                plt.plot(D / 1e4, E, "k-")
                plt.xlim([-0.1, 1.1])
                plt.ylim([-1, 1])
                plt.xlabel("D(E)/1E4")
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
                plt.plot(f1 - f2, E, "b--", D / 1e4, E, "k-")
                plt.xlim([-0.1, 1.1])
                plt.ylim([-1, 1])
                plt.xlabel("f1(E+U)-f2(E+U), D(E)/1E4")
                plt.ylabel("ENERGY  [eV]")
                plt.title("VD = 0.0 V")

                plt.subplots_adjust(wspace=0.5, hspace=0.4)

            elif VD == 0.05:
                plt.figure(3, figsize=(8, 6))

                plt.subplot(2, 3, 1)
                plt.plot(f1, E, "k-")
                plt.xlim([-0.1, 1.1])
                plt.ylim([-1, 1])
                plt.xlabel("f1(E+U)")
                plt.ylabel("ENERGY  [eV]")
                plt.title("VD = 0.05 V")

                plt.subplot(2, 3, 2)
                plt.plot(D / 1e4, E, "k-")
                plt.xlim([-0.1, 1.1])
                plt.ylim([-1, 1])
                plt.xlabel("D(E)/1E4")
                plt.ylabel("ENERGY  [eV]")
                plt.title("VD = 0.05 V")

                plt.subplot(2, 3, 3)
                plt.plot(f2, E, "k-")
                plt.xlim([-0.1, 1.1])
                plt.ylim([-1, 1])
                plt.xlabel("f2(E+U)")
                plt.ylabel("ENERGY  [eV]")
                plt.title("VD = 0.05 V")

                plt.subplot(2, 3, 5)
                plt.plot(f1 - f2, E, "b--", D / 1e4, E, "k-")
                plt.xlim([-0.1, 1.1])
                plt.ylim([-1, 1])
                plt.xlabel("f1(E+U)-f2(E+U), D(E)/1E4")
                plt.ylabel("ENERGY  [eV]")
                plt.title("VD = 0.05 V")

                plt.subplots_adjust(wspace=0.5, hspace=0.4)

            elif VD == 0.1:
                plt.figure(4, figsize=(8, 6))

                plt.subplot(2, 3, 1)
                plt.plot(f1, E, "k-")
                plt.xlim([-0.1, 1.1])
                plt.ylim([-1, 1])
                plt.xlabel("f1(E+U)")
                plt.ylabel("ENERGY  [eV]")
                plt.title("VD = 0.1 V")

                plt.subplot(2, 3, 2)
                plt.plot(D / 1e4, E, "k-")
                plt.xlim([-0.1, 1.1])
                plt.ylim([-1, 1])
                plt.xlabel("D(E)/1E4")
                plt.ylabel("ENERGY  [eV]")
                plt.title("VD = 0.1 V")

                plt.subplot(2, 3, 3)
                plt.plot(f2, E, "k-")
                plt.xlim([-0.1, 1.1])
                plt.ylim([-1, 1])
                plt.xlabel("f2(E+U)")
                plt.ylabel("ENERGY  [eV]")
                plt.title("VD = 0.1 V")

                plt.subplot(2, 3, 5)
                plt.plot(f1 - f2, E, "b--", D / 1e4, E, "k-")
                plt.xlim([-0.1, 1.1])
                plt.ylim([-1, 1])
                plt.xlabel("f1(E+U)-f2(E+U), D(E)/1E4")
                plt.ylabel("ENERGY  [eV]")
                plt.title("VD = 0.1 V")

                plt.subplots_adjust(wspace=0.5, hspace=0.4)

            elif VD == 0.2:
                plt.figure(5, figsize=(8, 6))

                plt.subplot(2, 3, 1)
                plt.plot(f1, E, "k-")
                plt.xlim([-0.1, 1.1])
                plt.ylim([-1, 1])
                plt.xlabel("f1(E+U)")
                plt.ylabel("ENERGY  [eV]")
                plt.title("VD = 0.2 V")

                plt.subplot(2, 3, 2)
                plt.plot(D / 1e4, E, "k-")
                plt.xlim([-0.1, 1.1])
                plt.ylim([-1, 1])
                plt.xlabel("D(E)/1E4")
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
                plt.plot(f1 - f2, E, "b--", D / 1e4, E, "k-")
                plt.xlim([-0.1, 1.1])
                plt.ylim([-1, 1])
                plt.xlabel("f1(E+U)-f2(E+U), D(E)/1E4")
                plt.ylabel("ENERGY  [eV]")
                plt.title("VD = 0.2 V")

                plt.subplots_adjust(wspace=0.5, hspace=0.4)

            elif VD == 0.3:
                plt.figure(6, figsize=(8, 6))

                plt.subplot(2, 3, 1)
                plt.plot(f1, E, "k-")
                plt.xlim([-0.1, 1.1])
                plt.ylim([-1, 1])
                plt.xlabel("f1(E+U)")
                plt.ylabel("ENERGY  [eV]")
                plt.title("VD = 0.3 V")

                plt.subplot(2, 3, 2)
                plt.plot(D / 1e4, E, "k-")
                plt.xlim([-0.1, 1.1])
                plt.ylim([-1, 1])
                plt.xlabel("D(E)/1E4")
                plt.ylabel("ENERGY  [eV]")
                plt.title("VD = 0.3 V")

                plt.subplot(2, 3, 3)
                plt.plot(f2, E, "k-")
                plt.xlim([-0.1, 1.1])
                plt.ylim([-1, 1])
                plt.xlabel("f2(E+U)")
                plt.ylabel("ENERGY  [eV]")
                plt.title("VD = 0.3 V")

                plt.subplot(2, 3, 5)
                plt.plot(f1 - f2, E, "b--", D / 1e4, E, "k-")
                plt.xlim([-0.1, 1.1])
                plt.ylim([-1, 1])
                plt.xlabel("f1(E+U)-f2(E+U), D(E)/1E4")
                plt.ylabel("ENERGY  [eV]")
                plt.title("VD = 0.3 V")

                plt.subplots_adjust(wspace=0.5, hspace=0.4)

    plt.figure(1)
    plt.plot(VV, ID, "k-")

plt.figure(1)
plt.grid(color="grey", linestyle=":")
plt.xlabel("DRAIN VOLTAGE  [V]")
plt.ylabel("CURRENT  [A]")
plt.gca().get_yaxis().get_major_formatter().set_powerlimits((0, 0))

plt.show()
