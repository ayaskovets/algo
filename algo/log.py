class Colors:
    OK = '\033[92m'
    INFO = '\033[94m'
    FAIL = '\033[91m'
    END = '\033[0m'


def print_info(text: str) -> None:
    print(f'{Colors.INFO}{text}{Colors.END}')


def print_ok(text: str) -> None:
    print(f'{Colors.OK}{text}{Colors.END}')


def print_fail(text: str) -> None:
    print(f'{Colors.FAIL}{text}{Colors.END}')
