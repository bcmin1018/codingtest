from collections import deque

def solution(m, n, puddles):
    answer = 0
    queue = deque()
    visited = [[0 for _ in range(0, m+1)] for _ in range(0, n+1)]
    path = [[0 for _ in range(0, m+1)] for _ in range(0, n+1)]
    def bfs(start):
        queue.append(start)
        x, y = start[0], start[1]
        visited[y][x] = 1
        path[1][1] = 1
        while queue:
            x, y = queue.popleft()
            for i, j in [(1, 0), (0, 1)]:
                ni, nj = x+i, y+j
                if 0 <= ni < m+1 and 0 <= nj < n+1:
                    if [ni, nj] not in puddles:
                        if visited[nj][ni] == 0:
                            queue.append((ni, nj))
                            visited[nj][ni] = visited[y][x] + 1
                            path[nj][ni] = path[y][x]
                        elif visited[nj][ni] == visited[nj][ni]:
                            path[nj][ni] = (path[nj][ni] + path[y][x]) % 1000000007
    bfs((1,1))
    answer = path[n][m]
    return answer
m, n, puddles = 4, 3, [[2,2]]
print(solution(m, n, puddles))