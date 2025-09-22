# tree_utils.py

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_small_testcase():
    node_0 = TreeNode(1)
    node_1 = TreeNode(6)
    node_2 = TreeNode(5)
    node_3 = TreeNode(8)
    node_4 = TreeNode(10)
    node_0.left = node_1
    node_0.right = node_2
    node_1.left = node_3
    node_1.right = node_4
    return node_0


"""
Example use:

      1
    /  \
   6    5
  / \
 8  10

"""