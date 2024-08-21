# 최소 경로라고 문제에 있으니 BFS로 접근
# 최대 시간 복잡도는 100 * 100 이니까 최대 10000 개의 노드를 돌면서 상하좌우 40000번을 방문한다. 따라서 O(50000)
# 상, 하, 좌, 우 이동
from collections import deque

def solution(board):
    x, y = len(board[0]), len(board),
    board = [list(b) for b in board]
    v = [[0] * x for _ in range(y)]

    def bfs(node):
        answer = 0
        q = deque()
        v[node[0]][node[1]] = 1
        q.append(node)
        while q:
            i, j, level = q.popleft()
            if board[i][j] == 'G':
                return level

            for ii, jj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                now_i, now_j = i, j
                while True:
                    next_i, next_j = now_i+ii, now_j+jj
                    # 장애물이나 맨끝에 도착하면 스탑
                    # 끝까지 가면 방문 표시한다.
                    # 끝까지 간 좌표를 큐에 넣는다.
                    if 0 <= next_i < y and 0 <= next_j < x and board[next_i][next_j] != 'D':
                        now_i, now_j = next_i, next_j
                        continue
                    break
                if 0 <= now_i < y and 0 <= now_j < x and v[now_i][now_j] == 0:
                    v[now_i][now_j] = 1
                    q.append((now_i, now_j, level+1))

    answer = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 'R':
                answer = bfs((i, j, 0))
    if answer is None:
        return -1
    return answer


# test = ["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]
test = [".D.R", "....", ".G..", "...D"]
print(solution(test))