# Problem
#   Write a function that takes in a Binary Tree and returns a list of its branch sums ordered from leftmost branch sum to rightmost branch sum.
#   A branch sum is the sum of all values in a Binary Tree branch. A Binary Tree branch is a path of nodes in a tree that starts at the root node and ends at any leaf node.
#   Each BinaryTree node has an integer value, a left child node, and a right child node. Children nodes can either be BinaryTree nodes themselves or None / null.
# Sample Input
#   tree =   1
#          /     \
#         2       3
#       /   \   /   \
#      4     5 6     7
#    /   \  /
#   8    9 10
# Sample Output
#   [15, 16, 18, 10, 11]

# Solution 1
#   * Time Complexity: O(n) -> n is the number of nodes in the tree
#   * Space Complexity: O(n) -> n is the number of nodes in the tree
def branch_sums(root):
    sums = []
    calculate_branch_sums(root, 0, sums)
    return sums


def calculate_branch_sums(node, running_sum, sums):
    if node is None:
        return
    new_running_sum = running_sum + node.value
    if node.left is None and node.right is None:
        sums.append(new_running_sum)
        return
    calculate_branch_sums(node.left, new_running_sum, sums)
    calculate_branch_sums(node.right, new_running_sum, sums)


# Solution 2
#   * Time Complexity: O(n) -> n is the number of nodes in the tree
#   * Space Complexity: O(n) -> n is the number of nodes in the tree
def branch_sums_iterative(root):
    sums = []
    stack = [{"node": root, "running_sum": 0}]
    while len(stack) > 0:
        node_info = stack.pop()
        node, running_sum = node_info["node"], node_info["running_sum"]
        if node is None:
            continue
        new_running_sum = running_sum + node.value
        if node.left is None and node.right is None:
            sums.append(new_running_sum)
            continue
        stack.append({"node": node.right, "running_sum": new_running_sum})
        stack.append({"node": node.left, "running_sum": new_running_sum})

    return sums


class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


binary_tree = BinaryTree(1)
binary_tree.left = BinaryTree(2)
binary_tree.right = BinaryTree(3)
binary_tree.left.left = BinaryTree(4)
binary_tree.left.right = BinaryTree(5)
binary_tree.right.left = BinaryTree(6)
binary_tree.right.right = BinaryTree(7)
binary_tree.left.left.left = BinaryTree(8)
binary_tree.left.left.right = BinaryTree(9)
binary_tree.left.right.left = BinaryTree(10)

print(branch_sums(binary_tree))
print(branch_sums_iterative(binary_tree))
