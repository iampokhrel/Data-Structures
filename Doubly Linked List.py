# ========================CREATING A BASIC Doubly LINKED LIST===========================
"""
This program creates a python implementation of Doubly Linked Lists.
Internally, however, they are stored as dictionaries for ease of use.
The locations are keys of the dictionaries, with values being random normal values.
"""

import numpy as np

# ===========NODE=============


class __Node:
    """
    Node class to store a single node.
    Requires the data to be stored in the node, and pointers to the next and the previous node
    """

    def __init__(self, data, previous, next) -> None:
        self.data = data
        self.next = next
        self.previous = previous


# ===========LIST=============

class LinkedList:
    """
    Contains the actual implementation of a doubly linked list.
    Requires startData (optional): A single data point to start the linked list.
    Methods:
        get(), getAll(), add(), delete(), pop(), len()
    """

    def __init__(self, startData=None) -> None:
        self.__list = dict()
        self.start = None
        self.end = None
        self.length = 0
        if startData is not None:
            pos = self.__createPos()
            self.start = pos
            self.end = pos
            self.__createNode(startData, self.start, None, None)

    def __createNode(self, data, pos, prev, next):
        """
        Creates a singe node
        """
        nd = __Node(data, prev, next)
        self.__list[pos] = nd
        self.length += 1

    def __createPos(self):
        """
        Create position in memory (de jure)
        Gives a random number as position pointer (de facto)
        """
        return round(np.random.normal(5000, 1250))

    def __getAtIndex(self, ind):
        """
        Returns the location of a certain node, given node index in the list
        """
        if ind > self.length/2:
            i, loc = 0, self.start
            while i != ind:
                loc = self.__list[loc].next
                i += 1
        else:
            i, loc = self.length - 1, self.end
            while i != ind:
                loc = self.__list[loc].previous
                i -= 1
        return loc

    def __getLast(self):
        """
        Returns the last node in the list
        """
        return self.end

    def getAll(self, fromSide="start"):
        """
        Returns a a dictionary, where the key are the positions and the values are the node data.
        Optional argument 'fromSide': 'start' (Default) or 'end'. 'start' lists the elements from the begining
        of the list, and 'end' lists the elements from the end of the list.
        """
        lst = dict()
        if fromSide == "start":
            loc = self.start
            while True:
                lst[loc] = self.__list[loc].data
                loc = self.__list[loc].next
                if loc is None:
                    break
        elif fromSide == "end":
            loc = self.end
            while True:
                lst[loc] = self.__list[loc].data
                loc = self.__list[loc].previous
                if loc is None:
                    break
        return lst

    def get(self, index):
        """
        Returns a certain node given its index
        """
        if index > self.length:
            raise IndexError("Index out of range of the linked list")
        if index == -1:
            return self.__list[self.__getLast()].data
        else:
            return self.__list[self.__getAtIndex(index)].data

    def add(self, data):
        """
        Adds a new node to the list given data.
        """
        if self.start is None:
            loc = self.__createPos()
            self.start = loc
            self.end = loc
            self.__createNode(data, self.start, None)
        else:
            last = self.__getLast()
            pos = self.__createPos()
            self.__list[last].next = pos
            prev = self.end
            self.__createNode(data, pos, prev, None)
        self.length += 1

    def delete(self, index):
        """
        Delete a certain node, given index
        """
        if index > self.length or index < 0:
            raise IndexError("Index out of range of the linked list")
        if index == self.length - 1:
            self.pop()
            return
        loc = self.__getAtIndex(index)
        nextLoc = self.__list[loc].next
        prevLoc = self.__list[loc].previous
        self.__list.pop(index)

        if index == 0:
            self.start = nextLoc
        if index == -1 or index == self.length - 1:
            self.end = prevLoc
        else:
            pre = self.__getAtIndex(index-1)
            post = self.__getAtIndex(index+1)
            self.__list[pre].next = nextLoc
            self.__list[post].previous = prevLoc
        self.length -= 1

    def pop(self):
        """
        Delete the last node
        """
        self.__list[-2].next = None
        self.__list.pop(self.length-1)

    def len(self):
        """
        Returns length of the list
        """
        return self.length

    def peek(self):
        """
        Peek at the last node in the linked list
        """
        return self.__list[self.__getLast()].data
