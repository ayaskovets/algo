import copy

from algo.ctx import Context
from algo.log import print_info, print_ok, print_error, progress


def test(algorithms: list, inputs: list, predicate) -> None:
    for algorithm in algorithms:
        print_info(
            f'TEST ({algorithm.__name__}) [{len(inputs)}]: ', end='', flush=True)

        for input in progress(inputs):
            ctx = Context()
            output = algorithm(copy.deepcopy(input), ctx=ctx)

            if not predicate(output):
                print_error(
                    f'\nERROR ({algorithm.__name__}): {input} -> {output}')
                assert False

        print_ok(f'\nOK ({algorithm.__name__}) [{len(inputs)}]')
