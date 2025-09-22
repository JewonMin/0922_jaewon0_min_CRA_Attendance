from .rule import PlayerRule
from .model import Player
from enum import Enum

class LegacyPlayerRule(PlayerRule):
    class Grade(Enum):
        NORMAL = 0
        SILVER = 2
        GOLD = 1

    class GradeThreshold(Enum):
        SILVER = 30
        GOLD = 50

    def __init__(self):
        self.point_map = {
            "monday": 1, "tuesday": 1, "wednesday": 3,
            "thursday": 1, "friday": 1, "saturday": 2, "sunday": 2,
        }
        self.wednesday_bonus_threshold: int = 10
        self.wednesday_bonus_point: int = 10
        self.weekend_bonus_threshold: int = 10
        self.weekend_bonus_point: int = 10

    def update_basic_info(self, player: Player, weekday:str):
        player.days[weekday] += 1
        player.points += self.point_map[weekday]

    def update_bonus_info(self, player: Player):
        if player.wednesday_count >= self.wednesday_bonus_threshold:
            player.points += self.wednesday_bonus_point
        if player.weekend_count >= self.weekend_bonus_threshold:
            player.points += self.weekend_bonus_point

    def update_grade_info(self, player: Player):
        if player.points >= self.GradeThreshold.GOLD.value:
            player.grade = self.Grade.GOLD.value
        elif player.points >= self.GradeThreshold.SILVER.value:
            player.grade = self.Grade.SILVER.value
        else:
            player.grade = self.Grade.NORMAL.value

    def is_removed_player(self, player: Player) -> bool:
        return (player.grade == self.Grade.NORMAL.value
                and player.wednesday_count == 0
                and player.weekend_count == 0)

    def print_each_player_grade(self, player:Player):
        grade_name = \
            {self.Grade.NORMAL.value: "NORMAL",
             self.Grade.GOLD.value: "GOLD",
             self.Grade.SILVER.value: "SILVER"}[player.grade]
        print(f"NAME: {player.name}, POINT: {player.points}, GRADE: {grade_name}")




