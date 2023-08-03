class SuperHero:
    people = 'people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase

    def __str__(self):
        return f'name: {self.name} \n' \
               f'helth x2: {self.health_points *2} \n' \
               f'nickname: {self.nickname} \n' \
               f'superpower: {self.superpower} \n' \
               f'health: {self.health_points}'

    def __len__(self):
        return len(self.catchphrase)

    def print(self):
        print(self.name, self.nickname, self.superpower, self.health_points)

Hero = SuperHero('Bruce', 'Hulk', 'Superhuman strength', 100, 'HulkSmash')
print(Hero)
print(len(Hero))