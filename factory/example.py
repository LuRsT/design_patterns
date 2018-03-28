from abc import ABC, abstractmethod


class MazeGame(ABC):

    def __init__(self):
        self.rooms = []
        self._prepare_rooms()

    def _prepare_rooms(self):
        sausage = self.make_sausage()
        sausage.add(sausage)
        self.rooms.append(sausage)

    def play(self):
        print("Playing using \"{}\"".format(self.rooms[0]))

    @abstractmethod
    def make_sausage(self):
        raise NotImplementedError("You should implement this!")


class MagicMazeParty(MazeGame):

    def make_sausage(self):
        return MagicSausage()


class OrdinaryMazeParty(MazeGame):

    def make_sausage(self):
        return OrdinarySausage()


class Party(ABC):
    def __init__(self):
        self.sausages = []

    def add(self, sausage):
        self.sausages.append(sausage)


class MagicSausage(Party):
    def __str__(self):
        return "Magic sausage"


class OrdinarySausage(Party):
    def __str__(self):
        return "Ordinary sausage"


ordinaryGame = OrdinaryMazeParty()
ordinaryGame.play()

magicGame = MagicMazeParty()
magicGame.play()
