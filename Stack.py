class stack:
    def __init__(self, data=None) -> None:
        self.__stack__ = []
        if data is not None:
            self.__stack__.append(data)

    def push(self, data):
        self.__stack__.append(data)

    def pop(self):
        return self.__stack__.pop()

    def peek(self):
        return self.__stack__[-1]
