def bfs(row,col):
    n = len(grid)
    m = len(grid[0])
    if grid[row][col] == '0':
        return False
    else:
        need_visit = [[row,col]]
        while need_visit:
            row,col = need_visit.pop()

            grid[row][col]='0'
            for drow,dcol in [[1,0],[-1,0],[0,1],[0,-1]]:
                if (0 <= row+drow) and (row+drow <= n-1) and (0 <= col+dcol) and (col+dcol <= m-1):
                    if grid[row+drow][col+dcol] == '1':
                        need_visit.append([row+drow,col+dcol])
                        grid[row+drow][col+dcol] = '0'
        return True
