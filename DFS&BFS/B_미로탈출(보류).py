# https://school.programmers.co.kr/learn/courses/30/lessons/159993
# 해당 문제에서는

from collections import deque

def solution(maps):
    x = len(maps[0])
    y = len(maps)

    visited = [[0] * x for _ in range(0, y)]
    queue = deque()
    def bfs(start, flag, cost):
        queue.append((start, flag, cost))
        visited[start[1]][start[0]] = 1
        while queue:
            start, flag, cost = queue.popleft()
            x_, y_ = start[0], start[1]
            if maps[y_][x_] == flag:
                return cost

            for w, l in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                nx, ny = x_+ w, y_+ l
                if 0 <= nx < x and 0 <= ny < y and maps[ny][nx] != "X" and visited[ny][nx] == 0 :
                    queue.append(((nx, ny), flag, cost+1))
                    visited[ny][nx] = 1
        return -1

    def do_search(start, flag):
        for yy in range(0, y):
            for xx in range(0, x):
                if maps[yy][xx] == start:
                    return bfs((xx, yy), flag, 0)


    path1 = do_search("S", "L")
    queue = deque()
    path2 = do_search("L", "E")

    if path1 == -1 or path2 == -1:
        return -1
    else:
        return path1 + path2

maps = ["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"]
print(solution(maps))