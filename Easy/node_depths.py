# Description
# You are given a binary tree and you are asked to write a function that finds its depth.
#
# A binary tree has the following properties:
#
# It has a root node.
# Each node has a left child and a right child.
# Example:
#       1
#      / \
#     2   3
#    / \  / \
#   4   5 6  7
#  / \
# 8   9
#
# The depth of the above tree is 4.
#
# The depth of a tree is the number of nodes along the longest path from the root node down to the farthest leaf node.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None


# Solution 1
# Big O: O(n) time | O(h) space - where n is the number of nodes in the Binary Tree and h is the height of the Binary Tree
def find_node_depth(tree):
    current_depth = 0
    return find_node_depth_helper(tree, current_depth)


def find_node_depth_helper(tree, current_depth):
    if tree is None:
        return 0
    return current_depth + find_node_depth_helper(tree.left, current_depth + 1) + find_node_depth_helper(tree.right, current_depth + 1)


# Solution 2
# Big O: O(n) time | O(h) space - where n is the number of nodes in the Binary Tree and h is the height of the Binary Tree
def find_node_depth_iterative(tree):
    stack = [{"node": tree, "depth": 0}]
    sum_of_depths = 0
    while len(stack) > 0:
        node_info = stack.pop()
        node, depth = node_info["node"], node_info["depth"]
        if node is None:
            continue
        sum_of_depths += depth
        stack.append({"node": node.right, "depth": depth + 1})
        stack.append({"node": node.left, "depth": depth + 1})
    return sum_of_depths


binary_tree = BinaryTree(1)

binary_tree.left = BinaryTree(2)
binary_tree.right = BinaryTree(3)

binary_tree.left.left = BinaryTree(4)
binary_tree.left.right = BinaryTree(5)

binary_tree.right.left = BinaryTree(6)
binary_tree.right.right = BinaryTree(7)

binary_tree.left.left.left = BinaryTree(8)
binary_tree.left.left.right = BinaryTree(9)

print(find_node_depth_iterative(binary_tree))
print(find_node_depth(binary_tree))
