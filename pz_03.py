class Tomato:

    growing = {"states": ("low", "medium", "done")}

    def __init__(self, _index, _state=growing["states"][0]):
        self._index = _index
        self.grow()

    def grow(self):
        self._index += 1
        self._state = self.growing["states"][self._index]

    def is_ripe(self):
        return self._state == self.growing["states"][2]


class TomatoBush:

    def __init__(self, tomatoes):
        pass

    def graw_all(self):
        Tomato(self._index)

    def all_are_ripe(self):
        return Tomato.is_ripe()

    def give_away_all(self):
        pass

test = Tomato(0)
print(test)