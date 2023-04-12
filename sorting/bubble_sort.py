from algo.ctx import Context
from algo.ops import Op


def bubble_sort(input, ctx: Context = None):
    n = len(input)

    for i in range(n):
        for j in range(i + 1, n):
            if ctx:
                ctx.ops[Op.SWAPS] += 1
            if input[j] < input[i]:
                if ctx:
                    ctx.ops[Op.COMPARISONS] += 1
                input[i], input[j] = input[j], input[i]

    return input
