import numpy as np
import pyabf
import matplotlib.pyplot as plt

def get_protocol(files):
    protocols = []
    for f in files:
        rec = pyabf.ABF(f)
        protocols.append(rec.protocol)
    return protocols

def files_from_protocol(prt_name,files):
    protocols = get_protocol(files)
    prt_file = []
    for i,prt in enumerate(protocols):
        if (prt_name in prt):
            prt_file.append(files[i])
    return prt_file

def plot_swps(file,legend=False):
    rec = pyabf.ABF(file)
    prt = rec.protocol
    fig,ax = plt.subplots(2,sharex=True)
    ax[0].set_title(prt)
    for swpNB in rec.sweepList:
        rec.setSweep(swpNB)
        ax[0].plot(rec.sweepX,rec.sweepY)
        ax[1].plot(rec.sweepX,rec.sweepC,label=f"sweep:{swpNB}")
    # labels and legends
    ax[1].set_xlabel(rec.sweepLabelX)
    ax[0].set_ylabel(rec.sweepLabelY)
    ax[1].set_ylabel(rec.sweepLabelC)
    ax[0].spines['bottom'].set_visible(False)
    # ax[0].set_xticks([])
    for i in range(2):
        ax[i].spines['right'].set_visible(False)
        ax[i].spines['top'].set_visible(False)
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

def swp_window(swps,start,end,sr,channel=0):
    i_start = int(start * sr)
    i_end = int(end * sr)
    return swps[:,channel,i_start:i_end]
