import unittest
from .introduction import add

class TestIntroduction(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 2), 3)

