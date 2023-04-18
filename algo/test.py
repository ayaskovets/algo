import copy

from algo.ctx import Context
from algo.log import print_info, print_ok, print_fail


def test(algorithms, inputs, predicate) -> None:
    for algorithm in algorithms:
        print_info(f'TEST ({algorithm.__name__}) [{len(inputs)}]: ',
                   end='', flush=True)

        for i, input in enumerate(inputs):
            ctx = Context()
            output = algorithm(copy.deepcopy(input), ctx=ctx)

            if not predicate(input, output):
                print_fail(f'FAIL [{i}]: {input} -> {output}')
                assert False

            if (i + 1) % (len(inputs) // min(len(inputs), 10)) == 0:
                print_info('.', sep='', end='', flush=True)

        print_ok(f'\nOK ({algorithm.__name__}) [{len(inputs)}]')
