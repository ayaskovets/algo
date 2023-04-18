from algo.ctx import Context
from algo.ops import Op


def bubble_sort(input, ctx: Context):
    n = len(input)

    for i in range(n):
        for j in range(i + 1, n):
            ctx.account(Op.COMPARISONS)
            if input[j] < input[i]:
                ctx.account(Op.SWAPS)
                input[i], input[j] = input[j], input[i]

    return input
