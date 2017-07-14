from __future__ import print_function
import unittest

class linked_list:
    class node:
        def __init__(self, value, next):
            self.value = value
            self.next = next

    def __init__(self, initial = None):

        self.front = self.back = None
######
######
#
#
#
    def empty(self):
        return self.front == self.back == None
#####
#####
#
#
#    
    def __iter__(self):
        self.current = self.front
        return self

#####
#####
#
#
#    
#
    def __next__(self):
        
        if self.current:
            
            tmp = self.current.value
            
            self.current = current.next
            
            return tmp
        
        else:
            
            raise StopIteration()

#######
#######
#
#
#
#

    def __str__(self):

        return",".join(str(node) for node in self)

#######
#######
#
#
#
#
    def __repr__(self):
        pass

######
######
#    
#
#
#
    def push_front(self, value):
        
        new = self.node(value, self.front)
        
        if self.empty():
            
            self.front = self.back = new
            
        else:
            
            self.front = new

#######
####### 
#      
#      
# 
#
    def push_back(self, value):

        new = self.node(value, None)

        if self.empty():

            self.push_front(value)

        else:

            self.tail.next = new


#######
#######
#
#
#
#
    def pop_front(self):

        pass

#######
#######
#
#
#
#
    def pop_back(self):

        pass

