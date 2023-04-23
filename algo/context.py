"""
    Module containing a wrapper for a single algorithm run context
"""

from algo.operations import Metric
from algo.types import Alias, Map, Maybe, Weight


class Context:
    """
        Context is a summary of the BigO y axis metrics that describe a single
        run of some algorithm
    """

    def __init__(self) -> None:
        self._operations: Map[Metric, Weight] = {}
        self._weights: Map[Alias, Weight] = {}

    def _set_weight(self, alias: Alias, amount: Weight) -> None:
        self._weights[alias] = amount

    def _get_weights(self) -> Map[Alias, Weight]:
        return self._weights

    def account(self, operation: Metric, amount: Weight = 1.0) -> None:
        """
            Arguments:
              - operation: an operation to account

              - amount: amount of the operation to account

            Returns:
              - None
        """

        self._operations[operation] =\
            self._operations.get(operation, 0.0) + amount

    def get(self, operation: Metric,
            default: Maybe[Weight] = None) -> Maybe[Weight]:
        """
            Arguments:
              - operation: an operation to get the amount of

              - default: the same as default in dict.get

            Returns:
              - the amount of the operation
        """
        return self._operations.get(operation, default)
