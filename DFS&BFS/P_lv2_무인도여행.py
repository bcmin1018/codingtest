import sys
limit_number = 10000
sys.setrecursionlimit(limit_number)

def solution(maps):
    answer = []
    w, h = len(maps[0]), len(maps)
    visited = [[0] * w for _ in range(0, h)]

    def dfs(node):
        x, y = node[0], node[1]
        visited[y][x] = 1
        total_food = int(maps[y][x])

        for i, j in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            n_x, n_y = x + i, y + j
            if 0 <= n_x < w and 0 <= n_y < h and maps[n_y][n_x] != "X" and visited[n_y][n_x] == 0:
                visited[n_y][n_x] = 1
                total_food += dfs((n_x, n_y))
        return total_food

    for i in range(0, w):
        for j in range(0, h):
            if maps[j][i] != "X" and visited[j][i] == 0:
                food = dfs((i, j))
                if food > 0:
                    answer.append(food)
    if answer:
        return sorted(answer)
    else:
        return [-1]

maps = ["X591X","X1X5X","X231X", "1XXX1"]
print(solution(maps))