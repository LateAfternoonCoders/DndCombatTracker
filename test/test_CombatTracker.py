from backend.models.characterStats import CharacterStats
from backend.combactTracker import CombatTracker
from backend.models.character import Character
from backend.models.user import Player, Master
import pytest


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


@pytest.mark.parametrize(
        "level, hp, initiative, armorClass, speed, expectedError",
        (
            (-2, 3, 4, 5, 6, "Invalid level!"),
            (2, -3, 4, 5, 6, "Invalid hp!"),
            (2, 3, -4, 5, 6, "Invalid initiative!"),
            (2, 3, 4, -5, 6, "Invalid armor class!"),
            (2, 3, 4, 5, -6, "Invalid speed!")
        ))
def test_fail_character_stats(
        level, hp, initiative, armorClass, speed, expectedError):

    with pytest.raises(Exception) as ex_info:
        CharacterStats(level, hp, initiative, armorClass, speed)
    assert str(ex_info.value) == expectedError


def test_add_character_stat():
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


def test_add_players():
    tracker = CombatTracker()
    player_names = ("Al", "Bi", "Ga", "Gg", "Pa", "St")
    players = list(map(Player, player_names))

    for p in players:
        tracker.add_user(p)

    tracker.add_user(Master("Ja"))

    assert all(
        [x.name == y for (x, y) in zip(tracker.get_players(), player_names)]
        )
    assert all(
        [x.role == 'Player' for x in tracker.get_players()]
        )


def test_add_master():
    tracker = CombatTracker()
    player_names = ("Al", "Bi", "Ga", "Gg", "Pa", "St")
    players = list(map(Player, player_names))

    for p in players:
        tracker.add_user(p)

    tracker.add_user(Master("Ja"))

    assert tracker.get_master().name == "Ja"
    assert tracker.get_master().role == "Master"


def test_fail_add_multiple_masters():
    tracker = CombatTracker()

    tracker.add_user(Master("Ja"))

    with pytest.raises(Exception) as ex_info:
        tracker.add_user(Master("Jb"))
    assert str(ex_info.value) == "Master already present!"


def test_assign_character_to_player():
    pass
