# https://www.youtube.com/watch?v=iDyzoCtblls&list=PLodgw23vNd_U66omABrprSwJBZhKPFGMM&index=3
import sys
sys.stdin = open('input.txt', 'r')




T = int(input())
for test_case in range(1, T+1):
    num, self_H = map(int, input().split())
    clerk_H = list(map(int, input().split()))
    dfs()