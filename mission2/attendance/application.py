from .model import AttendanceInfo, Player
from .rule import PlayerRule

class AttendanceApplication:
    def __init__(self, rule : PlayerRule):
        self.rule = rule
        self.info = AttendanceInfo()

    @staticmethod
    def parse_line(line: str):
        parts = line.strip().split()
        if len(parts) == 2:
            return parts[0], parts[1]
        return None, None

    def insert_day_info(self, name:str, weekday:str):
        player = self.info.get(name)
        self.rule.update_basic_info(player, weekday)

    def process_lines(self, lines):
        for line in lines:
            name, weekday = self.parse_line(line)
            if name and weekday:
                self.insert_day_info(name, weekday)

    def process_total_results(self):
        for player in self.info.players.values():
            self.rule.update_bonus_info(player)
            self.rule.update_grade_info(player)

    def get_removed_players(self):
        removed = []
        for player in self.info.players.values():
            if self.rule.is_removed_player(player):
                removed.append(player.name)
        return removed

    def print_removed_player(self):
        removed = self.get_removed_players()
        print("\nRemoved player")
        print("==============")
        for name in removed:
            print(name)

    def print_results(self):
        for player in self.info.players.values():
            self.rule.print_each_player_grade(player)
        self.print_removed_player()
