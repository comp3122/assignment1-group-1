print("Assignemtn 1")
# Path: index.py
# mvc model player class
# """
# Player class
class Player:
    def __init__(self, name, age, position):
        self.name = name
        self.age = age
        self.position = position
        self.stats = []
        self.team = None
        self.league = None
        self.country = None
        self.club = None
        self.contract = None
        self.salary = None
# """

player = Player('John Doe', 25, 'Forward')
print(player.name)
