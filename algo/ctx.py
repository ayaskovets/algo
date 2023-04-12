import collections


class Context:
    def __init__(self) -> None:
        self.ops = collections.defaultdict(int)
