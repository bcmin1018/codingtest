# https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDN86AAXw5UW6&subjectId=AWOVF-WqqecDFAWg
# 집합 A를 1차원 배열에 놓고 포함 시킬 것인지 아닌지를 판별한다.
# n은 배열의 인덱스를 나타낸다.

import sys
sys.stdin = open("input.txt", "r")

def dfs(n, sum_, cnt):
    global ans

    # 가지치기: 가장 마지막에 고민
    if sum_> K : # 이미 초과했고 음수가 없음.
        return

    if n == N: # 종료 조건
        if sum_ == K and cnt == CNT:
            ans += 1
        return

    dfs(n+1, sum_ + lst[n], cnt + 1 ) # 사용하는 것을 선택 하면 숫자를 더하고 cnt 를 1 증가 시킨다.
    dfs(n+1, sum_, cnt)


T = int(input())
for test_case in range(1, T+1):
    CNT, K = map(int, input().split())
    lst = [n for n in range(1, 13)]
    N = 12

    ans = 0
    dfs(0, 0, 0)
    print(ans)



