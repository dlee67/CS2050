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

        return ",".join(str(node) for node in self)

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

        new = None

        if self.empty():

            raise RuntimeError

        elif(self.front == self.back):

            new = self.front.value

            self.front = self.back = None

            return new
            
        
        else:
        
            new = self.front.value

            self.front = self.front.next

            return new
        

    def pop_back(self):

        new = None

        if self.empty():

            raise RuntimeError

#왜됄수박에없는거지?
#         
#If front is same as back, that only means 
#
#THERE IS ONLY ONE NODE IN THE LINKED LIST.
#
#because a fresh push_front will have both FRONT AND BACK WILL BE INNITIALIZED with
#
#the VERY FIRST NODE to be put in the linked list,
#
#that's why.
#
#
        elif(self.front == self.back):

            new = self.front.value

            self.front = self.back = None

            return new

        else:

            old = self.back.value

            new = self.front
            
#When node that is being flipped through has a
#
#next that point to the truely last node,
#
#THEN I AM NOW AT THE SECOND TO LAST NODE.
#
#
#

#But, I must remember the philosophy of this while block.
#
#I DOING IT SO I CAN POP THE VALUE INSIDE THE LAST NODE AND DELETE IT.
#
#THIS WORKS BECAUSE I AM TRYING TO FIND THE SECOND TO LAST NODE
#
#AND THE SECOND TO LAST NODE WILL BECOME BACK, which is a last node.
#
#
            while new.next != self.back:
                
#new has the reference to the LAST NODE
                
                new = new.next

#The last node has now beoome the "previous second to last node".
            self.back = new

            new.next = None

#The value of the last node is now being popped.
            return old
            
        
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

        self.assertEquals(ll.__str__(), '1,2,3')

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

class factorial:
    
    def fact(self, a):
        
        if a < 0:

            raise ValueError("Less than zero")
        
        if a == 0 or a == 1:

            return 1

        stack = linked_list()
        
        while a > 1:

            stack.push_front(a)
            
            a -= 1

        result = 1
        
        while not stack.empty():

            result *= stack.pop_front()

        return result

class test_factorial (unittest.TestCase):

    def test_less_than_zero(self):

        self.assertRaises(ValueError, lambda: factorial().fact(-1))

    def test_zero(self):

        self.assertEquals(factorial().fact(0), 1)

    def test_one(self):

        self.assertEquals(factorial().fact(1), 1)

    def test_two(self):

        self.assertEquals(factorial().fact(2), 2)

    def test_10(self):

        self.assertEquals(factorial().fact(10), 10*9*8*7*6*5*4*3*2*1)

if __name__ == "__main__":

        print (factorial().fact(1))

        print (factorial().fact(2))

        print (factorial().fact(100))
