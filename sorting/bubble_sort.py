from algo.ops import Op

def bubble_sort(input, ctx):
    n = len(input)

    for i in range(n):
        for j in range(n):
            if ctx: ctx.ops[Op.SWAP] += 1
            if input[j] > input[i]:
                if ctx: ctx.ops[Op.COMPARISON] += 1
                input[i], input[j] = input[j], input[i]

    return input
