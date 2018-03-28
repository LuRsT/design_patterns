class Icecream:

    def __init__(self):
        self.scoops = 0
        self.flavour = ''

    def __str__(self):
        return f'I am a {self.flavour} icecream, with {self.scoops} scoops'


class IcecreamBuilder:

    def __init__(self):
        self.icecream = Icecream()

    def set_flavour(self, flavour):
        self.icecream.flavour = flavour

    def set_scoops(self, scoops):
        self.icecream.scoops = scoops

    def build(self):
        return self.icecream


if __name__ == '__main__':
    ice_cream = IcecreamBuilder()
    ice_cream.set_flavour('Chocolate')
    ice_cream.set_scoops(2)
    print(ice_cream.build())
