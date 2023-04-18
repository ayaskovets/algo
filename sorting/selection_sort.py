from algo.ctx import Context
from algo.ops import Op


def selection_sort(input, ctx: Context):
    n = len(input)

    for i in range(n):
        min_j = i
        for j in range(i + 1, n):
            ctx.account(Op.COMPARISONS)
            if input[min_j] > input[j]:
                min_j = j
        ctx.account(Op.SWAPS)
        input[min_j], input[i] = input[i], input[min_j]

    return input
