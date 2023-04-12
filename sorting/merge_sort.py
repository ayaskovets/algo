from algo.ctx import Context
from algo.ops import Op


def merge_sort(input, ctx: Context = None):
    n = len(input)

    if ctx:
        ctx.ops[Op.COMPARISONS] += 1
    if n < 2:
        return input

    m = n // 2
    l, r = input[:m], input[m:]

    merge_sort(l, ctx=ctx)
    merge_sort(r, ctx=ctx)

    i = j = 0
    for k in range(n):
        if i < len(l) and j < len(r):
            if ctx:
                ctx.ops[Op.COMPARISONS] += 3
            if l[i] < r[j]:
                input[k] = l[i]
                i += 1
            else:
                input[k] = r[j]
                j += 1
        elif i < len(l):
            if ctx:
                ctx.ops[Op.COMPARISONS] += 1
            input[k] = l[i]
            i += 1
        else:
            if ctx:
                ctx.ops[Op.COMPARISONS] += 1
            input[k] = r[j]
            j += 1

    return input
