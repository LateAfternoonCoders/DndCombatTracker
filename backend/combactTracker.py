from backend.models.character import Character


class CombatTracker():
    def __init__(self):
        self._characters = []

    def add_character(self, character: Character):
        self._characters += [character]

    def remove_character(self, character: Character):
        self._characters.remove(character)

    def get_characters(self) -> list[Character]:
        return self._characters
