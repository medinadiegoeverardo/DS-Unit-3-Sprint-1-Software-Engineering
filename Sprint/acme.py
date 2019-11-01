import numpy as np


class AcmeProduct:

    def __init__(self, name, price=10, weight=20, flammability=.5,
                 identifier=np.random.randint(1000000, 9999999)):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier

    def stealability(self):
        steal_me = self.price / self.weight
        if steal_me < .5:
            return 'Not so stealable'
        elif steal_me >= .5 and steal_me < 1.0:
            return 'Kinda stealable'
        else:
            return 'Very stealable'

    def explode(self):
        would_explode = self.flammability * self.weight
        if would_explode < 10:
            return 'fizzle'
        elif would_explode >= 10 and would_explode < 50:
            return 'boom'
        else:
            return 'BABOOM'


class BoxingGlove(AcmeProduct):

    def __init__(self, weight=10):
        super().__init__(weight)
        self.weight = weight
        # if I wanted to inherit other properties like name or price, add them
        # to super()

    def explode(self):
        return '...it\'s a glove.'

    def punch(self):
        if self.weight < 5:
            return 'That tickles'
        elif self.weight >= 5 and self.weight < 15:
            return 'Hey that hurt!'
        else:
            return 'Ouch!'

#prod = AcmeProduct('Toy', 20, 5, .2)
# print(prod.__dict__)

# autopep8 -i -a acme.py