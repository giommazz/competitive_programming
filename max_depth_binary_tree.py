"""
Maximum Depth of Binary Tree (LeetCode)

found at: https://leetcode.com/explore/interview/card/top-interview-questions-easy/94/trees/555/

Given the root of a binary tree, return its maximum depth.
A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
Example: 
    Input: root = [3,9,20,null,null,15,7]
    Output: 3

This solution beats 12.43% of other submitted solutions
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root != None:
            return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        else:
            return 0
