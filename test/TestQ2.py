import unittest
from questions import q2


class TestQ2(unittest.TestCase):

    def test_all_product_1(self):
        produced = q2.all_product([1, 2, 3, 4])
        expected = [24, 12, 8, 6]
        assert (expected == produced)

    def test_all_product_2(self):
        produced = q2.all_product([3, 2, 1])
        expected = [2, 3, 6]
        assert (expected == produced)
