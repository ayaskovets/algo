class Colors:
    OK = '\033[92m'
    INFO = '\033[94m'
    ERROR = '\033[91m'
    END = '\033[0m'


def print_info(*args, **kwargs) -> None:
    print(Colors.INFO, sep='', end='')
    print(*args, **kwargs)
    print(Colors.END, sep='', end='')


def print_ok(*args, **kwargs) -> None:
    print(Colors.OK, sep='', end='')
    print(*args, **kwargs)
    print(Colors.END, sep='', end='')


def print_error(*args, **kwargs) -> None:
    print(Colors.ERROR, sep='', end='')
    print(*args, **kwargs)
    print(Colors.END, sep='', end='')


def progress(items, length=10):
    for i, item in enumerate(items):
        yield item
        if (i + 1) % (len(items) // min(len(items), length)) == 0:
            print_info('.', sep='', end='', flush=True)
