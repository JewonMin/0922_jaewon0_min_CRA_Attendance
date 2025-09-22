from enum import StrEnum

POINTS_MAP = {
    "monday": (0, 1),
    "tuesday": (1, 1),
    "wednesday": (2, 3),
    "thursday": (3, 1),
    "friday": (4, 1),
    "saturday": (5, 2),
    "sunday": (6, 2),
}
class Day(StrEnum):
    MONDAY = "monday"
    TUESDAY = "tuesday"
    WEDNESDAY = "wednesday"
    THURSDAY = "thursday"
    FRIDAY = "friday"
    SATURDAY = "saturday"
    SUNDAY = "sunday"

def parse_line(line: str):
    parts = line.strip().split()
    if len(parts) == 2:
        return parts[0], parts[1]
    return None, None

def update_basic_info(attendance_info, name, weekday):
    if name not in attendance_info:
        attendance_info[name] = {
            "days" : [0] * 7,
            "points" : 0,
            "wednesday_count":0,
            "weekend_count":0,
            "grade":0
        }
    player = attendance_info[name]
    if weekday in POINTS_MAP:
        day, score = POINTS_MAP[weekday]
        player["days"][day] += 1
        player["points"] += score
        if weekday == Day.WEDNESDAY:
            player["wednesday_count"] += 1
        if weekday in (Day.SATURDAY, Day.SUNDAY):
            player["weekend_count"] += 1

def update_bonus_info(player):
    if player["days"][POINTS_MAP[Day.WEDNESDAY][0]] > 9:
        player["points"] += 10
    if player["days"][POINTS_MAP[Day.SATURDAY][0]] + player["days"][POINTS_MAP[Day.SUNDAY][0]] > 9:
        player["points"] += 10

def get_grade_info(player):


def load_file(file_name: str):
    attendance_info = {}
    try:
        with open(file_name, encoding='utf-8') as f:
            for line in f:
                name, weekday = parse_line(line)
                if name and weekday :
                    update_basic_info(attendance_info, name, weekday)
        for player in attendance_info.values():
            update_bonus_info(player)
            get_grade_info(player)
        return attendance_info

    except FileNotFoundError:
        print("파일을 찾을 수 없습니다.")


if __name__ == "__main__":
    data = load_file("attendance_weekday_500.txt")
    #print_result(data)