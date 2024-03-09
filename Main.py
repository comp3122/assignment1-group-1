import RPGMap

class RPGGame:
    def _init_(self, map_width, map_height):
        self.map = RPGMap(map_width, map_height)
        self.player = None
        self.monsters = []

    def add_player(self, player, x, y):
        self.player = player
        self.map.place_character(x, y, 'P')

    def add_monster(self, monster, x, y):
        self.monsters.append(monster)
        self.map.place_character(x, y, 'M')

    def run(self):
        # This is a very basic game loop that just makes the player and monsters attack each other
        while self.player.is_alive() and any(monster.is_alive() for monster in self.monsters):
            for monster in self.monsters:
                if monster.is_alive():
                    self.player.attack(monster)
                if monster.is_alive():
                    monster.attack(self.player)
            self.map.print_map()

        if self.player.is_alive():
            print("Player wins!")
        else:
            print("Monsters win!")
