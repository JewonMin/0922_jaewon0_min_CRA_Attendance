from .application import AttendanceApplication
from .model import AttendanceInfo, Player
from .rule import PlayerRule
from .rule_legacy import LegacyPlayerRule

GRADE_NORMAL = 0
GRADE_GOLD = 1
GRADE_SILVER = 2

def test_parse_line():
    app = AttendanceApplication(LegacyPlayerRule())
    line1 = 'Alice monday'
    expected_result1 = ('Alice', 'monday')
    actual_result1 = app.parse_line(line1)
    assert actual_result1 == expected_result1

    line2 = ''
    expected_result2 = (None, None)
    actual_result2 = app.parse_line(line2)
    assert actual_result2 == expected_result2

def test_process_lines():
    lines = [
        "Alice monday",
        "Alice wednesday",
        "Bob saturday",
        "Bob sunday",
        "Cara tuesday",
        "Cara tuesday",
    ]
    app = AttendanceApplication(LegacyPlayerRule())
    app.process_lines(lines)
    assert len(app.info.players) == 3

def test_total_results(capsys):
    lines1 = [
        "Alice monday",
        "Alice wednesday",
        "Bob saturday",
        "Bob sunday",
        "Cara tuesday",
        "Cara tuesday",
    ] * 30
    lines2 = [
        "Cathy monday"
    ] * 30
    lines3 = [
        "Cath monday"
    ]
    expected_str1 = "NAME: Alice, POINT: 130, GRADE: GOLD"
    expected_str2 = "NAME: Bob, POINT: 130, GRADE: GOLD"
    expected_str3 = "NAME: Cara, POINT: 60, GRADE: GOLD"
    expected_str4 = "Cathy, POINT: 30, GRADE: SILVER"
    expected_str5 = "NAME: Cath, POINT: 1, GRADE: NORMAL"
    expected_str6 = "Removed player\n==============\nCath"

    lines = lines1 + lines2 + lines3
    app = AttendanceApplication(LegacyPlayerRule())
    app.process_lines(lines)
    app.process_total_results()
    app.print_results()
    out = capsys.readouterr().out
    assert len(app.info.players) == 5
    assert expected_str1 in out
    assert expected_str2 in out
    assert expected_str3 in out
    assert expected_str4 in out
    assert expected_str5 in out
    assert expected_str6 in out
