from collections import deque
import sys
read = sys.stdin.readline

n, m, v = map(int, read().split())
print(n,m,v)

graph = [[0] * (n + 1) for _ in range(n + 1)]

visit_list = [0] * (n + 1)

visit_list2 = [0] * (n + 1)

for _ in range(m):
  a, b = map(int, read().split())
  graph[a][b] = graph[b][a] = 1
print(graph)
