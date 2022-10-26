import logging, time
from typing import Callable, Optional
logging.basicConfig(filename="output.log", level=logging.INFO)

def timer(fn: Callable) -> Callable:
    def track_time(*args, **kwargs):
        start_time = time.time()
        res = fn(*args, **kwargs)
        print(f"Execution time {time.time() - start_time}")
        return res
    return track_time


def calculator_logger(fn: Callable) -> Callable:
    def logeris():
        logging.info(f"Running a function {fn.__name__}" )
        return fn()
    return logeris()



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
