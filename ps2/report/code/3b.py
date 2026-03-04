# A simple PYTHON code to plot the momentum
# wave function for a particle in an escape-proof "box"

import matplotlib.pyplot as plt
import numpy as np

hbar = 1.054e-34
L = 101e-10

# Set up k' and p' axes

k_prime = np.linspace(-2 * np.pi / L, 2 * np.pi / L, 100)
dk_prime = k_prime[1] - k_prime[0]
p_prime = hbar * k_prime
dp_prime = p_prime[1] - p_prime[0]

# k1 and p1

k1 = np.pi / L
p1 = hbar * k1

# Fourier transform A(k')

A1 = 0.5 * np.sqrt(L / np.pi) * (np.sinc((k_prime + k1) * L / (2 * np.pi)))
A2 = 0.5 * np.sqrt(L / np.pi) * (np.sinc((k_prime - k1) * L / (2 * np.pi)))
A = A1 + A2
A_sum = np.sum(np.abs(A) ** 2) * dk_prime

# Momentum wave function Phi(p')

Phi1 = (
    0.5
    * np.sqrt(L / (np.pi * hbar))
    * (np.sinc((p_prime + p1) * L / (2 * np.pi * hbar)))
)
Phi2 = (
    0.5
    * np.sqrt(L / (np.pi * hbar))
    * (np.sinc((p_prime - p1) * L / (2 * np.pi * hbar)))
)
Phi = Phi1 + Phi2
Phi_sum = np.sum(np.abs(Phi) ** 2) * dp_prime

# Normalized p' axis for plotting purposes; the points of classical
# momenta occur when the variable pp_N is plus or minus unity

pp_N = p_prime / p1

plt.figure(1)
plt.plot(pp_N, Phi1, "kx")
plt.plot(pp_N, Phi2, "ko", markerfacecolor="none")
plt.plot(pp_N, Phi, "k--")

# --- NEW CODE FOR INTERSECTIONS ---
# The prefactor from your Phi equations determines the peak height
prefactor = 0.5 * np.sqrt(L / (np.pi * hbar))

# Plot the intersection of Phi2 and Phi at pp_N = 1
# Using f-strings to dynamically format the label with scientific notation (.2e)
plt.plot(
    1, prefactor, "ro", markersize=8, label=f"\u03a62 & \u03a6: (1.0, {prefactor:.2e})"
)

# Plot the intersection of Phi1 and Phi at pp_N = -1
plt.plot(
    -1,
    prefactor,
    "bs",
    markersize=8,
    label=f"\u03a61 & \u03a6: (-1.0, {prefactor:.2e})",
)
# ----------------------------------

plt.grid(color="grey", linestyle=":")
plt.xlabel("NORMALIZED MOMENTUM  [p'/p_1]")
plt.ylabel("WAVE FUNCTION  [sqrt(s / kg m)]")
plt.legend()

plt.figure(2)
plt.plot(pp_N, np.abs(Phi) ** 2, "k-")
plt.grid(color="grey", linestyle=":")
plt.xlabel("NORMALIZED MOMENTUM  [p'/p_1]")
plt.ylabel("PROBABILITY DENSITY  [s / kg m]")

plt.show()
