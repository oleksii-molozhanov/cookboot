from dataclasses import dataclass
from typing import NewType


Ingridient = NewType("Ingridient", str)


@dataclass
class Recipe:
    id: str
    name: str
    ingridients: list[Ingridient]
