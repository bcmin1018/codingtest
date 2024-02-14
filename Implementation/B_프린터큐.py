# https://www.acmicpc.net/problem/1966

from collections import deque

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    print_pool = [int(p) for p in input().split()]

    lst = deque()
    for p in reversed(print_pool):
        lst.append(p)

    k = print_pool[M]
    top = max(print_pool)

    answer = 0
    while True:
        if top != lst[0]:
            lst.append(lst.popleft())

        elif top == lst[0]:
            lst.popleft()
            answer += 1



    #
    #
    #     if k == print_pool[-1] and k == top:
    #         answer += 1
    #         print(answer)
    #     else:
    #         print_pool.popleft()

    # 우선순위 높은대로 정렬

    # if print_pool.index(max(print_pool)) == len(print_pool):

