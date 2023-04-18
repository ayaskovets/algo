from algo.ctx import Context
from algo.ops import Op


def merge_sort(input, ctx: Context):
    n = len(input)

    ctx.account(Op.COMPARISONS)
    if n < 2:
        return input

    m = n // 2
    l, r = input[:m], input[m:]

    merge_sort(l, ctx=ctx)
    merge_sort(r, ctx=ctx)

    i = j = 0
    for k in range(n):
        ctx.account(Op.COMPARISONS)
        if i >= len(l):
            input[k] = r[j]
            j += 1
            continue

        ctx.account(Op.COMPARISONS)
        if j >= len(r):
            input[k] = l[i]
            i += 1
            continue

        ctx.account(Op.COMPARISONS)
        if l[i] < r[j]:
            input[k] = l[i]
            i += 1
        else:
            input[k] = r[j]
            j += 1

    return input
