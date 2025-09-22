# bfs_and_dfs.py

from tree_utils import TreeNode

nodes = [1, 6, 5, 8, 10]

node_0 = TreeNode(1)
node_1 = TreeNode(6)
node_2 = TreeNode(5)
node_3 = TreeNode(8)
node_4 = TreeNode(10)
node_0.left = node_1
node_0.right = node_2
node_1.left = node_3
node_1.right = node_4

def dfs(root):
    if root is None:
        return
    print(root.val)
    dfs(root.left)
    dfs(root.right)
    

# FIFO collection
from collections import deque

def bfs(root):
    if root is None: # empty tree: nothing to traverse
        return
    
    queue = deque([root]) # initialize deque with `root`, euivalent `queue.append(root)`

    while queue:
        node = queue.popleft() # O(1) dequeue from left
        print(node.val) # visit the current node
        if node.left: # enqueue left child if it exists
            queue.append(node.left) # O(1) enqueue to the right
        if node.right: # enqueue right child if it exists
            queue.append(node.right)


def diameterOfBinaryTree(root) -> int:
    res = 0

    def dfs(root):
        nonlocal res

        if not root:
            return 0
        left = dfs(root.left)
        right = dfs(root.right)
        res = max(res, left + right)
        height = 1 + max(left, right)
        print(f"node {root.val}: diameter is {res}, height is {height}")
        
        return height

    dfs(root)
    return res

print("Breadth-First Search")
bfs(node_0)
print()
print("Depth-First Search")
dfs(node_0)
print()
diameterOfBinaryTree(node_0)