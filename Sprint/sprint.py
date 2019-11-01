import numpy as np

class AcmeProduct:

    def __init__(name, price=10, weight=20, flammability=.5, identifier=np.random.randint(1000000, 9999999)):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier

