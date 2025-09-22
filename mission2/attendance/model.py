from dataclasses import dataclass, field
from typing import Dict
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
    def wednesday_count(self) -> int:
        return self.days["wednesday"]
    @property
    def weekend_count(self) -> int:
        return self.days["saturday"] + self.days["sunday"]

@dataclass
class AttendanceInfo:
    players: Dict[str, Player] = field(
        default_factory=lambda: {}
    )
    def get(self, name:str) -> Player:
        if name not in self.players:
            self.players[name] = Player(name=name)
        return self.players[name]




