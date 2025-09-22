from dataclasses import dataclass, field
from typing import List, Dict
from enum import Enum

class Grade(Enum):
    NORMAL = 0
    SILVER = 2
    GOLD = 1

@dataclass
class Player:
    name:str
    days: Dict[str, int] = field(
        default_factory=lambda: {
            "monday": 0,
            "tuesday": 0,
            "wednesday": 0,
            "thursday": 0,
            "friday": 0,
            "saturday": 0,
            "sunday": 0,
        }
    )
    points: int = 0
    grade: int = Grade.NORMAL.value

    @property
