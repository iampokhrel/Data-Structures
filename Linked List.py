# ========================CREATING A BASIC LINKED LIST===========================
"""
This program creates a python implementation of Linked Lists.
Internally, however, they are stored as dictionaries for ease of use.
The locations are keys of the dictionaries, with values being random normal values.
"""

import numpy as np

# ===========NODE=============


class Node:
    def __init__(self, data, next) -> None:
        self.data = data
        self.next = next


# ===========LIST=============

class LinkedList:
    def __init__(self, startData=None) -> None:
        self.__list = dict()
        self.start = None
        if startData is not None:
            self.start = self.__createPos()
            self.__createNode(startData, self.start, None)

    def __createNode(self, data, pos, next):
        nd = Node(data, next)
        self.__list[pos] = nd

    def __createPos(self):
        return round(np.random.normal(5000, 1250))

    def __getAtIndex(self, ind):
        i, loc = 0, self.start
        while i != ind:
            loc = self.__list[loc].next
            i += 1
        return loc

    def __getLast(self):
        loc = self.start
        while True:
            if self.__list[loc].next is None:
                break
            loc = self.__list[loc].next
        return loc

    def getAll(self):
        lst = dict()
        loc = self.start
        while True:
            lst[loc] = self.__list[loc].data
            loc = self.__list[loc].next
            if loc is None:
                break
        return lst

    def get(self, index): 
        if index == -1:
            return self.__list[self.__getLast()].data
        else:
            return self.__list[self.__getAtIndex(index)].data

    def add(self, data):
        if self.start is None:
            self.start = self.__createPos()
            self.__createNode(data, self.start, None)
        else:
            last = self.__getLast()
            pos = self.__createPos()
            self.__list[last].next = pos
            self.__createNode(data, pos, None)

    def delete(self, index):
        pass


l2 = LinkedList(25)
print(l2.getAll())
print(l2.get(0))
print(l2.get(-1))
l2.add(33)
print(l2.get(0))
print(l2.get(1))
print(l2.get(-1))
print(l2.getAll())
