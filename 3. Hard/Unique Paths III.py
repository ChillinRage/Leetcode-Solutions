def uniquePathsIII(grid):
        
    def find_obstacles_and_start():
        nonlocal grids
            
        start_row = 0
        start_col = 0
            
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:    # found start point
                    start_row = r
                    start_col = c
                elif grid[r][c] == -1: # found obstacle
                    grids -= 1         # reduce available moves
            
        return (start_row, start_col)
        
    def traverse(r, c, steps):
        nonlocal paths
        nonlocal grid
            
        # out of bounds
        if (r < 0) or (c < 0) or (r == row) or (c == col):
            return
            
        # already traversed before or blocked
        elif grid[r][c] == -1:
            return
            
        # currently at goal
        elif grid[r][c] == 2:
            # traversed through available grids
            if steps == grids:
                paths += 1
                    
            return
        else:
            grid[r][c] = -1 # current grid traversed
            traverse(r - 1, c, steps + 1) # move up
            traverse(r + 1, c, steps + 1) # move down
            traverse(r, c - 1, steps + 1) # move left
            traverse(r, c + 1, steps + 1) # move right
            grid[r][c] = 0
                
            return 
            
    row = len(grid)
    col = len(grid[0])
        
    grids = row * col  # fixed no. of cells
    paths = 0
        
    start_row, start_col = map(int, find_obstacles_and_start())
    grid[start_row][start_col] = 0
        
    traverse(start_row, start_col, 1)
        
    return paths
