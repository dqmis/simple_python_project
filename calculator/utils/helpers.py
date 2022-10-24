from typing import Callable, Optional
import time
import logging


def timer(fn: Callable) -> Callable:
    # TODO: Log how much time has passed
    def track_time():
        start_time = time.time()
        print(f'Vykdymo laikas = {time.time() - start_time}')
    return track_time


def calculator_logger(fn: Callable) -> Callable:
    # TODO: Log function name and it's args and kwargs
    def cal_loger(*args):
            cal_log_info = (f"Funkcija {fn.__name__} su args {args}")
            return fn(*args)
    return cal_loger

def input_parser(fn: Callable) -> Callable:
    def convert_to_int(*args) -> Optional[int]:
        # TODO: Enable this function to work with multiple args and kwargs
        try:
            return fn(args[0], int(args[1]))
        except Exception:
            print(f"Cannot convert input of type {type(args[1])} to an int")
            return None

    return convert_to_int