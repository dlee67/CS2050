from __future__ import print_function
import unittest

class linked_list:
    class node:
        def __init__ (self, value, next):
            self.value = value
            self.next = next

    # do not put in getters and setters as they are not needed

    def __init__(self, initial = None):
        # for extra credit, add in the elements of initial
        self.front = self.back = None

    def empty(self):
        return self.front == self.back == None

    def __iter__(self):
        self.current = self.front
        return self

    def __next__(self):
        if self.current:
            tmp = self.current.value
            self.current = self.current.next
            return tmp
        else:
            raise StopIteration()

    def __str__(self):
        pass

    def __repr__(self):
        # extra credit
        pass

    def push_front(self, value):
        old = self.front
        new = self.node(value, self.front)
        if self.empty():
            self.front = self.back = self.node(value, None)
        else:
            new.next = old
            self.front = new

    def push_back(self, value):

        new = self.node(value, None)

        if self.empty():

            self.push_front(value)

        else:

            self.back.next = new

            self.back = new



    def pop_front(self):


        if self.empty():

            raise RuntimeError

        elif self.front == self.back:

            new = self.front.value

            self.front = self.back = None

            return new
        else:

            new = self.front.value

            self.front = self.front.next

            return new


    def pop_back(self):

        if self.empty():

            raise RuntimeError

        elif self.front == self.back:

            new = self.front.value

            self.front = self.back = None

            return new

        else:
            sheesh = self.back.value

            new = self.front

            while new.next != self.back:

                new = new.next

            self.back = new

            new.next = None

            return sheesh



class test_linked_list (unittest.TestCase):
    def test_none(self):
        self.assertTrue(linked_list().empty())
    def test_pop_front_empty(self):
        self.assertRaises(RuntimeError, lambda: linked_list().pop_front())
    def test_pop_back_empty(self):
        self.assertRaises(RuntimeError, lambda: linked_list().pop_back())
    def test_push_back_pop_front(self):
        ll = linked_list()
        ll.push_back(1)
        ll.push_back(2)
        ll.push_back(3)
        self.assertFalse(ll.empty())
        self.assertEquals(ll.pop_front(), 1)
        self.assertEquals(ll.pop_front(), 2)
        self.assertEquals(ll.pop_front(), 3)
        self.assertTrue(ll.empty())
    def test_push_front_pop_front(self):
        ll = linked_list()
        ll.push_front(1)
        ll.push_front(2)
        ll.push_front(3)
        self.assertEquals(ll.pop_front(), 3)
        self.assertEquals(ll.pop_front(), 2)
        self.assertEquals(ll.pop_front(), 1)
        self.assertTrue(ll.empty())
    def test_push_front_pop_back(self):
        ll = linked_list()
        ll.push_front(1)
        ll.push_front(2)
        ll.push_front(3)
        self.assertFalse(ll.empty())
        self.assertEquals(ll.pop_back(), 1)
        self.assertEquals(ll.pop_back(), 2)
        self.assertEquals(ll.pop_back(), 3)
        self.assertTrue(ll.empty())
    def test_push_back_pop_back(self):
        ll = linked_list()
        ll.push_back(1)
        ll.push_back("foo")
        ll.push_back([3,2,1])
        self.assertFalse(ll.empty())
        self.assertEquals(ll.pop_back(),[3,2,1])
        self.assertEquals(ll.pop_back(), "foo")
        self.assertEquals(ll.pop_back(), 1)
        self.assertTrue(ll.empty())


