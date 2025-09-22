from abc import ABC, abstractmethod
from .model import Player

class PlayerRule(ABC):
    @abstractmethod
    def update_basic_points(self, player: Player, weekday:str):
        pass

    @abstractmethod
    def update_bonus_points(self, player: Player):
        pass

    @abstractmethod
    def update_grade(self, player: Player):
        pass

    @abstractmethod
    def is_removed_player(self, player: Player) -> bool:
        pass

