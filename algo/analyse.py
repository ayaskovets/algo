import copy
import time

import matplotlib.pyplot as plt

from algo.ctx import Context
from algo.ops import Op


ALPHA = 0.5
LS = ['-', '--', '-.', ':']


def analyse(algorithms, inputs, ops) -> None:
    x = [len(input) for input in inputs]

    for algorithm in algorithms:
        ctxs = []
        for input in inputs:
            ctx = Context()

            start = time.time()
            algorithm(copy.deepcopy(input), ctx=ctx)
            end = time.time()

            ctx.account(Op.RUNTIME, end - start)

            ctxs.append(ctx)

        for i, op in enumerate(ops):
            y = [ctx.get(op) for ctx in ctxs]

            plt.plot(
                x, y, label=f'{algorithm.__name__} {op.name}', alpha=ALPHA, ls=LS[i % len(LS)])

    plt.grid(True)
    plt.legend()
    plt.show()
