"""
    Module containing the analyse function to analyse and display
    computational complexity of algorithms
"""

import collections

from algo.internal.log import print_info, print_ok, progress
from algo.internal.run import run_algorithm
from algo.internal.show import show_analysis


def analyse(algorithms: list, inputs: list, weights: list[tuple],
            operations: list[tuple]) -> None:
    """
        Arguments:
          - algorithms: list of functions each taking one input value of
                arbitrary type and return an output of arbitrary type

          - inputs: list of inputs to run the algorithms on

          - weights: list of tuples(function, alias), where function is a
                callable taking a single input from inputs and returning
                the weight of this input, (for example in the context of
                sorting function weight of the sorted list is its length) and
                alias is a name for this function to display on the analysis
                graph

          - operations: list of tuples()

        Returns:
          - None
    """

    ctxs_by_algorithm = collections.defaultdict(list)

    for algorithm in algorithms:
        print_info(f'RUN ({algorithm.__name__}) [{len(inputs)}]: ',
                   end='', flush=True)

        for inp in progress(inputs):
            ctx = run_algorithm(algorithm, inp, weights)
            ctxs_by_algorithm[algorithm].append(ctx)

        print_ok(f'\nDONE ({algorithm.__name__}) [{len(inputs)}]')

    show_analysis(ctxs_by_algorithm, weights, operations)
