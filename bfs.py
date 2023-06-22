from collections import deque

class Solution:
    def orangesRotting(self, grid) -> int:
        x = len(grid[0])
        y = len(grid)
        visited = [[0] * x for _ in range(y)]
        cnt = 0
        q = deque()
        for i in range(y):
            for j in range(x):
                if grid[i][j] == 2:
                    visited[i][j] = 1
                    q.append((j, i))
                elif grid[i][j] == 1:
                    cnt += 1
        while q:
            cx, cy = q.popleft()
            for i, j in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                nx, ny = cx + i, cy + j
                if 0 <= nx < x and 0 <= ny < y and visited[ny][nx] == 0 and grid[ny][nx] == 1:
                    visited[ny][nx] += visited[cy][cx] + 1
                    q.append((nx, ny))
                    cnt -= 1
        if cnt == 0:
            return visited[cy][cx] - 1
        return -1

if __name__ == "__main__":
    a = Solution()
    print(a.orangesRotting([[2,1,1],[0,1,1],[1,0,1]]))