
class Composite:
    def __init__(self):
        self.__array = []

    def __len__(self):
        return len(self.__array)

    def __getitem__(self, key):
        return self.__array[key]

    def __setitem__(self, key, value):
        try:
            self.__array[key] = value
        except IndexError:
            assert key >= 0, 'key must be 0 or positive'
            self.__array.extend(((key + 1) - len(self.__array)) * [None])
            self.__array[key] = value

