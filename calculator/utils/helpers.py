from typing import Callable, Optional


def timer(fn: Callable) -> Callable:
    # TODO: Log how much time has passed
    pass


def calculator_logger(fn: Callable) -> Callable:
    # TODO: Log function name and it's args and kwargs
    pass


def input_parser(fn: Callable) -> Callable:
    def convert_to_int(*args) -> Optional[int]:
        # TODO: Enable this function to work with multiple args and kwargs
        try:
            parsed_args = [int(arg) for arg in args[1:]]
            parsed_args.insert(0, args[0])
            return fn(*parsed_args)
        except Exception:
            print(f"Cannot convert input of type {type(args[1])} to an int")
            return None

    return convert_to_int
