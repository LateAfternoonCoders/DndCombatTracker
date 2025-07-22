from backend.models.characterStats import CharacterStats
from backend.combactTracker import CombatTracker
from backend.models.character import Character


def test_add_character():
    testname = "testname"
    testclass = "testclass"
    testrace = "testrace"
    tracker = CombatTracker()
    char = Character(testname, testclass, testrace)
    tracker.add_character(char)

    result = tracker.get_characters()
    assert len(result) == 1
    assert result[0].name == testname
    assert result[0].className == testclass
    assert result[0].raceName == testrace


def test_remove_character():
    testname = "testname"
    testclass = "testclass"
    testrace = "testrace"
    tracker = CombatTracker()
    char = Character(testname, testclass, testrace)
    tracker.add_character(char)

    tracker.remove_character(tracker.get_characters()[0])

    result = tracker.get_characters()
    assert len(result) == 0


def test_remove_specific_character():
    tracker = CombatTracker()

    # Add 3 characters
    [tracker.add_character(
        Character(f"testname{x}", f"testclass{x}", f"testrace{x}")
        ) for x in range(3)]

    tracker.remove_character(tracker.get_characters()[1])

    result = tracker.get_characters()
    assert len(result) == 2
    assert result[0].name == "testname0"
    assert result[0].className == "testclass0"
    assert result[0].raceName == "testrace0"
    assert result[1].name == "testname2"
    assert result[1].className == "testclass2"
    assert result[1].raceName == "testrace2"


# TODO Add test to validate the set_stats using out of bounds values
def test_set_character_stat():
    pass


def test_add_character_stat():
    pass
    testname = "testname"
    testclass = "testclass"
    testrace = "testrace"
    level = 2
    hp = 3
    initiative = 4
    armorClass = 5
    speed = 6

    tracker = CombatTracker()
    char = Character(testname, testclass, testrace)
    stats = CharacterStats(level, hp, initiative, armorClass, speed)

    char.set_stats(stats)
    tracker.add_character(char)
    chars = tracker.get_characters()
    readStats = chars[0].get_stats()

    assert readStats.level == level
    assert readStats.hp == hp
    assert readStats.initiative == initiative
    assert readStats.armorClass == armorClass
    assert readStats.speed == speed
