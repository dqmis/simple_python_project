from typing import Optional

from calculator.utils.helpers import calculator_logger, input_parser, timer


class Calculator:
    def __init__(self) -> None:
        self._memory = 0

    @property
    def memory(self) -> int:
        return self._memory

    def clear(self) -> int:
        self._memory = 0
        return self._memory

    @timer
    @calculator_logger
    @input_parser
    def add(self, *args, **kwargs) -> int:
        
        for i in args:
            self._memory += i
        
        for key, value in kwargs.items():
            self._memory += kwargs[key]

        return self._memory

    @timer
    @calculator_logger
    @input_parser
    def sub(self, *args, **kwargs) -> int:
        
        for i in args:
            self._memory -= i
        
        for key, value in kwargs.items():
            self._memory -= kwargs[key]

        return self._memory

    @timer
    @calculator_logger
    @input_parser
    def mul(self, *args, **kwargs) -> int:
        
        for i in args:
            self._memory *= i
        
        for key, value in kwargs.items():
            self._memory *= kwargs[key]

        return self._memory

    @timer
    @calculator_logger
    @input_parser
    def pow(self, *args, **kwargs) -> int:
        
        for i in args:
            self._memory = self._memory ** i
        
        for key, value in kwargs.items():
            self._memory = self._memory ** kwargs[key]

        return self._memory
