import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import trapz, simps

def integral(xvg, txt):
    pmf = pd.read_csv(xvg, header = None, delim_whitespace= True)
    df = pd.DataFrame({0: [pmf[0][0]], 1: [pmf[1][0]], 2: [pmf[2][0]]})
    df = df.append(pmf)
    df = df.reset_index(drop = True)
    pmf = df.copy(deep = True)
    pmf = pmf[pmf[0] <= 4.000000]
    pmf = pmf.append({'0': 4.000000, '1': 0.097642, '2': 0.014463}, ignore_index=True)
    pmf[3] = np.exp(pmf[1]/2.478)
    diff = pd.read_csv(txt, header = None, delim_whitespace= True)
    diffusion_interpl = np.interp(pmf[0], diff[0], diff[1])
    pmf[0] = pmf[0] * 1 * 10 ** -7
    diff = pd.DataFrame({0: pmf[0], 1: diffusion_interpl })
    integrand = pmf[3]/diff[1]
    return 1/trapz(integrand, pmf[0])
