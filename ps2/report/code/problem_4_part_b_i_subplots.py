# If you've used the same variable names as in the sample code, then you
# should be able to simply insert this into the appropriate spot in your
# own code; otherwise, you'll have to modify this accordingly, which
# should be easy to do---if disaster strikes and it doesn't work, then
# please ask for help

# The "if" statement is used to choose VD values closest to the required
# values of 0.0, 0.2, 0.3, ..., 0.8 V, and you don't need to
# worry about how this works

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

elif abs(VD - 0.25) <= dV / 2:
    plt.figure(5, figsize=(8, 6))

    plt.subplot(2, 3, 1)
    plt.plot(f1, E, "k-")
    plt.xlim([-0.1, 1.1])
    plt.ylim([-1, 1])
    plt.xlabel("f1(E+U)")
    plt.ylabel("ENERGY  [eV]")
    plt.title("VD = 0.25 V")

    plt.subplot(2, 3, 2)
    plt.plot(D / 100, E, "k-")
    plt.xlim([-0.1, 1.1])
    plt.ylim([-1, 1])
    plt.xlabel("D(E)/100")
    plt.ylabel("ENERGY  [eV]")
    plt.title("VD = 0.25 V")

    plt.subplot(2, 3, 3)
    plt.plot(f2, E, "k-")
    plt.xlim([-0.1, 1.1])
    plt.ylim([-1, 1])
    plt.xlabel("f2(E+U)")
    plt.ylabel("ENERGY  [eV]")
    plt.title("VD = 0.25 V")

    plt.subplot(2, 3, 5)
    plt.plot(f1 - f2, E, "b--", D / 100, E, "k-")
    plt.xlim([-0.1, 1.1])
    plt.ylim([-1, 1])
    plt.xlabel("f1(E+U)-f2(E+U), D(E)/100")
    plt.ylabel("ENERGY  [eV]")
    plt.title("VD = 0.25 V")

    plt.subplots_adjust(wspace=0.5, hspace=0.4)

elif abs(VD - 0.3) <= dV / 2:
    plt.figure(6, figsize=(8, 6))

    plt.subplot(2, 3, 1)
    plt.plot(f1, E, "k-")
    plt.xlim([-0.1, 1.1])
    plt.ylim([-1, 1])
    plt.xlabel("f1(E+U)")
    plt.ylabel("ENERGY  [eV]")
    plt.title("VD = 0.3 V")

    plt.subplot(2, 3, 2)
    plt.plot(D / 100, E, "k-")
    plt.xlim([-0.1, 1.1])
    plt.ylim([-1, 1])
    plt.xlabel("D(E)/100")
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
    plt.plot(f1 - f2, E, "b--", D / 100, E, "k-")
    plt.xlim([-0.1, 1.1])
    plt.ylim([-1, 1])
    plt.xlabel("f1(E+U)-f2(E+U), D(E)/100")
    plt.ylabel("ENERGY  [eV]")
    plt.title("VD = 0.3 V")

    plt.subplots_adjust(wspace=0.5, hspace=0.4)

elif abs(VD - 0.4) <= dV / 2:
    plt.figure(7, figsize=(8, 6))

    plt.subplot(2, 3, 1)
    plt.plot(f1, E, "k-")
    plt.xlim([-0.1, 1.1])
    plt.ylim([-1, 1])
    plt.xlabel("f1(E+U)")
    plt.ylabel("ENERGY  [eV]")
    plt.title("VD = 0.4 V")

    plt.subplot(2, 3, 2)
    plt.plot(D / 100, E, "k-")
    plt.xlim([-0.1, 1.1])
    plt.ylim([-1, 1])
    plt.xlabel("D(E)/100")
    plt.ylabel("ENERGY  [eV]")
    plt.title("VD = 0.4 V")

    plt.subplot(2, 3, 3)
    plt.plot(f2, E, "k-")
    plt.xlim([-0.1, 1.1])
    plt.ylim([-1, 1])
    plt.xlabel("f2(E+U)")
    plt.ylabel("ENERGY  [eV]")
    plt.title("VD = 0.4 V")

    plt.subplot(2, 3, 5)
    plt.plot(f1 - f2, E, "b--", D / 100, E, "k-")
    plt.xlim([-0.1, 1.1])
    plt.ylim([-1, 1])
    plt.xlabel("f1(E+U)-f2(E+U), D(E)/100")
    plt.ylabel("ENERGY  [eV]")
    plt.title("VD = 0.4 V")

    plt.subplots_adjust(wspace=0.5, hspace=0.4)

elif abs(VD - 0.5) <= dV / 2:
    plt.figure(8, figsize=(8, 6))

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

elif abs(VD - 0.6) <= dV / 2:
    plt.figure(9, figsize=(8, 6))

    plt.subplot(2, 3, 1)
    plt.plot(f1, E, "k-")
    plt.xlim([-0.1, 1.1])
    plt.ylim([-1, 1])
    plt.xlabel("f1(E+U)")
    plt.ylabel("ENERGY  [eV]")
    plt.title("VD = 0.6 V")

    plt.subplot(2, 3, 2)
    plt.plot(D / 100, E, "k-")
    plt.xlim([-0.1, 1.1])
    plt.ylim([-1, 1])
    plt.xlabel("D(E)/100")
    plt.ylabel("ENERGY  [eV]")
    plt.title("VD = 0.6 V")

    plt.subplot(2, 3, 3)
    plt.plot(f2, E, "k-")
    plt.xlim([-0.1, 1.1])
    plt.ylim([-1, 1])
    plt.xlabel("f2(E+U)")
    plt.ylabel("ENERGY  [eV]")
    plt.title("VD = 0.6 V")

    plt.subplot(2, 3, 5)
    plt.plot(f1 - f2, E, "b--", D / 100, E, "k-")
    plt.xlim([-0.1, 1.1])
    plt.ylim([-1, 1])
    plt.xlabel("f1(E+U)-f2(E+U), D(E)/100")
    plt.ylabel("ENERGY  [eV]")
    plt.title("VD = 0.6 V")

    plt.subplots_adjust(wspace=0.5, hspace=0.4)

elif abs(VD - 0.65) <= dV / 2:
    plt.figure(10, figsize=(8, 6))

    plt.subplot(2, 3, 1)
    plt.plot(f1, E, "k-")
    plt.xlim([-0.1, 1.1])
    plt.ylim([-1, 1])
    plt.xlabel("f1(E+U)")
    plt.ylabel("ENERGY  [eV]")
    plt.title("VD = 0.65 V")

    plt.subplot(2, 3, 2)
    plt.plot(D / 100, E, "k-")
    plt.xlim([-0.1, 1.1])
    plt.ylim([-1, 1])
    plt.xlabel("D(E)/100")
    plt.ylabel("ENERGY  [eV]")
    plt.title("VD = 0.65 V")

    plt.subplot(2, 3, 3)
    plt.plot(f2, E, "k-")
    plt.xlim([-0.1, 1.1])
    plt.ylim([-1, 1])
    plt.xlabel("f2(E+U)")
    plt.ylabel("ENERGY  [eV]")
    plt.title("VD = 0.65 V")

    plt.subplot(2, 3, 5)
    plt.plot(f1 - f2, E, "b--", D / 100, E, "k-")
    plt.xlim([-0.1, 1.1])
    plt.ylim([-1, 1])
    plt.xlabel("f1(E+U)-f2(E+U), D(E)/100")
    plt.ylabel("ENERGY  [eV]")
    plt.title("VD = 0.65 V")

    plt.subplots_adjust(wspace=0.5, hspace=0.4)

elif abs(VD - 0.7) <= dV / 2:
    plt.figure(11, figsize=(8, 6))

    plt.subplot(2, 3, 1)
    plt.plot(f1, E, "k-")
    plt.xlim([-0.1, 1.1])
    plt.ylim([-1, 1])
    plt.xlabel("f1(E+U)")
    plt.ylabel("ENERGY  [eV]")
    plt.title("VD = 0.7 V")

    plt.subplot(2, 3, 2)
    plt.plot(D / 100, E, "k-")
    plt.xlim([-0.1, 1.1])
    plt.ylim([-1, 1])
    plt.xlabel("D(E)/100")
    plt.ylabel("ENERGY  [eV]")
    plt.title("VD = 0.7 V")

    plt.subplot(2, 3, 3)
    plt.plot(f2, E, "k-")
    plt.xlim([-0.1, 1.1])
    plt.ylim([-1, 1])
    plt.xlabel("f2(E+U)")
    plt.ylabel("ENERGY  [eV]")
    plt.title("VD = 0.7 V")

    plt.subplot(2, 3, 5)
    plt.plot(f1 - f2, E, "b--", D / 100, E, "k-")
    plt.xlim([-0.1, 1.1])
    plt.ylim([-1, 1])
    plt.xlabel("f1(E+U)-f2(E+U), D(E)/100")
    plt.ylabel("ENERGY  [eV]")
    plt.title("VD = 0.7 V")

    plt.subplots_adjust(wspace=0.5, hspace=0.4)

elif abs(VD - 0.8) <= dV / 2:
    plt.figure(12, figsize=(8, 6))

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
