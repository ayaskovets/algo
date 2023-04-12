from algo.ctx import Context
from algo.ops import Op


def selection_sort(input, ctx: Context = None):
    n = len(input)

    for i in range(n):
        min_j = i
        for j in range(i + 1, n):
            if ctx:
                ctx.ops[Op.COMPARISONS] += 1
            if input[min_j] > input[j]:
                min_j = j
        if ctx:
            ctx.ops[Op.SWAPS] += 1
        input[min_j], input[i] = input[i], input[min_j]

    return input
