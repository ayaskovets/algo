import copy

from algo.log import print_info, print_ok, print_fail

def test(algorithm, inputs, predicate) -> None:
    print_info(f'TEST ({algorithm.__name__}) [{len(inputs)}]')

    for i, input in enumerate(inputs):
        output = algorithm(copy.deepcopy(input), ctx=None)

        if not predicate(input, output):
            print_fail(f'FAIL [{i}]: {output}')
            assert False

    print_ok(f'OK ({algorithm.__name__}) [{len(inputs)}]')
