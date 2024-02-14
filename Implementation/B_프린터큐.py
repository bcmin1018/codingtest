# https://www.acmicpc.net/problem/1966

from collections import deque

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())

    print_pool = [int(p) for p in input().split()]

    # 우선순위 높은대로 정렬

    if print_pool.index(max(print_pool)) == len(print_pool):

