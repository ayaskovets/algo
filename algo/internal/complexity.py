# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring

import enum

from algo.types import Plot


class Complexity(enum.Enum):
    N = enum.auto()
    N_2 = enum.auto()
    LOG_N = enum.auto()
    N_LOG_N = enum.auto()


def calculate_complexity(plot: Plot) -> Complexity:
    """
        Calculates complextity from graph points
    """

    # TODO: implement
    return Complexity.N
