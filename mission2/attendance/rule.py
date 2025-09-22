from abc import ABC, abstractmethod
from .model import Player

class PlayerRule(ABC):
    @abstractmethod
    def update_basic_info(self, player: Player, weekday:str):
        pass

    @abstractmethod
    def update_bonus_info(self, player: Player):
        pass

    @abstractmethod
    def update_grade_info(self, player: Player):
        pass

    @abstractmethod
    def is_removed_player(self, player: Player) -> bool:
        pass

    @abstractmethod
    def print_each_player_grade(self, player: Player):
        pass
