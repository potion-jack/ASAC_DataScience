grid = [
    ["1","1","0","0","1"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
]
def dfs(row,col):
    n = len(grid)
    m = len(grid[0])
    if grid[row][col] == '0':
        return False

    elif grid[row][col] == '1':
        need_visit = [[row,col]]
        grid[row][col] = '0'
        while need_visit:
            row,col = need_visit.pop()
            for drow,dcol in [[1,0],[-1,0],[0,1],[0,-1]]:
                if (0 <= row+drow) & (row+drow <= n-1) & (0 <= col+dcol) & (col+dcol <= m-1):
                    dfs(row+drow,col+dcol)
        return True

count = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if dfs(i,j):
            count += 1
print(count)

