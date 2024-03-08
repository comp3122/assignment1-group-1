# monster class
# """
class Monster:
    def __init__(self, name, health, attack, defense):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense

    def take_damage(self, damage):
        self.health -= damage

    def attack_monster(self, monster):
        damage = self.attack - monster.defense
        monster.take_damage(damage)
# """

monster1 = Monster('Goblin', 100, 20, 10)
monster2 = Monster('Troll', 200, 30, 15)
monster1.attack_monster(monster2)
print(monster2.health)
