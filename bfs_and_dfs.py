# bfs_and_dfs.py


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

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
    # empty tree: nothing to traverse
    if root is None:
        return
    
    # initialize deque with `root`
    queue = deque([root])

    # process nodes level by level
    while queue:
        # O(1) dequeue from left
        node = queue.popleft()   
        # visit the current node
        print(node.val)

        # enqueue left child if it exists
        if node.left:
            # O(1) enqueue to the right
            queue.append(node.left)

        # enqueue right child if it exists
        if node.right:
            queue.append(node.right)

    
print("Breadth-First Search")
bfs(node_0)
print()
print("Depth-First Search")
dfs(node_0)