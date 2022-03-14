from dataclasses import dataclass, field


@dataclass
class Response:
    # TODOs
    # Represent status_code as enums
    status_code: int = 200
    message: str = "success"    
    data: dict = field(default_factory= lambda x: {})
    # TODOs
    # Represent metadata as seperate class
    metadata : dict = field(default_factory= lambda x: {}) 
    