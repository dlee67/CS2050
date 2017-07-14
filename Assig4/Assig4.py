from __future__ import print_function
from sys import stdin
import unittest

'''
Description:This is an assignment 4.
Author:Dong(Bob) Lee
Version:1.0
Help received from:Ms.Haley, Mr.Luke, Joe James(YouTube).
Help provided to:Dong(Bob) Lee
'''

class FamilyTree(object):
    def __init__(self, name, parent=None):
        self._name = name
        self.left = self.right = None
        self._parent = parent

    def __iter__(self):
        if self.left:
            for node in self.left:
                yield node

        yield self._name

        if self.right:
            for node in self.right:
                yield node

    def __str__(self):
        return ','.join(str(node) for node in self)

    def add_below(self, parent, child):
        ''' Add a child below a parent. Only two children per parent
            allowed. '''

        where = self.find(parent)

        if not where:
            raise ValueError('could not find ' + parent)

        if not where.left:
            where.left = FamilyTree(child, where)
        elif not where.right:
            where.right = FamilyTree(child, where)
        else:
            raise ValueError(self + 'already has the allotted two children')

    # Not a BST; have to search up to the whole tree
    def find(self, name):
        if self._name == name: return self

        if self.left:
            left = self.left.find(name)
            if left: return left

        if self.right:
            right = self.right.find(name)
            if right: return right

        return None

    def parent(self, name):

#Still, not returning None.

#Am I even innitializing a correct node?

#If I use find, is it even returning a "lisa" node?

        node = self.find(name)

        return node._parent._name

#And also, if I do have a Lisa node assigned to node variable.
#am I calling the field correctly?

#    return "Homer"

    def grand_parent(self, name):

        node = self.find(name)

        o_node = node._parent

        if o_node._parent == None:

           return None

        e_node = o_node._parent

        return e_node._name

    def generations(self):
        ''' Return a list of lists, where each sub-list is a generation.  '''

        # First, create a list 'this_level' with the root, and three empty
        # lists: 'next_level', 'result', and 'names'

        this_level = [self]

        next_level = []

        result = []

        names = []

        # While 'this_level' has values

        while this_level != []:

            # Remove the first element and append its name to 'names'

            chamber = this_level.pop(0)

            name = chamber._name

            print(name)

            names.append(name)

            # If the first element has a left, append it to 'next_level'

            if chamber.left:

                next_level.append(chamber.left)

            # and do the same for the right

            if chamber.right:

                next_level.append(chamber.right)

            # If 'this_level' is now empty

            if this_level == []:
                # Append 'names' to 'result', set "this_level' to

                result.append(names)

                # 'next_level', and 'next_level' and 'names' to empty

                this_level = next_level

                next_level = []

                names = []

                # lists

        # return result

        return result

    def inorder(self):
        ''' Return a list of the in-order traversal of the tree. '''

        names = []

        if self.left:

            names += self.left.inorder()

        names += [self._name]

        if self.right:

            names += self.right.inorder()

        print(names)

        return names

    def preorder(self):
        ''' Return a list of the pre-order traversal of the tree. '''

        names = []

        names += [self._name]

        if self.left:

            names += self.left.preorder()

        if self.right:

            names += self.right.preorder()

        print(names)

        return names

    def postorder(self):
        ''' Return a list of the post-order traversal of the tree. '''

        names = []

        if self.left:

            names += self.left.postorder()

        if self.right:

            names += self.right.postorder()

        names += [self._name]

        print(names)

        return names


class TestFamilyTree(unittest.TestCase):
    def test_empty(self):
        self.assertEquals(str(FamilyTree(None)), 'None')

    def setUp(self):
        self.tree = FamilyTree("Grandpa")
        self.tree.add_below("Grandpa", "Homer")
        self.tree.add_below("Grandpa", "Herb")
        self.tree.add_below("Homer", "Bart")
        self.tree.add_below("Homer", "Lisa")

    def test_str(self):
        self.assertEquals(str(self.tree), "Bart,Homer,Lisa,Grandpa,Herb")

    def test_parent(self):
        self.assertEquals(self.tree.parent("Lisa"), "Homer")

    def test_grand_parent(self):
        self.assertEquals(self.tree.grand_parent("Lisa"), "Grandpa")

    def test_no_grand_parent(self):
        self.assertEquals(self.tree.grand_parent("Homer"), None)

#It was ["Herb", "Homer"]

#but it's ["Homer", "Herb"], right?

    def test_generations(self):
        self.assertEquals(self.tree.generations(), \
            [["Grandpa"], ["Homer", "Herb"], ["Bart", "Lisa"]])

    ''' Write some more tests, espcially for your generations method, and
        your traversal methods. '''

    def test_inorder(self):

        self.assertEquals(self.tree.inorder(), ['Bart', 'Homer', 'Lisa', 'Grandpa', 'Herb'])

    def test_postorder(self):

        self.assertEquals(self.tree.postorder(), ['Bart', 'Lisa', 'Homer', 'Herb', 'Grandpa'])

    def test_preorder(self):

        self.assertEquals(self.tree.preorder(), ['Grandpa', 'Homer', 'Bart', 'Lisa', 'Herb'])

if '__main__' == __name__:
    ''' Read from standard input a list of relatives. The first line must
        be the ultimate ancestor (the root). The following lines are in the
        form: parent child.'''

    for line in stdin:
        a = line.strip().split(" ")

        ft = None

        if len(a) == 1:
            ft = FamilyTree(a[0])
        else:
            ft.add_below(a[0], a[1])

    print(ft.generations())
