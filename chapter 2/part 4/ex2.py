class BigThing:
    def __init__(self, obj):
        self._obj = obj

    def size(self):
        if isinstance(self._obj, int):
            return self._obj
        elif isinstance(self._obj, str) or isinstance(self._obj, list) or isinstance(self._obj, dict):
            return len(self._obj)


class BigCat(BigThing):
    def __init__(self, obj, weight):
        super().__init__(obj)
        self._weight = weight

    def size(self):
        if self._weight > 20:
            return "Very Fat"
        elif self._weight > 15:
            return "Fat"
        else:
            return "Ok"


my_thing = BigThing(5)
print(my_thing.size())

cutie = BigCat("mitzy", 15)
print(cutie.size())
