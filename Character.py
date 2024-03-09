class Character:
    def _init_(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other_character):
        other_character.health -= self.attack_power
        print(f"{self.name} attacks {other_character.name} for {self.attack_power} damage!")

    def is_alive(self):
        return self.health > 0

class Player(Character):
    def _init_(self, name, health, attack_power):
        super()._init_(name, health, attack_power)

class Monster(Character):
    def _init_(self, name, health, attack_power):
        super()._init_(name, health, attack_power)
