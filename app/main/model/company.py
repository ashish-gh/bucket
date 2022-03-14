from dataclasses import dataclass, field


@dataclass
class Coordinates:
    """
    Representation of location on earths sphere.
    
    """
    latitude: float = field(default=0.0, metadata= {"unit": "degrees"})
    longitude: float = field(default=0.0, metadata= {"unit": "degrees"})

    # TODO
    # Check if the co-ordinate is valid co-ordinate or not    

    def __str__(self) -> str:
        return f"{self.latitude} | {self.longitude}"       

@dataclass
class Location(Coordinates):
    street: str = ""
    city: str = ""
    state: str = ""
    zip: str = ""

    def __str__(self) -> str:
        return f"{self.street} | {self.city} | {self.state} | {self.zip}  | {self.latitude} | {self.longitude}"
       

    

@dataclass
class Company:
    name: str = ""
    