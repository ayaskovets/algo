import copy

from algo.log import print_info, print_ok, print_fail

def test(algorithms, inputs, predicate) -> None:
    for algorithm in algorithms:
        print_info(f'TEST ({algorithm.__name__}) [{len(inputs)}]')

        for i, input in enumerate(inputs):
            output = algorithm(copy.deepcopy(input), ctx=None)

            if not predicate(input, output):
                print_fail(f'FAIL [{i}]: {input} -> {output}')
                assert False

        print_ok(f'OK ({algorithm.__name__}) [{len(inputs)}]')
