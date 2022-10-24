from datetime import datetime
from operator import index
from typing import Callable, Optional
import time
import logging


def timer(fn: Callable) -> Callable:
    # TODO: Log how much time has passed
    def timer_function(*args, **kwargs):
        start_time = time.time() 
        res = fn(*args, **kwargs)
        print(f"Execution time {time.time() - start_time}")
        return res
    return timer_function


def calculator_logger(fn: Callable) -> Callable:
    # TODO: Log function name and it's args and kwargs
    logging.basicConfig(filename="output.log", level=logging.INFO)
    def logging_function(*args, **kwargs):
        res = fn(*args, **kwargs)
        logging.info(f"{datetime.now()}: Running function {fn.__name__} with args {args} and kwargs {kwargs}")    
        return res
    return logging_function


def input_parser(fn: Callable) -> Callable:
    def convert_to_int(*args, **kwargs) -> Optional[int]:
        # TODO: Enable this function to work with multiple args and kwargs
                
        for i in range(1, len(args)):
            try:
                args[i] = int(args[i])
            except Exception:
                print(f"Args conversion: Cannot convert input of type {type(args[i])} to an int")
                return None
                    
        for key, value in kwargs.items():
            try:
                kwargs[key] = int(value)
            except Exception:
                print(f"Kwargs conversion: Cannot convert input of type {type(kwargs['key'])} value to an int")
                return None

        return fn(args, kwargs)
    return convert_to_int
