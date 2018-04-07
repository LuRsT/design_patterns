class IceCream:

    def __init__(self, cone):
        self.cone = cone

    def get_cone(self):
        self.cone.get()


class NormalCone:

    def get(self):
        print('Fetching from tube...')


# Imagine that this class was done earlier and we can't modify it's code
# So we create the adapter bellow that will provide the interface that icecream
# needs
class WaffleCone:

    def grab_and_wrap(self):
        print('Grabbing and wrapping')


class WaffleConeAdapter:

    def __init__(self, cone_instance):
        self.cone_instance = cone_instance

    def get(self):
        return self.cone_instance.grab_and_wrap()


if __name__ == '__main__':
    i = IceCream(WaffleConeAdapter(WaffleCone()))
    i.get_cone()

    i = IceCream(NormalCone())
    i.get_cone()
