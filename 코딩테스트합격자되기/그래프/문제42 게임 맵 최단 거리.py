# https://school.programmers.co.kr/learn/courses/30/lessons/1844
# BFS를 사용하여 풀기
# 큐는 큐에 넣을때 방문을 표시한다.

from collections import deque

def solution(maps):
    x = len(maps[0])
    y = len(maps)

    visited = [[0] * x for _ in range(0, y)]
    queue = deque()
    def bfs(start):
        visited[start[1]][start[0]] = 1
        queue.append(start)

        if start[1] == y and start[0] == x:
            return

        while queue:
            x_, y_ = queue.popleft()
            for i, j  in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                nx, ny = x_+i, y_+j
                if 0<= nx < x and 0 <= ny < y and maps[ny][nx] != 0 and visited[ny][nx] == 0:
                    queue.append((nx, ny))
                    visited[ny][nx] = visited[y_][x_] + 1


    bfs((0,0))

    if visited[y-1][x-1] == 0:
        return -1
    else:
        return visited[y-1][x-1]


# maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]
print(solution(maps))