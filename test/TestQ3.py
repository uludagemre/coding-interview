import unittest
from questions.q3 import *


class TestQ2(unittest.TestCase):
    left_left_deep_root = Node("40")
    left_right_deep_root = Node("50")
    left_root = Node("10", left_left_deep_root, left_right_deep_root)

    right_left_deep_root = Node("60")
    right_right_deep_root = Node("70")
    right_root = Node("20", right_left_deep_root, right_right_deep_root)

    mother = Node("30", left_root, right_root)

    def test_serialize_positive(self):
        assert ("30, 10, 20, 40, 50, 60, 70" == serialize(self.mother))

    def test_deserialize_positive(self):
        root_node = deserialize("30, 10, 20, 40, 50, 60, 70")
        assert ("30" == root_node.val)
        assert ("10" == root_node.left.val)
        assert ("20" == root_node.right.val)
