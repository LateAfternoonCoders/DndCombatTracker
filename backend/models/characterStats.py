class CharacterStats:
    def __init__(
            self, level: int, hp: int,
            initiative: int, armorClass: int, speed: int):
        if level < 1:
            raise ValueError("Invalid level!")
        if hp < 1:
            raise ValueError("Invalid hp!")
        if initiative < 1:
            raise ValueError("Invalid initiative!")
        if armorClass < 1:
            raise ValueError("Invalid armor class!")
        if speed < 1:
            raise ValueError("Invalid speed!")

        self.level = level
        self.hp = hp
        self.initiative = initiative
        self.armorClass = armorClass
        self.speed = speed
