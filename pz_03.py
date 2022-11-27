class Tomato:

    growing = {"states": ("low", "medium", "done")}

    def __init__(self, _index, _state=growing["states"][0]):
        self._index = _index
        self.grow()

    def grow(self):
        self._index += 1
        self._state = self.growing["states"][self._index]
        self.is_ripe()

    def is_ripe(self):
        if self._state == self.growing["states"][2]:
            print("good")
        else:
            self.grow()


test = Tomato(0)
print(test)