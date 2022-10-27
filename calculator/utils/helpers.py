from typing import Callable, Optional
import logging
from datetime import datetime

logging.basicConfig(filename="output.log", level=logging.INFO)

def timer(fn: Callable) -> Callable:
    # TODO: Log how much time has passed
    
    def time_calc(*args, **kwargs):
        start_time = datetime.now()
        res = fn(*args, **kwargs)
        end_time = datetime.now()
        execution_time = end_time - start_time
        print(f"Process time: {execution_time}")
        return res
    return time_calc
    

def calculator_logger(fn: Callable) -> Callable:
    # TODO: Log function name and it's args and kwargs
    def logger(*args, **kwargs):
        logging.info(f"{datetime.now()} test Runing a function {fn.__name__} w/ {args} and {kwargs}")
        return fn()
    return logger


def input_parser(fn: Callable) -> Callable:
    def convert_to_int(*args, **kwargs) -> Optional[int]:
        # TODO: Enable this function to work with multiple args and kwargs
        try:
            #return fn(args[0], int(args[1]))
            return fn(*args, int(**kwargs))
        except Exception:
            print(f"Cannot convert input of type {type(*args)} to an int")
            return None

    return convert_to_int


