import os.path
import sys

import matplotlib.pyplot as plt
import numpy as np

# Physical constants in MKS units

hbar = 1.054e-34
q = 1.602e-19

# Energy parameters in eV; included are the single-electron charging
# energy U0; the kBT product; the equilibrium Fermi level mu; and the
# energy levels cal_E1 and cal_E2, where "cal_E" is short-form for "calligraphic E"

# Please especially note that ALL ENERGY VARIABLES IN THIS CODE
# ARE IN eV (NOT joules); the equations from class must be adjusted
# accordingly, multiplying or dividing appropriate terms by a factor of q

# YOU MUST ENTER THE APPROPRIATE VALUES OF cal_E1 and cal_E2

U0 = 0.025
kBT = 0.025
mu = 0
cal_E1 = 0.14395
cal_E2 = 0.33185

# Capacitance parameters

alpha_G = 0.5
alpha_D = 0.5
alpha_S = 1 - alpha_G - alpha_D

# Energy grid in eV, from -1 eV to 1 eV

NE = 501
E = np.linspace(-1, 1, NE)
dE = E[1] - E[0]

# Coupling coefficients, which are now grids over E, with
# gamma_1 equal to 0.005 eV for E > 0, and 0 for E <= 0, and
# with gamma_2 equal to 0.005 eV for all E; the 1e-6
# term is included to avoid divide-by-zero errors

gamma_1 = 0.005 * (E + abs(E)) / (E + E + 1e-6)
gamma_2 = 0.005 * np.ones(NE)
gamma = gamma_1 + gamma_2

# Reference number of electrons in the channel, assumed to be zero in
# this code

N0 = 0

# Voltage values to consider for the final plots

NV = 121
VV = np.linspace(-0.4, 0.8, NV)
dV = VV[1] - VV[0]

# Initialized number of electrons and current

N = np.zeros_like(VV)
I = np.zeros_like(VV)

# Loop over voltage values and compute number of electrons and current
# for each voltage value in a self-consistent manner

for count in range(0, NV):
    # Set terminal voltages

    VG = 0
    VD = VV[count]
    VS = 0

    # Values of mu1 and mu2; notice that the usual factor of q multiplying
    # the voltages is omitted, because in this code, energy is in eV

    mu1 = mu - VS
    mu2 = mu - VD

    # Compute source and drain Fermi functions

    f1 = 1 / (1 + np.exp((E - mu1) / kBT))
    f2 = 1 / (1 + np.exp((E - mu2) / kBT))

    # Value of Laplace potential in eV

    UL = -(alpha_G * VG) - (alpha_D * VD) - (alpha_S * VS)

    # Initial value of Poisson part in eV

    UP = 0

    # Iterate until self-consistent potential is achieved by monitoring
    # the Poisson part (the Laplace part does not change)

    dUP = 1
    while dUP > 1e-6:
        # Lorentzian SHIFTED density of states for levels 1 and 2,
        # each normalized so that its integral is unity

        D1 = (0.01 / (2 * np.pi)) / ((E - (UL + UP) - cal_E1) ** 2 + (0.01 / 2) ** 2)
        D1 = D1 / (dE * np.sum(D1))

        D2 = (0.01 / (2 * np.pi)) / ((E - (UL + UP) - cal_E2) ** 2 + (0.01 / 2) ** 2)
        D2 = D2 / (dE * np.sum(D2))

        # Total density of states

        D = D1 + D2

        # Compute number of channel electrons

        N[count] = dE * np.sum(((gamma_1 / gamma) * f1 + (gamma_2 / gamma) * f2) * D)

        # Newly calculated Poisson part of self-consistent potential

        UPnew = U0 * (N[count] - N0)

        # Change in Poisson part between iterations

        dUP = abs(UP - UPnew)

        # New guess for next iteration, found by adding a fraction of the
        # difference between iterations to the old guess

        UP = UP + 0.1 * (UPnew - UP)

    # Compute the current in A after the self-consistent potential
    # has been achieved; notice the extra factor of q preceding the
    # equation, which is needed since the gammas are in eV

    I[count] = q * (q / hbar) * dE * np.sum((f1 - f2) * D * gamma_1 * gamma_2 / gamma)

    # Gets the path of the subplot file in the current directory and then executes the subplot file

    path = os.path.join(os.path.dirname(sys.argv[0]), "problem_4_part_b_i_subplots.py")
    exec(open(path).read())


# Plotting commands, including lines to modify the linewidth
# and Fontsize, just to make the plots look nicer; you don't
# need to worry about how these work

plt.figure(1)
plt.plot(VV, N, "k")
plt.grid(color="grey", linestyle=":")
plt.xlabel("DRAIN VOLTAGE  [V]")
plt.ylabel("NUMBER OF ELECTRONS")

plt.figure(2)
plt.plot(VV, I, "k")
plt.grid(color="grey", linestyle=":")
plt.xlabel("DRAIN VOLTAGE  [V]")
plt.ylabel("CURRENT  [A]")

plt.show()
