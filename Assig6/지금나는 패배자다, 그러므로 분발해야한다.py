from __future__ import print_function
import unittest
'''
    This method assumes the solution is a list of tuples such as:
    [(0, 1), (1, 3), (2, 0), (3, 2)]
'''

def print_board(solution):
    length = len(solution)
    print("for:", length)
    print('-' * length)

    if solution == []:
        print("no solution found")
    else:
        for i in range(length):
            for j in range(length):
                if (i, j) in solution:
                    print("Q", end="")
                else:
                    print(".", end="")
            print()

    print('-' * length)

'''
    Given the location of two queens, find if they are safe
    from each other.
'''
def safe((x1, y1), (x2, y2)):
    if x1 == x2: return False
    if y1 == y2: return False
    if abs(x2-x1) == abs(y2-y1): return False
    return True

def print_solution(size, placed):
    print("for:", size)
    if placed == []:
        print("no solution found")
        return

    print('-' * size)

    for i in range(size):
        for j in range(size):
            if (i, j) in placed:
                print("Q", end="")
            else:
                print(".", end="")
        print()

    print('-' * size)

def solve_queens(size, row, placed):
    if row == size:
        return placed
    for column in range(size):
        new_queen = (row, column)
        good = True
        for queen in placed:
            good &= safe(new_queen, queen)
        if good:
            placed.append(new_queen)
            tmp = solve_queens(size, row + 1, placed)
            if not tmp:
                placed.pop()
            else:
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
        self.assertEquals(solve_queens(0, 0, []), [])
        self.assertEquals(solve_queens(2, 0, []), [])
        self.assertEquals(solve_queens(3, 0, []), [])
    def test_one(self):
        self.assertEquals(solve_queens(1, 0, []), [(0, 0)])
    def test_four(self):
        self.assertEquals(solve_queens(4, 0, []), [(0, 1), (1, 3), (2, 0), (3, 2)])
    def test_eight(self):
        self.assertEquals(solve_queens(8, 0, []), \
            [(0, 0), (1, 4), (2, 7), (3, 5), (4, 2), (5, 6), (6, 1), (7, 3)])

if __name__ == "__main__":
    solution = solve_queens(8, 0, [])
    print_solution(8, solution)