import random
ABILITIES=['strength', 'dexterity', 'constitution', 'intelligence', 'wisdom', 'charisma']
def modifier(value):
    return (value - 10) // 2
class Character:
    def __init__(self):
        for abil in ABILITIES:
            setattr(self, abil, self.ability())
        self.hitpoints=10+modifier(self.constitution)
    @staticmethod
    def ability():
        return sum(sorted([random.randint(1,6) for _ in range(4)])[1:])