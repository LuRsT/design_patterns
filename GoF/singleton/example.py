class Singleton:
    """
    This class manages the "TheInstance" instance

    """
    instance = None

    class TheInstance:
        """
        This is the instance that will be stored by singleton

        """
        def __init__(self):
            self.icecreams = 0

        def make_icecream(self):
            self.icecreams += 1

        def how_many_icecreams(self):
            return self.icecreams

    def __init__(self):
        if Singleton.instance is None:
            Singleton.instance = Singleton.TheInstance()

    # These methods will just call the methods inside the instance
    def make_icecream(self):
        Singleton.instance.make_icecream()

    def how_many_icecreams(self):
        Singleton.instance.how_many_icecreams()


if __name__ == '__main__':
    # This will create the first instance
    s = Singleton()
    s.make_icecream()
    s.make_icecream()

    # Let's try to create another instance
    ss = Singleton()
    ss.make_icecream()

    # Doesn't matter which instance because they are the same
    assert ss.how_many_icecreams() == s.how_many_icecreams()
