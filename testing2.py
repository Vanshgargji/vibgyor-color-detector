import random

def num_islands(grid):
    if not grid:
        return 0
    
    rows, cols = len(grid), len(grid[0])
    islands = 0

    def dfs(r, c):
        # Base case: if out of bounds or at a water cell ('0')
        if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == '0':
            return
        
        # Mark the current land cell as visited by flipping it to '0'
        grid[r][c] = '0'
        
        # Explore all 4 neighbors (Up, Down, Left, Right)
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                # Found a new island, start DFS to sink it
                islands += 1
                dfs(r, c)
    
    return islands

# Example Walkthrough:
example_grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]

print(f"Number of islands: {num_islands(example_grid)}")
