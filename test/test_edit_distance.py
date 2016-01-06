import unittest
from edit_distance import edit_distance

class TestEditDistance(unittest.TestCase):
    def test_delete(self):
        "able to find a simple delete"
        self.assertEqual(edit_distance("aaab", "aaa"), 1)

    def test_addition(self):
        "able to find a simple delete"
        self.assertEqual(edit_distance("aaa", "aaab"), 1)

    def test_change(self):
        "able to find a simple change"
        self.assertEqual(edit_distance("hat", "cat"), 1)
