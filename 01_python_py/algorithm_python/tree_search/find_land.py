"""
육지를 찾아라(탐색)

예제1)
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

예제2)
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

-> 큰 틀에서는 counting prob
+ 덩어리를 어떻게 판별할 것인가?

상하좌우에 대한 operation

구현 : dfs bfs 둘다 가능
dfs : stack + recursive
bfs : queue

"""
grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]

# row,col 위치에서 시작한다면,
# mine was df bfs(arr,st)
# 입력 시작위치 row,col을 받음
# 출력 : 시작점에서 이동이 가능한 것들 끝나면 1로 출력 , 못하면 0으로 출력


from collections import deque


def bfs_ice_deque(row, col):
    if graph[row][col] == 0:
        need_visit = deque([[row, col]])
        graph[row][col] = 1
    while True:
        if not need_visit:  # need_visit이 없으면
            return 1  # 여기서 더 찾지않고 종료
        else:
            row, col = need_visit.popleft()
            for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                if (0 <= row + dy <= n - 1) and (0 <= col + dx <= m - 1):
                    if graph[row + dy][col + dx] == 0:
                        need_visit.append([row + dy, col + dy])
                        graph[row + dy][col + dx] = 1
    else:
        return 0
