import unittest
from questions import q1


class TestQ1(unittest.TestCase):

    def test_positive_is_sum_up(self):
        assert q1.is_sum_up([10, 15, 3, 7], 25)

    def test_negative_is_sum_up(self):
        assert not q1.is_sum_up([10, 15, 3, 7], 24)

    def test_positive_is_sum_up_with_string_list(self):
        assert q1.is_sum_up("[10, 15, 3, 7]", 25)

    def test_positive_is_sum_up_with_string_k(self):
        assert q1.is_sum_up([10, 15, 3, 7], "25")
