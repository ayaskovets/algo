import collections

from algo.ops import Op


class Context:
    def __init__(self) -> None:
        self._ops = collections.defaultdict(int)

    def account(self, op: Op, amount: int = 1):
        self._ops[op] += amount

    def remove(self, op: Op, amount: int = 1):
        self._ops[op] -= amount

    def get(self, op: Op):
        return self._ops[op]
