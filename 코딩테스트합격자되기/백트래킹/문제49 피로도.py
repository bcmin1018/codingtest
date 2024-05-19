#https://school.programmers.co.kr/learn/courses/30/lessons/87946
# 모든 경우의 수를 완전탐색 하되 효율성을 위해 백트래킹을 한다.
# 백트레킹 조건은 현재 피로도가 던전 입장 피로도 포다 낮으면 백트래킹한다.

def solution(k, dungeons):
    v = [0] * len(dungeons)
    def dfs(k, n, cnt):
        max_cnt = cnt
        for i in range(len(dungeons)):
            if v[i] == 0 and k >= dungeons[i][0]:
                v[i] = 1
                max_cnt = max(max_cnt, dfs(k-dungeons[i][1], n+1, cnt + 1))
                v[i] = 0
        return max_cnt

    ans = dfs(k, 0, 0)
    return ans

print(solution(80, [[80,20],[50,40],[30,10]]))