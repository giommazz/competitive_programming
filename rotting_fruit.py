# rotting_fruit.py
# https://neetcode.io/problems/rotting-fruit?list=neetcode150

"""
You are given a 2-D matrix grid. Each cell can have one of three possible values:
- 0 representing an empty cell
- 1 representing a fresh fruit
- 2 representing a rotten fruit
Every minute, if a fresh fruit is horizontally or vertically adjacent to a rotten fruit, then the fresh fruit also becomes rotten.

Return the minimum number of minutes that must elapse until there are zero fresh fruits remaining. 
If one cannot rot all fresh fruit on the grid, return -1.
"""

from collections import deque
from typing import List

def orangesRotting(grid: List[List[int]]) -> int:
    """Return minutes needed to rot grid.

    Input:
    - grid: matrix 0 empty, 1 fresh, 2 rotten

    Output:
    - int: minutes; -1 when impossible
    
    Time: O(ROWS*COLS) because visit each cell once.
    Space: O(ROWS*COLS) because queue + seen can hold all cells.
    """

    def _count_fruit(grid, ROWS, COLS):
        """Count fresh fruit and seed queue.

        Input:
        - grid: orange matrix
        - ROWS: row count
        - COLS: column count

        Output:
        - fresh_fruit: fresh orange total
        - q: rotten frontier queue
        - seen: visited rotten set
        
        Time: O(ROWS*COLS) because sweep grid once.
        Space: O(ROWS*COLS) because queue/seen may store all cells.
        """
        fresh_fruit, q, seen = 0, deque(), set()
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    fresh_fruit += 1  # Count fresh orange
                if grid[row][col] == 2:
                    if (row, col) not in seen:
                        q.append([row, col])  # Seed BFS with rotten
                        seen.add((row, col))  # Record processed rotten

        return fresh_fruit, q, seen
    
    if grid:
        ROWS, COLS = len(grid), len(grid[0])
        fresh_fruit, q, seen = _count_fruit(grid, ROWS, COLS)

        def _update_queue(row, col):
            """Rot neighbor then enqueue.

            Input:
            - row: neighbor row index
            - col: neighbor column index

            Output:
            - None: mutate fresh_fruit, grid, q, seen
           
            Time: O(1) because handle single neighbor.
            Space: O(1) because no extra growth beyond shared structures.
            """
            # Use `fresh_fruit` defined in `orangesRotting` and mutate that -> "local" to `orangesRotting` & "global" for `_update_queue`
            # Needed because integers are immutable. Not needed for `grid`, `q`, `seen`: in-place mutations affect original objects
            nonlocal fresh_fruit
            grid[row][col] = 2  # Convert fresh to rotten
            fresh_fruit -= 1  # Track remaining fresh count
            if (row, col) not in seen:
                q.append([row, col])  # Push new rotten to BFS frontier
                seen.add((row, col))  # Avoid duplicate enqueue

        minutes = 0

        print(f"Initial queue: {q}")  # Debug initial rotten frontier
        while q:
            for _ in range(len(q)):
                row, col = q.popleft()
                if row-1>= 0 and grid[row-1][col] == 1:
                    _update_queue(row-1, col)
                if row+1<ROWS and grid[row+1][col] == 1:
                    _update_queue(row+1, col)
                if col-1>=0 and grid[row][col-1] == 1:
                    _update_queue(row, col-1)
                if col+1<COLS and grid[row][col+1] == 1:
                    _update_queue(row, col+1)
            minutes = minutes + 1 if len(q) > 0 else minutes  # Increment minute when next layer exists
            print(f"currently rotting fruit after {minutes} minutes: {q}")
            for i in range(ROWS):
                print(grid[i])
            print(f"Fresh fruit left: {fresh_fruit}")
            print()
        # impossible when fresh remain
        if fresh_fruit > 0:
            return -1
        return minutes
    
# grid = [[1,1,0],[0,1,1],[0,1,2]]
# grid = [[1,0,1],[0,2,0],[1,0,1]]
grid=[[2,1,1],[0,1,1],[1,0,1]]

print(orangesRotting(grid))
