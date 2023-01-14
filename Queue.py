class queue:
    def __init__(self, data=None) -> None:
        self.__queue__ = []
        if data is not None:
            self.__queue__.append(data)
 
    def enqueue(self, data):
        self.__queue__.append(data)

    def dequeue(self):
        return self.__queue__.pop(0)

    def peek(self):
        return self.__queue__[0]
