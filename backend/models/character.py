from backend.models.characterStats import CharacterStats


class Character:
    def __init__(self, name: str, className: str, raceName: str):
        self.name = name
        self.className = className
        self.raceName = raceName
        self._ID = None

    def set_stats(self, stats: CharacterStats):
        self.stats = stats

    def get_stats(self):
        return self.stats
