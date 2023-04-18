import enum


class Op(enum.Enum):
    COMPARISONS = 'comparisons'
    MEMORY = 'memory'
    RUNTIME = 'runtime'
    SWAPS = 'swaps'
