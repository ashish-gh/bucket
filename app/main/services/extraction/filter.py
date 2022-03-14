import json
import os
from abc import ABCMeta, abstractmethod
from typing import Dict

import pandas as pd
from loguru import logger

from .extractor import JSONExtractor


class BaseFilter(metaclass=ABCMeta):
    
    @abstractmethod
    def filter(self, *args, **kwargs):
        raise NotImplementedError
    
    def classname(self) -> str:
        return f"{self.__class__.__name__}"
    

class NameFilter(BaseFilter):
    """
    Filter data using name
    """

    def __init__(self, name: str = "") -> None:
        if not name:
            raise ValueError(f"Empty value of `name` for class: {self.classname}")
        self.name = name
    def filter(self, name: str = ""):
        logger.debug(f"Using : {self.classname} filter.")
        if not name:
            name = self.name
        data = JSONExtractor().extract()
        data = data.get(name, {})
        return data






# class CombinedFilter(BaseFilter):
#     def filter(self, *args, **kwargs):
#         pass



def main():
    pass


if __name__ == "__main__":
    main()
