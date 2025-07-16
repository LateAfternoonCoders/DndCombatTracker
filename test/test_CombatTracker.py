from backend.combactTracker import CombatTracker
from backend.models.character import Character


def test_add_character():
    testname = "testname"
    tracker = CombatTracker()
    char = Character(testname)
    tracker.add_character(char)

    result = tracker.get_characters()
    assert len(result) == 1
    assert result[0].name == testname


def test_remove_character():
    testname = "testname"
    tracker = CombatTracker()
    char = Character(testname)
    tracker.add_character(char)

    tracker.remove_character(tracker.get_characters()[0])

    result = tracker.get_characters()
    assert len(result) == 0


def test_remove_specific_character():
    tracker = CombatTracker()

    [tracker.add_character(Character(f"testname{x}")) for x in range(3)]

    tracker.remove_character(tracker.get_characters()[1])

    result = tracker.get_characters()
    assert len(result) == 2
    assert result[0].name == "testname0"
    assert result[1].name == "testname2"
