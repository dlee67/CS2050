#링크드리스트의 기존이뭐냐?
#
#그냥안에있는거 집게처럼 집어올수는없다는거야
#
#For the Linked List, there always needs to be a linear search fot the item
#
#I want.
#
#
#
#
#
#
#
class LinkedList:

    class Node:

        def __init__(self, item):
            self.item = item
            self.next = None

        def getItem(self):
            return self.item

        def getNext(sels):
            return self.next

        def setItem(self, item):
            self.item = item

        def setNext(self, otherside):
            self.next = otherside

#The point of the constructor is to keep the reference to the first Node.
#
#The above comment is the pure designation of LinkedList constructor
#
#If I am trying to be flashy, I can also have the last node stored in here.
#
#They both point to something called "dummy node" to begin with, 
#
#What does the dummy node do? They just don't contain anything.
#
    def __init__(self, contents=[]):

        self.first = LinkedList.__Node(None, None)
        self.last = self.first
        self.numItems = 0

        for e in contents:
            self.append(e)

    def __getItem__(self, index):
        if index >= 0 and index < self.numItems:
            cursor = self.first.getNext()
            for i in range(index):
                cursor = cursor.getNext()

    def __setItem__(self, index, val):
        if index >= 0 and index < self.numItems:
            cursor = self.first.getNext()
            for i in range(index):
                cursor = cursor.getNext()

            cursor.setItem(val)

        raise IndexError("LinkedList assignment index out of range")
    

    def __add__(self, other):
        if type(self) != type(other):
            raise TypeError("Concatenate undefined for " + \
                            str(type(self) + " + " + str(type(other)))

        result = LinkedList()

        cursor = self.first.getNext()

        while cursor != None:

            result.append(cursor.getItem())

            cursor = cursor.getNext()

        cursor = other.first.getNext()

        while cursor != None:
            result.append(cursor.getItem())
            cursor = cursor.getNext()

        return result
                            
                                
