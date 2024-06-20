# https://www.acmicpc.net/problem/16928
from collections import deque

n, m = map(int, input().split())
board = [0] * 101
v = [0] * 101

ladder = dict()
snake = dict()
for _ in range(n):
    a, b = map(int, input().split())
    ladder[a] = b

for _ in range(m):
    a, b = map(int, input().split())
    snake[a] = b

def bfs():
    q = deque()
    q.append((1, 0))
    v[1] = 1
    while q:
        m, c = q.popleft()
        if m == 100:
            print(c)
            break

        for i in range(1, 7):
            new = m + i
            print(new)
            if v[new] == 0 and new in ladder:
                q.append((ladder[new], c+1))
                v[ladder[new]] = 1

            if v[new] == 0 and new in snake:
                q.append((snake[new], c+1))
                v[snake[new]] = 1

            if v[new] == 0 and board[new] < 100:
                q.append((new, c+1))
                v[new] = 1

bfs()