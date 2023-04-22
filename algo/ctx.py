import collections
import operator
import typing

from algo.log import print_error
from algo.ops import Agg, Op


class Context:
    def __init__(self) -> None:
        self._ops = {}

    def account(self, op: Op, amount: float = 1.0) -> None:
        if op not in self._ops:
            self._ops[op] = amount
        else:
            self._ops[op] += amount

    def get(self, op: Op, default: float = None) -> typing.Optional[float]:
        return self._ops.get(op, default)


class ContextAgg:
    def __init__(self) -> None:
        self._ctxs_by_algorithm = collections.defaultdict(
            lambda: collections.defaultdict(list))

    def account(self, algorithm, weight: float, ctx: Context) -> None:
        self._ctxs_by_algorithm[algorithm][weight].append(ctx)

    @staticmethod
    def _aggregate(ctxs: list[Context], aggregation: Agg, op: Op) -> float:
        if aggregation == Agg.AVERAGE:
            return sum(ctx.get(op, 0.0) for ctx in ctxs) / len(ctxs)
        elif aggregation == Agg.SUM:
            return sum(ctx.get(op, 0.0) for ctx in ctxs)
        else:
            print_error(f'aggregation {aggregation} is not implemented yet!')
            assert not 'implemented yet!'

    def get(self, algorithm, aggregation: Agg, op: Op) -> tuple[list, list]:
        x, y = [], []

        for weight, ctxs in sorted(self._ctxs_by_algorithm[algorithm].items(), key=operator.itemgetter(0)):
            x.append(weight)
            y.append(ContextAgg._aggregate(ctxs, aggregation, op))

        return x, y
