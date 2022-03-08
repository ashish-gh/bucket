import json
import os
from abc import ABCMeta, abstractmethod
from typing import Dict

from .handler import JSONFileHandler


class BaseExtractor(metaclass=ABCMeta):
    
    @abstractmethod
    def extract(self, *args, **kwargs):
        raise NotImplementedError
    
    def classname(self) -> str:
        return f"{self.__class__.__name__}"
    

class JSONExtractor(BaseExtractor):
    """
    Extractor to extract all data saved in json file.
    """
    def extract(self) -> Dict[str, Dict]:
        file_name = os.path.join(
            os.getcwd(), "app", "services", "extraction", "lookups", "data.json"
        )
        with JSONFileHandler(file_name=file_name, mode="r") as handler:
            data = json.load(handler)
        return data

class DataBaseExtrctor(BaseExtractor):
    """
    Extractor to extract all data from database.
    All database connection is maintained before this
    """
    def extract(self, *args, **kwargs):
        pass
