def IV_style(ax,
            xcoord=(0.9, 0.4),
            ycoord=(0.45, 0.9)):
    ax.spines['left'].set_position('zero')
    ax.spines['bottom'].set_position('zero')
    ax.set_xlabel('V (mV)')
    ax.set_ylabel('I/Cm (pA/pF)')
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.xaxis.set_label_coords(xcoord[0], xcoord[1]) 
    ax.yaxis.set_label_coords(ycoord[0], ycoord[1])
    # Customize ticks to remove the 0 ticks and labels
    xticks = [tick for tick in ax.get_xticks() if tick != 0]
    yticks = [tick for tick in ax.get_yticks() if tick != 0]
    ax.set_xticks(xticks)
    ax.set_yticks(yticks)

