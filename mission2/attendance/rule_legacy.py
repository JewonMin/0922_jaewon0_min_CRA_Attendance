from .rule import PlayerRule

class LegacyPlayerRule(PlayerRule):
    def update_basic_points(self, player: Player, weekday:str):
        pass

    def update_bonus_points(self, player: Player):
        pass

    def update_grade(self, player: Player):
        pass

    def is_removed_player(self, player: Player) -> bool:
        pass
