from __future__ import print_function
import unittest

def findandreplace(find, replace, string):

    if string == "":

        return ""

    if string == None:

        return None

    if find == None:

        return string

    if find == "":

        return string

    if replace == None:

        return string

    if string[0] == find:

        return replace + findandreplace(find, replace, string[len(find):])

    else:

        return string[:len(find)] + findandreplace(find, replace, string[len(find):])

class TestFindAndReplace(unittest.TestCase):
    def test_all_none(self):
        self.assertEqual(findandreplace(None, None, None), None)
    def test_find_none(self):
        self.assertEqual(findandreplace(None, "a", "aabb"), "aabb")
    def test_find_empty(self):
        self.assertEqual(findandreplace("", "a", "aabb"), "aabb")
    def test_replace_none(self):
        self.assertEqual(findandreplace("a", None, "aabb"), "aabb")
    def test_string_none(self):
        self.assertEqual(findandreplace("a", "b", None), None)
    def test_simple(self):
        self.assertEqual(findandreplace("a", "b", "aabb"), "bbbb")
    def test_remove(self):
        self.assertEqual(findandreplace(" ", "", " a abb"), "aabb")
    def test_gettysburg(self):
        self.assertEqual(findandreplace("Four score", "Twenty", \
            "Four score and seven years ago"), "Twenty and seven years ago")