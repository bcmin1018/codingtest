class Solution(object):
    def __init__(self):
        self.size = 0

    def maxAreaOfIsland(self, grid):
        global v, X, Y, map, max_size
        Y = len(grid)
        X = len(grid[0])
        map = grid
        v = [[0 for _ in range(X)] for _ in range(Y)]
        max_size = 0
        # 0, 0 좌표 부터 맵을 순회 한다.
        for y in range(0, Y):
            for x in range(0, X):
                # 방문하지 않고 1인 경우 dfs 탐색에 들어간다.
                if v[y][x] == 0 and map[y][x] == 1:
                    self.dfs(x, y)
                    if self.size > max_size:
                        max_size = self.size
                        self.size = 0
                    else:
                        self.size = 0
        return max_size

    def dfs(self, x, y):
        # dfs 탐색 하는 곳은 방문한 곳이므로 1로 표기한다.
        v[y][x] = 1
        self.size += 1
        for i, j in ((1,0), (0,1), (-1,0), (0,-1)):
            nx, ny = x+i, y+j
            # 네 방면을 돌며 1이고 방문하지 않은 경우 dfs를 또 탐색한다. dfs 탐색을 마치면 빠져나와 다른 방향을 계속 순회한다.
            if 0<=nx<X and 0<=ny<Y and v[ny][nx] == 0 and map[ny][nx] == 1:
                self.dfs(nx, ny)

if __name__ == "__main__":
    grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
    # grid = [[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]
    # grid = [[1]]
    for i in grid:
        print(i)
    # a = Solution()
    # print(a.maxAreaOfIsland(grid))
