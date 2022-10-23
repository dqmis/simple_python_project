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
    def add(self, a: Optional[int] = None, b: Optional[int] = None) -> int:
        if a:
            self._memory += a
        if b:
            self._memory += b
        return self._memory

    @timer
    @calculator_logger
    #@input_parser
    def sub(self, a: Optional[int] = None, b: Optional[int] = None) -> int:
        if a:
            self._memory -= a
        if b:
            self._memory -= b
        return self._memory

    @timer
    @calculator_logger
    @input_parser
    def mul(self, a: Optional[int]) -> int:
        if a:
            self._memory *= a
        return self._memory

    @timer
    @calculator_logger
    @input_parser
    def pow(self, a: Optional[int]) -> int:
        if a:
            self._memory = self._memory**a
        return self._memory
