from backend.models.character import Character


class User():
    def __init__(self, name: str, role: str):
        self.name = name
        self._ID = None
        self.role = role


class Player(User):
    def __init__(self, name):
        super().__init__(name, "Player")
        self.active_character = None

    def set_active_character(self, character: Character):
        self.active_character = character

    def get_active_character(self) -> Character:
        return self.active_character


class Master(User):
    def __init__(self, name):
        super().__init__(name, "Master")
