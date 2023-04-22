import random

from algo.analyse import analyse
from algo.test import test
from algo.ops import Agg, Op

from sorting.bubble_sort import bubble_sort
from sorting.selection_sort import selection_sort
from sorting.merge_sort import merge_sort

if __name__ == '__main__':
    # list of algorithms to test and analyse
    algorithms = [
        bubble_sort,
        selection_sort,
        merge_sort
    ]

    # list of inputs
    inputs = [
        random.sample(range(-size, size), size)
        for size in list(range(0, 100)) * 3
    ]

    # predicate for sorting functions
    predicate = lambda output: output == sorted(output)

    # weight function for list
    weight = len

    # list of operations to analyse
    ops = [
        (Agg.AVERAGE, Op.COMPARISONS),
        (Agg.AVERAGE, Op.RUNTIME_MS),
    ]

    # test(algorithms, inputs, predicate)
    analyse(algorithms, inputs, weight, ops)
