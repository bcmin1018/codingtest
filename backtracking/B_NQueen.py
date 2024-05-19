# https://www.acmicpc.net/problem/9663
# https://www.youtube.com/watch?v=HRwFgtiqHH0
# https://www.acmicpc.net/problem/9663

# 체스판에 몇개를 배치해야하나

# 가능한 좌표의 위치를 찾기 위해 3가지의 배열을 만들어야 한다.
# 룩업 테이블 사용
# 같은 열에 체스가 있는지 확인하는 배열
# 대각선 오른쪽 위에 체스가 있는지 확인 하는 배열
# 대각선 왼쪽 위에 체스가 있는지 확인 하는 배열

# import sys
# sys.stdin = open("input.txt", "r")
#
# def dfs(n):
#     global ans
#     if n==N:
#         ans+=1
#         return
#
#     for j in range(N):
#         #  v1[j] 는 세로를 확인하기 위한 배열로 퀸을 둔 곳에 1로 표기한다.
#         if v1[j] == v2[n+j] == v3[n-j] == 0:
#             v1[j] = v2[n+j] = v3[n-j] = 1
#             dfs(n+1)
#             v1[j] = v2[n+j] = v3[n-j] = 0
#
# N = int(input())
#
# ans = 0
# v1 = [0] * N # 컬럼
# v2 = [0] * (N*2) # 우측 대각선,
# v3 = [0] * (N*2) # 좌측 대각선
# dfs(0)
# print(ans)


def solution(n):
    column_check = [0] * n
    right_check = [0] * (2 * n)
    left_check = [0] * (2 * n)
    answer = 0

    def dfs(step):
        nonlocal answer
        if step == n:  # 위에서 부터 몇열인지 확인한다.
            answer += 1
            return
        for j in range(n):
            if column_check[j] == right_check[step + j] == left_check[step - j] == 0:
                column_check[j] = right_check[step + j] = left_check[step - j] = 1
                dfs(step+1)
                column_check[j] = right_check[step + j] = left_check[step - j] = 0
    dfs(0)
    return answer


print(solution(4))
