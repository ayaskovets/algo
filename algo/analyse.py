import copy
import time

import matplotlib.pyplot as plt
import memory_profiler

from algo.ctx import Context, ContextAgg
from algo.log import print_info, print_ok, progress
from algo.ops import Agg, Op


ALPHA = 0.5
LS = ['-', '--', '-.', ':']


def _run_algorithm(algorithm, input) -> Context:
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


def _show_analysis(algorithms: list, ctx_agg: ContextAgg, ops: list[tuple[Agg, Op]]) -> None:
    for agg, op in ops:
        for algorithm in algorithms:
            x, y = ctx_agg.get(algorithm, agg, op)

            plt.plot(
                x, y, label=f'{algorithm.__name__} {agg.name} {op.name}', alpha=ALPHA)

    # TODO: different subplot for each op
    # TODO: get ~complexity

    plt.grid(True)
    plt.legend()
    plt.show()


def analyse(algorithms: list, inputs: list, weight, ops: list[tuple[Agg, Op]]) -> None:
    ctx_agg = ContextAgg()

    for algorithm in algorithms:
        print_info(f'ANALYSE ({algorithm.__name__}) [{len(inputs)}]: ',
                   end='', flush=True)

        for input in progress(inputs):
            ctx = _run_algorithm(algorithm, input)
            ctx_agg.account(algorithm, weight(input), ctx)

        print_ok(f'\nDONE ({algorithm.__name__}) [{len(inputs)}]')

    _show_analysis(algorithms, ctx_agg, ops)
