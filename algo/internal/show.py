# pylint: disable=missing-module-docstring
# pylint: disable=invalid-name

import matplotlib.pyplot as plt

from algo.types import Algorithm, Alias, Map, Operation, Plot


LS = ['-', '--', '-.', ':']
LW = list(range(1, 4))


# pylint: disable=too-many-locals
def show_analysis(plots: Map[Operation, Map[Alias, Map[Algorithm, Plot]]]) ->\
        None:
    """
        Shows a figure collecting all of the plot data in a single place
    """

    nrows = len(plots)
    ncols = max(map(len, plots.values()))

    fig, axs = plt.subplots(nrows, ncols, squeeze=False)

    for i, (operation, plots_by_alias) in enumerate(plots.items()):
        for j, (alias, plots_by_algorithm) in enumerate(plots_by_alias.items()):
            ax = axs[i, j]

            ax.set_ylabel(f'{operation[0].value} {operation[1].value}')
            ax.set_xlabel(alias)
            ax.grid(True)
            ax.label_outer()
            ax.ticklabel_format(axis='both', style='sci', scilimits=(0, 0))

            for k, (algorithm, plot) in enumerate(plots_by_algorithm.items()):
                axs[i, j].plot(plot[0], plot[1], alpha=0.5,
                               linewidth=LW[k % len(LW)],
                               linestyle=LS[k % len(LS)],
                               label=algorithm.__name__)

    # TODO: show complexity

    handles, labels = ax.get_legend_handles_labels()
    fig.legend(handles, labels, loc='upper center')
    plt.show()
