import json
import os
from abc import ABCMeta, abstractmethod
from dataclasses import dataclass
from typing import Dict, Type

from loguru import logger


class BaseHandler(metaclass=ABCMeta):
    
    @abstractmethod
    def handle(self, *args, **kwargs):
        raise NotImplementedError
    
    def classname(self) -> str:
        return f"{self.__class__.__name__}"
    

class FileHandler(BaseHandler):
    _mode = "r"

    def __init__(self, file_name: str = "") -> None:
        if not file_name:
            raise ValueError(f"Expected value for `file_name`. Got empty value")

        self.file_name = file_name
    
    def __enter__(self) -> Type[BaseHandler]:
        if not self.is_valid_file(file_name=self.file_name) or self.is_valid_extension(self.file_name) -> bool:
            msg = f"[Error] exception in parsing file"
            raise Exception 
        
        self.file = open(self.file_name, self._mode)
        return self.file
    
    def __exit__(self, *args, **kwargs):
        self.file.close()

    def is_valid_extension(self, file_name: str = "") -> bool:
        _, ext = os.path.splitext(file_name)
        if ext not in self.extensions:
            msg = f"[Error] extension not founf. Not a valid extension:  {str(ext)}"
            logger.error(msg)
            raise Exception
        return True
    
    def is_valid_file(self, file_name: str = ""):
        if not os.path.isfile(file_name):
            msg = f"[Error] unable to parse file. Not a valid file:  {str(file_name)}"
            logger.error(msg)
            raise FileNotFoundError(msg)
        return True

    def handle(self, *args, **kwargs):
        pass

class JsonFileHandler(FileHandler):
    extensions = [".json", ".JSON"]

    def __init__(self, file_name: str = "") -> None:
        super().__init__(file_name=file_name)

    def handle(self) -> Dict[str, Dict]:
        try:
            with open(self.file_name, self.mode) as file:
                data = json.load(file)
        except Exception as e:
            msg = f"[Error] in parsing file {str(self.file_name)}. Exception : {str(e)}"
            logger.error(msg)
            data = {}
        return data
