# https://neetcode.io/problems/invert-a-binary-tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# solution from the website
# time complexity O(n): must visit all nodes
def invertTree(self, root):
    
    if not root:
        return None

    # Swap children
    root.left, root.right = root.right, root.left

    # Recursion on both subtrees
    # Invert left subtree
    self.invertTree(root.left)
    # Invert right subtree
    self.invertTree(root.right)

    return root
