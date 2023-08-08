'''hw1'''
class SuperHero:
    people = 'people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase
    def Name(self):
        return f'name: {self.name}'

    def double_health(self):
        return f'helth x2: {self.health_points *2}'

    def __str__(self):
        return f'nickname: {self.nickname} \n' \
               f'superpower: {self.superpower} \n' \
               f'health: {self.health_points}'

    def __len__(self):
        return len(self.catchphrase)

    def print(self):
        print(self.name, self.nickname, self.superpower, self.health_points)

Hero = SuperHero('Bruce', 'Hulk', 'Superhuman strength', 1309, 'Hulk Smash')
print(Hero.Name())
print(Hero.double_health())
print(Hero)
print('Len catchphrase:', len(Hero))

'''hw2'''
class Terrestrial (SuperHero):
    fly = False
    def __init__(self, name, nickname, superpower, helth_points, catchphrase, damage):
        super().__init__(name, nickname, superpower, helth_points, catchphrase)
        self.damage = damage
    def double_health(self):
        return f'helth squared Iron Man: {self.health_points **2}'

class Cosmic (SuperHero):
    fly = False
    def __init__(self, name, nickname, superpower, helth_points, catchphrase, damage):
        super().__init__(name, nickname, superpower, helth_points, catchphrase)
        self.damage = damage
    def double_health(self):
        return f'helth squared Drax: {self.health_points **2}'
    fly = True

    def __str__(self):
        return "Phrase: "'fly in the True_phrase'

terrestrial = Terrestrial('Thony', 'Iron Man', 'genius', 93, 'I am Iron Man', 775.98)
cosmic = Cosmic('Arthur', 'Drax', 'increased strength', 2487, 'Drax the Destroyer', 174)

print(terrestrial.double_health())
print(cosmic.double_health())
print(cosmic)

class villain (Cosmic):
    people = 'monster'
    def gen_x(self):
        pass
    def crit(self):
        return f'Damage: {self.damage **2}'

cosmic2 = Cosmic('Eddie', 'Venom', 'Superhuman strength', 17180, 'We are Venom', 500)

print(villain.crit(cosmic))
