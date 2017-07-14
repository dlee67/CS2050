from __future__ import print_function
import unittest

#looook, the two next are highlighted.
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
        pass

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
        new = self.node(value, self.front)
        if self.empty():
            self.front = self.back = new
        else:
            self.front = new

#Got is from the website called Code Review
#사진필요하시면 초록색노트참고하시길.
#생각해보니, 아무것도않돼는 코드다.
    def push_back(self, value):
        
        new = self.node(value, None) #like this?

        if self.empty(): #To see if the front and back are empty, if they are, there is no linked list.
            push_front(new) #My decision was that I should use the push front for time saving.
        else:
            self.back.next = new
#I beilieve that now I have a two conneting nodes, but the very last node doesn't seem to be connected to those "two conneting nodes".
#How can I make that possible?
            
        
    def pop_front(self):
#At least in my understanding,
#value is innitialized with the value from
#the linked list's head
#head will be assigned with the next of linked list's head.
#
#but, it's not going to delete the Node that it "popped".
#
        prev_node = self.front
#
#당신의 마음으로부터 요동치는것이있었다.
#07:15PM 06/01/2016
#
#
#I believe that the below statement will "delete" the desired node because
#the head will be assinged with the node in the back.
#the previous head no longer exists
#
#틀렸다, 왜냐면, self.back은어차피 self.front와똑같은존재니깐.
#
#그냥복제됀거나마찬가지
        self.front = self.back        

        return prev_node

#While my itr_obj, which is repeatdly a node from next pointer,
#is not None, it will iterate and assign itr_obj to Node's next.
#when it finally reaches the at_back of the linked list,
#I break out of the loop.
#
#
    def pop_back(self):

        node = self.front
        
        return itr_obj

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
        if a < 0: raise ValueError("Less than zero")
        if a == 0 or a == 1: return 1

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
