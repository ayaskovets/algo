import enum


class Op(enum.Enum):
    # manually accounted
    COMPARISONS = 'comparisons'
    SWAPS = 'swaps'

    # automatically accounted
    MEMORY_KB = 'memory (kb)'
    RUNTIME_MS = 'runtime (ms)'


class Agg(enum.Enum):
    AVERAGE = 'average'
    SUM = 'sum'
