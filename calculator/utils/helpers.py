from typing import Callable, Optional
import logging
logging.basicConfig(filename="output.log", level=logging.INFO)
import time

def calculator_logger(fn: Callable) -> Callable:
    def calculator_logger(*args, **kwargs):
        logging.info(f"Running a function {fn.__name__} with args: {args} and kwargs: {kwargs}")
        return fn(*args, **kwargs)
    return calculator_logger

def timer(fn):
    def track_time(*args, **kwargs):
        start_time = time.time()
        res = fn(*args, **kwargs)
        execution_time = f"Execution time {time.time() - start_time}"
        return res, execution_time
    return track_time

def input_parser(fn: Callable) -> Callable:
    def convert_to_int(*args) -> Optional[int]:
        # TODO: Enable this function to work with multiple args and kwargs
        try:
            return fn(args[0], int(args[1]), int(args[2]))
        except Exception:
            print(f"Cannot convert input of type {type(args[1])} {type(args[2])} to an int")
            return None

    return convert_to_int
