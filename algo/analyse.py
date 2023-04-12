import copy

import matplotlib.pyplot as plt

from algo.ctx import Context


ALPHA = 0.5
LS = ['-', '--', '-.', ':']


def analyse(algorithms, inputs, ops) -> None:
    x = [len(input) for input in inputs]

    for algorithm in algorithms:
        ctxs = []
        for input in inputs:
            ctx = Context()
            algorithm(copy.deepcopy(input), ctx=ctx)
            ctxs.append(ctx)

        for i, op in enumerate(ops):
            y = [ctx.ops[op] for ctx in ctxs]

            plt.plot(
                x, y, label=f'{algorithm.__name__} {op.name}', alpha=ALPHA, ls=LS[i % len(LS)])

    plt.grid(True)
    plt.legend()
    plt.show()
