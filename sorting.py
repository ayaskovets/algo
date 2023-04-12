import random

from algo.analyse import analyse
from algo.test import test
from algo.ops import Op

from sorting.bubble_sort import bubble_sort
from sorting.selection_sort import selection_sort
from sorting.merge_sort import merge_sort

# list of array sizes with shuffled items [0..size)
sizes = list(range(200))

# list of algorithms to test and analyse
algorithms = [bubble_sort, selection_sort, merge_sort]

# list of inputs
inputs = [random.sample(range(-size, size), size) for size in sizes]

# predicate for sorting functions
predicate = lambda _, o: o == sorted(o)

# list of operations to analyse
ops = [Op.SWAPS, Op.COMPARISONS]

test(algorithms, inputs, predicate)
analyse(algorithms, inputs, ops)
