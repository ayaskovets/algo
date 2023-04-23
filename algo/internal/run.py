# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring

import copy
import time

# TODO: account memory usage
# import memory_profiler

from algo.context import Context
from algo.operations import Metric
from algo.types import Algorithm, Input, Weights


NS_IN_MS = 1e6


def run_algorithm(algorithm: Algorithm, inp: Input,
                  weights: Weights) -> Context:
    """
        Run the algorithm on the input and return the run context containing
        metainformation and metrics to analyse about the run
    """

    ctx = Context()

    inp = copy.deepcopy(inp)
    start = time.time_ns()

    algorithm(inp, ctx)

    end = time.time_ns()

    for function, alias in weights:
        # pylint: disable=protected-access
        ctx._set_weight(alias, function(inp))

    # TODO: account memory usage
    # memory = memory_profiler.memory_usage(
    #     (algorithm, [input, ctx], {}), max_usage=True)
    # ctx.account(Metric.MEMORY_KB, memory)

    ctx.account(Metric.RUNTIME_MS, (end - start) / NS_IN_MS)

    return ctx
