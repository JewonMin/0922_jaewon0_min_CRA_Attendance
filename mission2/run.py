from attendance.rule_legacy import LegacyPlayerRule
from attendance.application import AttendanceApplication

def process_file(filename: str) -> None:
    app = AttendanceApplication(rule = LegacyPlayerRule())
    try:
        with open(filename, encoding="utf-8") as line:
            app.process_lines(line)
    except FileNotFoundError:
        print("파일을 찾을 수 없습니다.")
        return

    app.process_total_results()
    app.print_results()

if __name__ == "__main__":
    process_file("attendance_weekday_500.txt")
