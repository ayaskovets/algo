# pylint: disable=missing-module-docstring
# pylint: disable=invalid-name

import matplotlib.pyplot as plt

from algo.internal.complexity import Complexity, calculate_complexity

from algo.types import Algorithm, Alias, Map, Operation, Plot


LS = ['-', '--', '-.', ':']
LW = list(range(1, 4))


# pylint: disable=inconsistent-return-statements
def _serialize_complexity(complexity: Complexity, alias: Alias):
    if complexity == Complexity.N:
        return f'{alias}'

    if complexity == Complexity.N_2:
        return f'{alias}²'

    if complexity == Complexity.LOG_N:
        return f'log₂({alias})'

    if complexity == Complexity.N_LOG_N:
        return f'{alias}log₂({alias})'

    assert not 'implemented yet!'


# pylint: disable=too-many-locals
def show_analysis(plots: Map[Operation, Map[Alias, Map[Algorithm, Plot]]]) ->\
        None:
    """
        Shows a figure collecting all of the plot data in a single place
    """

    nrows = len(plots)
    ncols = max(map(len, plots.values()))

    fig, axs = plt.subplots(nrows, ncols, squeeze=False)
    algorithms = []

    for i, (operation, plots_by_alias) in enumerate(plots.items()):
        for j, (alias, plots_by_algorithm) in enumerate(plots_by_alias.items()):
            ax = axs[i, j]

            ax.set_ylabel(f'{operation[0].value} {operation[1].value}')
            ax.set_xlabel(alias)
            ax.grid(True)
            ax.label_outer()
            ax.ticklabel_format(axis='both', style='sci', scilimits=(0, 0))

            if not algorithms:
                algorithms = list(plots_by_algorithm.keys())

            for k, (_, plot) in enumerate(plots_by_algorithm.items()):
                complexity = calculate_complexity(plot)

                ax.plot(plot[0], plot[1], alpha=0.5, linewidth=LW[k % len(LW)],
                        linestyle=LS[k % len(LS)],
                        label=_serialize_complexity(complexity, alias))

    handles, _ = ax.get_legend_handles_labels()
    fig.legend(handles, [algorithm.__name__ for algorithm in algorithms],
               loc='upper center')
    plt.show()
