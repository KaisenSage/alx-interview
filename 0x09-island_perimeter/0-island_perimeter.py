#!/usr/bin/python3
"""
Island Perimeter module
"""

def island_perimeter(grid):
    """
    Returns the perimeter of the island described in grid.
    
    Args:
        grid: List of lists of integers where 0 represents water and 1 represents land.
    
    Returns:
        Perimeter of the island.
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Check all four possible directions
                # Up
                if i == 0 or grid[i-1][j] == 0:
                    perimeter += 1
                # Down
                if i == rows - 1 or grid[i+1][j] == 0:
                    perimeter += 1
                # Left
                if j == 0 or grid[i][j-1] == 0:
                    perimeter += 1
                # Right
                if j == cols - 1 or grid[i][j+1] == 0:
                    perimeter += 1
    
    return perimeter

