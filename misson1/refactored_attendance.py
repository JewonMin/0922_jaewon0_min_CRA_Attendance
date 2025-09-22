
def parse_line(line: str):
    parts = line.strip().split()
    if len(parts) == 2:
        return parts[0], parts[1]
    return None, None

def update_attendance_info(attendance_info, name, weekday):
    pass

def get_grade(player:str):
    pass

def load_file(file_name: str):
    attendance_info = {}
    try:
        with open(file_name, encoding='utf-8') as f:
            for line in f:
                name, weekday = parse_line(line)
                if name and weekday :
                    update_attendance_info(attendance_info, name, weekday)
        for player in attendance_info.values():
            get_grade(player)
        return attendance_info


    except FileNotFoundError:
        print("파일을 찾을 수 없습니다.")





    except FileNotFoundError:
        print("파일을 찾을 수 없습니다.")


if __name__ == "__main__":
    data = load_file("attendance_weekday_500.txt")
    #print_result(data)