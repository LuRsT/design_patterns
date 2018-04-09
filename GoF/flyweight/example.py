from typing import NamedTuple


class ScoopFactory:
    """
    Creates and caches Scoop objects

    """
    def __init__(self):
        self.scoops = []

    def create_scoop(self, flavour):
        for scoop in self.scoops:
            if scoop.flavour == flavour:
                return scoop
        else:
            obj = Scoop(flavour)
            self.scoops.append(obj)
            return obj


# A simple flyweight, could be a lot more complex, but this one isn't
class Scoop(NamedTuple):
    flavour: str


if __name__ == '__main__':
    factory = ScoopFactory()
    scoop = factory.create_scoop('chocolate')
    scoop2 = factory.create_scoop('chocolate')

    assert scoop is scoop2
