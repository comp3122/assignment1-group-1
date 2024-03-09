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
    
    def get_stats(self):
        return self.stats
    
    def get_team(self):
        return self.team
    
    def get_league(self):
        return self.league
    
    def get_country(self):
        return self.country
    
    def get_club(self):
        return self.club
    
    def get_contract(self):
        return self.contract

    def get_salary(self):
        return self.salary
# """

player = Player('John Doe', 25, 'Forward')
print(player.name)
print(player.age)
print(player.position)
