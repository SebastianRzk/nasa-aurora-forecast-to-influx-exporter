import logging
from typing import Self


class Status:
    def __init__(self, name: str):
        self.is_ok = True
        self.name = name + "_status"

    def everything_worked_as_expected(self) -> Self:
        logging.info(f"Everything worked as expected at {self.name}")
        return self

    def failed(self) -> Self:
        logging.error(f"Error happend at {self.name}")
        self.is_ok = False
        return self
