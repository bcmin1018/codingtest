# https://www.acmicpc.net/problem/1697
from collections import deque
import sys
N, K = map(int, sys.stdin.readline().split())
MAX = 10 ** 5
visited = [0] * (MAX+1)

queue = deque()
queue.append(N)
while queue:
    n = queue.popleft()
    if n == K:
        break
    for x in [n+1, n-1, 2*n]:
        if 0<=x<=MAX and visited[x] == 0:
            queue.append(x)
            visited[x] = visited[n] + 1
print(visited[K])
