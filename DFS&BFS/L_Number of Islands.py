# https://leetcode.com/problems/number-of-islands/
# 군집화, 1이 연결된 지역이 한개의 섬
# bfs로 풀이

class Solution(object):
    def numIslands(self, grid):
        self.cnt = 0
        self.m = len(grid) # 세로
        self.n = len(grid[0]) # 가로
        self.v = [[0] * self.n for _ in range(self.m)]
        self.gridInt = []
        for row in grid:
            self.gridInt.append(list(map(int, row)))
        for y in range(self.m):
            for x in range(self.n):
                if self.v[y][x] == 0 and self.gridInt[y][x] == 1:
                    self.cnt += 1
                    self.v[y][x] = 1
                    self.bfs(x, y)
        return self.cnt

    def bfs(self, n, m):
        q = []
        q.append((n, m))
        while q:
            cx, cy = q.pop(0)
            for i, j in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                ny = cy + i
                nx = cx + j
                if 0<= ny < self.m and 0<= nx < self.n and self.v[ny][nx] == 0 and self.gridInt[ny][nx] == 1:
                    self.v[ny][nx] = 1
                    q.append((nx, ny))



if __name__ == "__main__":
    grid = [["1","1","1","1","1","1","1"]]
    a = Solution()
    print(a.numIslands(grid))





