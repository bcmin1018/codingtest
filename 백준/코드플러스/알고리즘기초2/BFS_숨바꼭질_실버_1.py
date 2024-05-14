from collections import deque

N, K = map(int, input().split())
cnt = 0
visited = [0] * K
queue = deque()
queue.append(N)
visited[N] = 1
while queue:
    n = queue.popleft()
    if n == K:
        break
    for x in [n+1, 2*n]:
        if visited[x] == 1:
            queue.append(x)
            cnt += 1
print(cnt)
