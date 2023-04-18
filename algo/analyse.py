import copy
import time

import matplotlib.pyplot as plt
import memory_profiler

from algo.ctx import Context
from algo.log import print_info, print_ok
from algo.ops import Op


ALPHA = 0.5
LS = ['-', '--', '-.', ':']


def __run_algorithm(algorithm, input) -> Context:
    ctx = Context()

    input = copy.deepcopy(input)
    start = time.time_ns()
    # TODO: count memory usage
    # memory = memory_profiler.memory_usage(
    #     (algorithm, [input, ctx], {}), max_usage=True)
    algorithm(input, ctx)
    end = time.time_ns()

    # ctx.account(Op.MEMORY_KB, memory)
    ctx.account(Op.RUNTIME_MS, (end - start) / 1e6)

    return ctx


def analyse(algorithms, inputs, ops) -> None:
    unique_inpit_sizes = sorted(set(len(input) for input in inputs))
    size_to_idx = {size: idx for idx, size in enumerate(unique_inpit_sizes)}

    x = list(unique_inpit_sizes)

    for algorithm in algorithms:
        print_info(f'ANALYSE ({algorithm.__name__}) [{len(inputs)}]: ',
                   end='', flush=True)

        ctxs = []
        for _ in x:
            ctxs.append([])

        for i, input in enumerate(inputs):
            ctx = __run_algorithm(algorithm, input)
            ctxs[size_to_idx[len(input)]].append(ctx)

            if (i + 1) % (len(inputs) // min(len(inputs), 10)) == 0:
                print_info('.', sep='', end='', flush=True)

        for i, op in enumerate(ops):
            # TODO: get avg
            y = [ctx[0].get(op) for ctx in ctxs]

            # TODO: different subplot for each op
            plt.plot(
                x, y, label=f'{algorithm.__name__} {op.name}', alpha=ALPHA, ls=LS[i % len(LS)])

        print_ok(f'\nDONE ({algorithm.__name__}) [{len(inputs)}]')

    plt.grid(True)
    plt.legend()
    plt.show()
