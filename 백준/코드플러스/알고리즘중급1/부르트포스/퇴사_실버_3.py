# https://www.acmicpc.net/problem/14501
# 1일부터 7일 까지 순회하며 최적의 답을 그냥 잔인하게 찾아보자
# 주의 할 점은 상담 비용이 최우선이 아니라 상담 개수가 최우선이다.

N = int(input())
t_lst, p_lst = [], []
for _ in range(N):
    T, P = map(int, input().split())
    t_lst.append(T)
    p_lst.append(P)

last = N + 1
m_profit = []

for i in range(1, N+1):
    profit = 0
    day = i
    while True:
        day = day + t_lst[day]
        if day > N:
            break
        profit += p_lst[day]

    m_profit.append(profit)


print(max(m_profit))


