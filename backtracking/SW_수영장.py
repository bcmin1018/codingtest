# https://www.youtube.com/watch?v=NjrQhNHOI-g&list=PLodgw23vNd_U66omABrprSwJBZhKPFGMM&index=5
# https://swexpertacademy.com/main/identity/anonymous/loginPage.do
import sys
sys.stdin = open('input.txt')

def dfs(m, sm):
    global ans

    # loop를 돌다가 sm이 ans 보다 크면 더 이상 dfs를 하지 않고 빠져나온다.
    if ans <= sm:
        return

    # 12월이 지나면 결과를 return
    if m > 12:
        ans = min(ans, sm)
        return

    # 일, 월, 분기, 1년 단위로 선택 하도록 한다.
    # 1 ~ 12 각 달에서 일, 월, 분기, 1년 금액 중 어떤 것으로 선택 할지 분기 처리한다.
    # ex) 1~11월 까지 일권 + 12월 1년권
    dfs(m + 1, sm + plan[m] * price[0])
    dfs(m + 1, sm + price[1])
    # 분기: 1, 4, 7, 10
    dfs(m + 3, sm + price[2])
    dfs(m + 12, sm + price[3])


T = int(input())
for test_case in range(1, T+1):
    price = list(map(int, input().split()))
    plan = [0] + list(map(int, input().split()))

    # 1. 백트래킹 사용
    # ans = 3000 * 12
    # dfs(1, 0)

    # 2. 그리디한 방법
    D = [0] * 13
    # 가능한 4가지 방법중 i달의 최소 비용
    for i in range(1, 13):
        mn = D[i-1] + plan[i] * price[0]  ##일일권
        mn = min(mn, D[i-1] + price[1])
        if i > 3:
            mn = min(mn, D[i-3] + price[2])
        if i > 12:
            mn = min(mn, D[i-12] + price[3])

        D[i] = mn
    ans = D[12]
    print(f'#{test_case} {ans}')