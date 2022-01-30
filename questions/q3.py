"""
Given the root to a binary tree, implement serialize(root), which serializes the
tree into a string, and deserialize(s), which deserializes the string back into 
the tree.
"""

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def serialize(node: Node) -> str:
    buffer = [(node, 0)]
    str_arr = []
    while len(buffer) > 0:
        curr_node, idx = buffer[0]
        curr_left = curr_node.left
        curr_right = curr_node.right

        while idx > len(str_arr):
            str_arr.append("None")
        str_arr.append(curr_node.val)
        del buffer[0]

        if curr_left is not None:
            buffer.append((curr_left, 2 * idx + 1))
        
        if curr_right is not None:
            buffer.append((curr_right, 2 * idx + 2))

    return ", ".join(str_arr)


def deserialize(s: str) -> Node:
    str_arr = s.split(", ")
    
    root = Node(str_arr[0])
    buffer = [(root, 0)]
    while len(buffer) > 0:
        curr_node, idx = buffer[0]
        del buffer[0]
        
        left_idx = 2 * idx + 1
        if left_idx < len(str_arr) and str_arr[left_idx] != "None":
            left_node = Node(str_arr[left_idx])
            curr_node.left = left_node
            buffer.append((left_node, left_idx))

        right_idx = 2 * idx + 2
        if right_idx < len(str_arr) and str_arr[right_idx] != "None":
            right_node = Node(str_arr[right_idx])
            curr_node.right = right_node
            buffer.append((right_node, right_idx))

    return root