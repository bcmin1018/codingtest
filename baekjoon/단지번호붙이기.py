# https://www.acmicpc.net/problem/2667

N = int(input())  # 가로 세로 길이
chk = [[0] * N for _ in range(N)]
dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]
house = []


def dfs(x, y):
    result = 1
    chk[y][x] = 1
    for i in range(4):
        xx, yy = x + dx[i], y + dy[i]
        if xx <= -1 or xx >= N or yy <= -1 or yy >= N:
            continue
        if house[yy][xx] == 0 or chk[y][x]: # house에 없거나 이미 방문한곳
            chk[y][x] = 1
            continue
        result += dfs(xx, yy)
    return result


def process():
    for _ in range(N):
        w = list(map(int, input()))
        house.append(w)
    answer = []
    for i in range(0, N):
        for j in range(0, N):
            if chk[j][i] == 1:
                continue
            answer.append(dfs(j,i))

    answer.sort()
    print(len(answer))
    for i in range(len(answer)):
        print(answer[i])




process()
