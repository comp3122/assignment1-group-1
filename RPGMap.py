class RPGMap:
    def _init_(self, width, height):
        self.width = width
        self.height = height
        self.map = [['.' for _ in range(width)] for _ in range(height)]

    def print_map(self):
        for row in self.map:
            print(' '.join(row))

    def place_character(self, x, y, character):
        if 0 <= x < self.width and 0 <= y < self.height:
            self.map[y][x] = character
        else:
            print("Invalid position")

    def move_character(self, old_x, old_y, new_x, new_y):
        if 0 <= old_x < self.width and 0 <= old_y < self.height and 0 <= new_x < self.width and 0 <= new_y < self.height:
            character = self.map[old_y][old_x]
            self.map[old_y][old_x] = '.'
            self.map[new_y][new_x] = character
        else:
            print("Invalid move")
