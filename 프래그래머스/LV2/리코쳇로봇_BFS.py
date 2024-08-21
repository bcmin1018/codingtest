# 최소 경로라고 문제에 있으니 BFS로 접근
# 최대 시간 복잡도는 100 * 100 이니까 최대 10000 개의 노드를 돌면서 상하좌우 40000번을 방문한다. 따라서 O(50000)
# 상, 하, 좌, 우 이동
from collections import deque

def solution(board):
    answer = 0
    x, y = len(board[0]), len(board),
    board = [list(b) for b in board]
    v = [[0] * x for _ in range(y)]
    print(board)
    # print(v)
    def bfs(node):
        q = deque()
        v[node[0]][node[1]] = 1
        q.append(node)
        while q:
            i, j = q.popleft()
            if board[i][j] == 'G':
                return

            for ii, jj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ni, nj = i + ii, j + jj
                if 0<=ni<y and 0<=nj<x and board[ni][nj] != 'D  ' and v[ni][nj] == 0:
                    v[ni][nj] = v[i][j] + 1
                    q.append((ni, nj))


    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 'R':
                bfs((i, j))
    print(v)
    return answer


test = ["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]
solution(test)