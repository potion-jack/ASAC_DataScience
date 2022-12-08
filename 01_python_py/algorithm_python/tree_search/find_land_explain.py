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
"""

from collections import deque
# deque : appendleft popleft 가 가능하여 가장 앞에것을 빼고 이동하는 비용이 없다

def bfs_ice_deque(row,col):
    # 입력을 받은 현 위치에서 움직일 수 있나 없나
    if graph[row][col] == 0: # 얼음을 얼릴 수 있고, 이동이 가능
        # 여기서 이동할 수 있는 위치 -> 방문할 곳 To_visit_list
        need_visit = deque([[row,col]])
        # 시작점에 대한 체크 1로 표시
        graph[row][col] = 1
        # 가능한 부분 이동
        # 일단 루프
        while True:
            # 종료할지 -> 더이상 움직일 곳이 없는 상황
            if not need_visit:
                return 1 # 일단 시작했음 (덩어리는 있다)
            else: # bfs : queue popleft (fistcome firstout)
                row, col = need_visit.popleft()
                # 여기서 LRUD (left_right_up_down)
                for dx,dy in [[0,1],[0,-1],[1,0],[-1,0]]:
                    # 가능한 4가지 경우들에 대해서 체크
                    if (0<= row+dy <= n-1) and (0<=col+dx<=m-1):
                        if graph[row+dy][col+dx] == 0:

                            need_visit.append([row+dy,col+dy]) # 시작 포인트들 지정

                            graph[row+dy][col+dx] = 1 # 시작포인트 들은 다 다녀갔으니.
            # 더 해야할지


    else:
        return 0
