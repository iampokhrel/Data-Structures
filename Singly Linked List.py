# ========================CREATING A BASIC LINKED LIST===========================
"""
This program creates a python implementation of Linked Lists.
Internally, however, they are stored as dictionaries for ease of use.
The locations are keys of the dictionaries, with values being random normal values.
"""

import numpy as np

# ===========NODE=============


class Node:
    """
    Node class to store a single node.
    Requires the data to be stored in the node, and pointer to the next node
    """

    def __init__(self, data, next) -> None:
        self.data = data
        self.next = next


# ===========LIST=============

class LinkedList:
    """
    Contains the actual implementation of a singly linked list.
    Requires startData (optional): A single data point to start the linked list.
    Methods:
        get(), add(), delete(), getAll()
    """

    def __init__(self, startData=None) -> None:
        self.__list = dict()
        self.start = None
        if startData is not None:
            self.start = self.__createPos()
            self.__createNode(startData, self.start, None)

    def __createNode(self, data, pos, next):
        """
        Creates a singe node
        """
        nd = Node(data, next)
        self.__list[pos] = nd

    def __createPos(self):
        """
        Create position in memory (de jure)
        Gives a random number as position pointer (de facto)
        """
        return round(np.random.normal(5000, 1250))

    def __getAtIndex(self, ind):
        """
        Returns the location of a certian node, given node index in the list
        """
        i, loc = 0, self.start
        while i != ind:
            loc = self.__list[loc].next
            i += 1
        return loc

    def __getLast(self):
        """
        Returns the last node in the list
        """
        loc = self.start
        while True:
            if self.__list[loc].next is None:
                break
            loc = self.__list[loc].next
        return loc

    def getAll(self):
        """
        Returns a a dictionary, where the key are the positions and the values are the node data.
        """
        lst = dict()
        loc = self.start
        while True:
            lst[loc] = self.__list[loc].data
            loc = self.__list[loc].next
            if loc is None:
                break
        return lst

    def get(self, index):
        """
        Returns a certain node given its index
        """
        if index == -1:
            return self.__list[self.__getLast()].data
        else:
            return self.__list[self.__getAtIndex(index)].data

    def add(self, data):
        """
        Adds a new node to the list given data.
        """
        if self.start is None:
            self.start = self.__createPos()
            self.__createNode(data, self.start, None)
        else:
            last = self.__getLast()
            pos = self.__createPos()
            self.__list[last].next = pos
            self.__createNode(data, pos, None)

    def delete(self, index):
        """
        Delete a certain node, given index
        """
        pass
