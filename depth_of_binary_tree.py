# https://neetcode.io/problems/depth-of-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# time complexity O(n): visit all nodes
def maxDepth(self, root) -> int:
    if root is None:
        return 0
    return 1 + max(self.maxDepth(root.right), self.maxDepth(root.left))