from backend.models.character import Character
from backend.models.user import User, Player, Master


class CombatTracker():
    def __init__(self):
        self._characters = []
        self._users = []

    def add_character(self, character: Character):
        self._characters += [character]

    def remove_character(self, character: Character):
        self._characters.remove(character)

    def get_characters(self) -> list[Character]:
        return self._characters

    def add_user(self, user: User):
        if isinstance(user, Master):
            if self.get_master() is not None:
                raise ValueError("Master already present!")
        self._users += [user]

    def get_players(self) -> list[Player]:
        return [x for x in self._users if x.role == 'Player']

    def get_master(self) -> Master:
        masters = [x for x in self._users if x.role == 'Master']

        if len(masters) > 1:
            raise ValueError("Too many masters!")
        elif len(masters) == 1:
            return masters[0]
        else:
            return None
