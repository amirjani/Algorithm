# Description
# You're given a Node class that has a name and an array of optional children
# nodes. When put together, nodes form an acyclic tree-like structure.
# Implement the depthFirstSearch method on the Node class, which takes in an
# empty array, traverses the tree using the Depth-first Search approach
# (specifically navigating the tree from left to right), stores all of the nodes'
# names in the input array, and returns it.
#
# Example
# Input:
# graph = A
#      /  |  \
#     B   C   D
#    / \     / \
#   E   F   G   H
#      / \   \
#     I   J   K
#
# Output: ["A","B","E","F","I","J","C","D","G","K","H"]
#
# Solution
# O(v+e) time | O(v) space
# v = number of vertices
# e = number of edges
def depth_first_search(node, array):
    array.append(node.name)
    for child in node.children:
        depth_first_search(child, array)
    return array


def depth_first_search_tree(tree, array):
    array.append(tree.value)
    if tree.left:
        depth_first_search_tree(tree.left, array)
    if tree.right:
        depth_first_search_tree(tree.right, array)
    return array


class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def add_child(self, name):
        self.children.append(Node(name))


class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


graph = Node("A")
graph.add_child("B")
graph.add_child("C")
graph.add_child("D")
graph.children[0].add_child("E")
graph.children[0].add_child("F")
graph.children[2].add_child("G")
graph.children[2].add_child("H")
graph.children[0].children[1].add_child("I")
graph.children[0].children[1].add_child("J")
graph.children[2].children[0].add_child("K")

tree = BinaryTree("A")
tree.left = BinaryTree("B")
tree.right = BinaryTree("C")
tree.left.left = BinaryTree("D")
tree.left.right = BinaryTree("E")
tree.right.left = BinaryTree("F")
tree.right.right = BinaryTree("G")
tree.left.left.left = BinaryTree("H")
tree.left.left.right = BinaryTree("I")
tree.left.right.left = BinaryTree("J")
tree.left.right.right = BinaryTree("K")

print(depth_first_search(graph, []))
print(depth_first_search_tree(tree, []))
