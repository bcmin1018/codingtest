from collections import deque
def solution(maps):
    direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    n = len(maps) #세로
    m = len(maps[0]) #가로

    dist = [[-1] * m for _ in range(n)]

    def bfs(start):
        queue = deque([start])
        dist[start[0]][start[1]] = 1

        while queue:
            x, y = queue.popleft()
            for d in direction:
                nx, ny = x + d[0], y + d[1]
                if nx < 0 or nx >= m or ny < 0 or ny >= n:
                    continue

                if maps[ny][nx] ==0:
                    continue

                if dist[ny][nx] == -1:
                    queue.append([nx, ny])
                    dist[ny][nx] = dist[y][x] + 1
        return dist

    bfs([0,0])
    return dist[n-1][m-1]



