class Colors:
    OK = '\033[92m'
    INFO = '\033[94m'
    FAIL = '\033[91m'
    END = '\033[0m'


def print_info(*args, **kwargs) -> None:
    print(Colors.INFO, sep='', end='')
    print(*args, **kwargs)
    print(Colors.END, sep='', end='')


def print_ok(*args, **kwargs) -> None:
    print(Colors.OK, sep='', end='')
    print(*args, **kwargs)
    print(Colors.END, sep='', end='')


def print_fail(*args, **kwargs) -> None:
    print(Colors.FAIL, sep='', end='')
    print(*args, **kwargs)
    print(Colors.END, sep='', end='')
