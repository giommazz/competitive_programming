# number_of_islands.py
# Neetcode: https://neetcode.io/problems/count-number-of-islands?list=neetcode150

"""
Given a 2D grid grid where '1' represents land and '0' represents water, count and return the number of islands.
An island is formed by connecting adjacent lands horizontally or vertically and is surrounded by water.
You may assume water is surrounding the grid (i.e., all the edges are water).

Examples:
- grid: [
    ["0","1","1","1","0"], ["0","1","0","1","0"], ["1","1","0","0","0"], ["0","0","0","0","0"]
  ]
  -> 1
- grid: [
    ["1","1","0","0","1"], ["1","1","0","0","1"], ["0","0","1","0","0"], ["0","0","0","1","1"]
  ]
  -> 4

Constraints: 
- 1 <= rows, cols <= 100;
- cells in {'0','1'}.
"""

def numIslands(grid):
    """
    Count islands via DFS.

    Input:
    - grid: List[List[str]]; '1' land, '0' water.

    Output:
    - int: island count

    Complexity:
    - Time O(n*m): visit each cell once.
    - Space O(n*m): worst-case recursion depth.

    Edge cases: 
    - empty grid -> 0
    - no land -> 0
    - all land -> 1
    - 1 row/col.
    """

    # Guard for empty input; no cells means no islands.
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])

    def dfs(r, c):
        """
          DFS: sink all land connected to (r, c).
        """
        # Base case: stop if out of bounds or cell is water.
        if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == "0":
            return
        # Mark cell as water to avoid revisiting.
        # Note: this mutates grid in-place. If preserving grid is required, pass deep copy.
        grid[r][c] = "0"
        # Explore four cardinal neighbors (no diagonals)
        dfs(r+1, c)
        dfs(r-1, c)
        dfs(r, c+1)
        dfs(r, c-1)

    islands = 0
    for r in range(rows):
        for c in range(cols):
            # Encounter land => new island.
            if grid[r][c] == "1":
                # Count island, then sink to avoid recounting cells.
                islands += 1
                dfs(r, c)
    return islands

grid1 = [
    ["0","1","1","1","0"],
    ["0","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
  ]
grid2 = [
    ["1","1","0","0","1"],
    ["1","1","0","0","1"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
  ]
grid3 = [
    ["1","0","1","0","1"],
    ["1","0","1","0","0"],
    ["1","1","1","0","1"],
  ]

print(numIslands(grid3))
