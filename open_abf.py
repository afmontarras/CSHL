import numpy as np
import pyabf
import matplotlib.pyplot as plt

def plot_swps(file,legend=False):
    rec = pyabf.ABF(file)
    fig,ax = plt.subplots(2,sharex=True)
    for swpNB in rec.sweepList:
        rec.setSweep(swpNB)
        ax[0].plot(rec.sweepX,rec.sweepY)
        ax[1].plot(rec.sweepX,rec.sweepC,label=f"sweep:{swpNB}")
    # labels and legends
    ax[1].set_xlabel(rec.sweepLabelX)
    ax[0].set_ylabel(rec.sweepLabelY)
    ax[1].set_ylabel(rec.sweepLabelC)
    if legend:
        ax[1].legend(loc="right")
    fig.tight_layout()

def get_sweeps(f):
    rec = pyabf.ABF(f)
    swps = []
    for swpNB in rec.sweepList:
        rec.setSweep(swpNB)
        swps.append((rec.sweepY,rec.sweepC))
    swps = np.array(swps)
    swp_time = rec.sweepX
    dt = swp_time[1] 
    return swps, swp_time, 1/dt

