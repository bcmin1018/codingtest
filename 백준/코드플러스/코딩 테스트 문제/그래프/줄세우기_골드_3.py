# https://www.acmicpc.net/problem/2252
# 위상 정렬이라는 것을 배웠다. 싸이클이 없는 방향 그래프인 경우 위상 정렬을 사용하자.
# 위상 정렬은 기본적으로 큐를 사용하여 구현한다. 

from collections import deque

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
indegree = [0] * (N+1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

result = []
q = deque()
for i in range(1, N+1):
    if indegree[i] == 0:
        q.append(i)

while q:
    now = q.popleft()
    result.append(now)

    for i in graph[now]:
        indegree[i] -= 1

        if indegree[i] == 0:
            q.append(i)

for i in result:
    print(i, end=" ")