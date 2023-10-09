# Problem
#   Write a function that takes in a Binary Search Tree (BST) and a target integer value and returns the closest value to that target value contained in the BST.
#   You can assume that there will only be one closest value.
# Sample Input
#   tree =   10
#          /     \
#         5      15
#       /   \   /   \
#      2     5 13   22
#    /           \
#   1            14
#
#   target = 12
#
# Sample Output
#   13
# Solution
#   * Time Complexity: O(log(n)) -> n is the number of nodes in the tree and log(n) is the height of the tree
#   * Space Complexity: O(1)
def find_closest_value_in_bst(tree, target_number):
    # set closest to infinity
    closest = float("inf")
    current_node = tree

    while current_node is not None:
        if abs(target_number - closest) > abs(target_number - current_node.value):
            closest = current_node.value
        if target_number < current_node.value:
            current_node = current_node.left
        elif target_number > current_node.value:
            current_node = current_node.right
        else:
            break

    return closest


def find_closest_value_in_bst_recursive(tree, target_number):
    return find_closest_value_in_bst_recursive_helper(tree, target_number, float("inf"))


def find_closest_value_in_bst_recursive_helper(tree, target_number, closest):
    if tree is None:
        return closest
    if abs(target_number - closest) > abs(target_number - tree.value):
        closest = tree.value
    if target_number < tree.value:
        return find_closest_value_in_bst_recursive_helper(tree.left, target_number, closest)
    elif target_number > tree.value:
        return find_closest_value_in_bst_recursive_helper(tree.right, target_number, closest)
    else:
        return closest


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


tree = BST(10)
tree.left = BST(5)
tree.right = BST(15)
tree.left.left = BST(2)
tree.left.right = BST(5)
tree.left.left.left = BST(1)
tree.right.left = BST(13)
tree.right.right = BST(22)
tree.right.left.right = BST(14)
target_number = 12

result = find_closest_value_in_bst(tree, target_number)
print("closest value is: ", result)
