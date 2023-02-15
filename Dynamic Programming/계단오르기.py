# https://www.acmicpc.net/problem/2579
# 최대값을 구하는 문제이므로 최대한 많은 계단을 밟아야하는 문제이다.

import sys
sys.stdin = open("input.txt", "r")

N = int(input()) # 계단의 수
s = [int(input()) for _ in range(N)]
dp = [0] * N
if len(s) <= 2: # 계단을 오를 수 있는 조건이 한개 또는 두개이기 때문에 두개 이하의 계단이 입력 되는 경우 그냥 모두 더한다. 모두 더한다는 의미는 계단을 한개씩 다 밟아서 간다는 뜻이다.
    print(sum(s))
else:
    dp[0] = s[0] # 첫번쨰 계단을 밟는다.
    dp[1] = s[0] + s[1] # 첫번쨰 계단 두번쨰 계단을 밟는다.
    for i in range(2, N):
        dp[i] = max(dp[i-3] + s[i-1] + s[i], dp[i-2] + s[i]) # 문제의 조건에서 첫번째, 두번쨰, 세번째, 계단을 연속적으로 밟을 수 없다. 따라서 최종 도착지 2번쨰 아래 계단에서 2칸을 바로 건너오는 방법과 3계단 전에서 2칸 올라오고 2칸을 올라오는 방법이 있다.
    print(dp[-1])



