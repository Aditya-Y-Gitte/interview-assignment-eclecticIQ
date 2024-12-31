from collections import deque

def isValid(cur_row, cur_col, row_len, col_len):
    '''
        isValid function: checks is the current row,col => cell is in grid returns True if in else False
        params: current row, 
                current column, 
                row length, 
                col length
    '''
    return 0 <= cur_row < row_len and 0 <= cur_col < col_len


def dfs(grid, cur_row, cur_col, visited, directions):
    '''
        dfs function: returns all cells adjacent to current cell marked 1.
        params: grid, 
                current row, 
                current column, 
                visited : set of visited cells i.e 1st iland cells, 
                directions: to go to adjacent cells
    '''
    if not isValid(cur_row, cur_col, len(grid), len(grid[0])) or grid[cur_row][cur_col] != 1 or (cur_row, cur_col) in visited:
        return
    visited.add((cur_row, cur_col))
    for dr, dc in directions:
        dfs(grid, cur_row + dr, cur_col + dc, visited, directions)



def bfs(grid, visited, row_len, col_len, directions):
    '''
        bfs function: returns minimum distance between ilands
        params: grid, 
                visited: set of visited cells i.e 1st iland cells, 
                current row, 
                current column,
    '''
    
    q = deque(visited)
    distance = 0
    
    while q:
        for i in range(len(q)):
            cur_row, cur_col = q.popleft()
            for dr, dc in directions:
                new_row, new_col = cur_row + dr, cur_col + dc
                if not isValid(new_row, new_col, row_len, col_len) or (new_row, new_col) in visited:
                    continue
                if grid[new_row][new_col] == 1:
                    return distance
                q.append((new_row, new_col))
                visited.add((new_row, new_col))
        distance += 1
    
    return distance

def shortestBridge(grid):
    '''
       shortestBridge function: returns shortestBridge length/cost
       params: grid
    '''
    row_len, col_len = len(grid), len(grid[0])
    visited = set()
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    for i in range(row_len):
        for j in range(col_len):
            if grid[i][j] == 1 and (i, j) not in visited:
                dfs(grid, i, j, visited, directions)
                break
        if visited:
            break
    
    return bfs(grid, visited, row_len, col_len, directions)



grid = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 0, 1],
    [0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0]
]
print(shortestBridge(grid))