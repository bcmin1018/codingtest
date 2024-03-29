answer = 0
def solution(k, dungeons):
    visited = [0] * len(dungeons)

    def dfs(k, dungeons, cnt):
        global answer
        answer = max(answer, cnt)
        for i in range(len(dungeons)):
            if visited[i] == 0 and dungeons[i][0] <= k:
                visited[i] = 1
                dfs(k-dungeons[i][1], dungeons, cnt+1)
                visited[i] = 0

    dfs(k, dungeons, 0)
    return answer




# k = 80
# k = 8
k = 10
# dungeons = 	[[80,20],[50,40],[30,10]]
# dungeons = [[7, 3], [5, 4], [1, 1]]
dungeons = [[9, 2], [10, 3], [7, 3], [5, 4], [1, 1]]
print(solution(k, dungeons))