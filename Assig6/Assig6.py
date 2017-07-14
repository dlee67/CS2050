from __future__ import print_function
import unittest

def safe((x1, y1), (x2, y2)):

    pass

#    ''' Return if two queens, represented by tuples,
#        are safe from each other. '''

#    if x1 == x2: return False

#    if y1 == y2: return False

#    if abs(x2-x1) == abs(y2-y1): return False

#    return True

def print_solution(size, placed):

    pass

    ''' Given a board size and a list of tuples,
        print out the board. '''

#    print("for:", size)

#    if placed == []:

#        print("no solution found")

#        return


#    for i in range(size):

#        for j in range(size):

#            if (i, j) in placed:

#                print("Q", end="")

#            else:

#                print(".", end="")

#        print()

#    print('-' * size)

def solve(size, row, placed):


    pass
#    ''' Look for a queens solution on a board of size,
#        checking for a specific row, given a list of
#        queens that are already placed. '''

    # print('size:', size)

    # print('row:', row)

    # print('placed:', placed)

#    if row == size:

#        return placed

    # for each column

        # check this (row, column) against the placed queens

        # if this (row, column) is safe

            # set a temp variable to solve with size, row+1,

            # and placed+[(row, column)]

            # if that didn't work, try the next column

            # else return the temp variable

    # we've tried all the columns to no avail, so return

    # an empty array to denote there is no solution for this

    # row using placed. that will signal backtracking in the

    # previous row.

class test_queen(unittest.TestCase):

    def test_same(self):

        self.assertFalse(safe((1, 1), (1, 1)))

    def test_same_row(self):

        self.assertFalse(safe((1, 1), (1, 2)))

    def test_same_column(self):

        self.assertFalse(safe((1, 1), (2, 1)))

    def test_same_diagonal(self):

        self.assertFalse(safe((1, 1), (5, 5)))

    def test_no_solution(self):

        self.assertEquals(solve(0, 0, []), [])

        self.assertEquals(solve(2, 0, []), [])

        self.assertEquals(solve(3, 0, []), [])

    def test_one(self):

        self.assertEquals(solve(1, 0, []), [(0, 0)])

    def test_four(self):

        self.assertEquals(solve(4, 0, []), [(0, 1), (1, 3), (2, 0), (3, 2)])

    def test_eight(self):

        self.assertEquals(solve(8, 0, []), \

            [(0, 0), (1, 4), (2, 7), (3, 5), (4, 2), (5, 6), (6, 1), (7, 3)])

if __name__ == "__main__":

    solution = solve(8, 0, [])

    print_solution(8, solution)