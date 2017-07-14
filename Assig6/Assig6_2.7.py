from __future__ import print_function
import unittest

'''
Description:A program that solves N-queens problem
Author:Bob(Dong) Lee
Version:1.0
Help received from:Ms.Haley, Wikipedia, YouTube
Help provided to:Bob(Dong) Lee
'''

def safe((x1, y1), (x2, y2)):

    ''' Return if two queens, represented by tuples,
        are safe from each other. '''

    if x1 == x2: return False
    if y1 == y2: return False
    if abs(x2-x1) == abs(y2-y1): return False
    return True

def print_solution(size, placed):
    ''' Given a board size and a list of tuples,
        print out the board. '''
    print("for:", size)
    if placed == []:
        print("no solution found")
        return

    for i in range(size):
        for j in range(size):
            if (i, j) in placed:
                print("Q", end="")
            else:
                print(".", end="")
        print()

    print('-' * size)


def solve(size, row, placed):

    if row == size:

        return placed

    for column in range(size):

        new_queen = (row, column)

        good = True

        for queen in placed:

            good &= safe(queen, new_queen)

        if good:

            print(new_queen, "Is good to append")

            placed.append(new_queen)

            temp = solve(size, row+1, placed)

            if temp == []:

                print("popping ", new_queen, " from", placed)

                placed.pop()

            else:

                print("Else block being run, returning ", placed)

                return placed

    return []

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
        self.assertEquals(solve(8, 8, []), [])
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
