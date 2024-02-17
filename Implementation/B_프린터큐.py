# https://www.acmicpc.net/problem/1966
from collections import deque

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    print_pool = deque([(i, int(p)) for i, p in enumerate(input().split())])

    answer = 0
    while True:
        # 현재 상태에서 가장 큰 수를 찾는다.
        max_ = max(print_pool, key=lambda x: x[1])
        # 가장 큰수와 큐의 맨 앞에 있는 수를 비교해서 다르면 순서를 바꾼다.
        if max_[1] != print_pool[0][1]:
            print_pool.append(print_pool.popleft())
        # 가장 큰수와 큐의 맨 앞에 있는 수가 같다면 찾으려는 인덱스의 값인지 확인한다.
        elif max_[1] == print_pool[0][1]:
            # 찾으려는 인덱스이면 answer+=1 하고 while를 break
            if max_[0] == M:
                print_pool.popleft()
                answer +=1
                break
            # 그렇지 않으면 큐의 맨앞의 값을 pop한다.
            else:
                print_pool.popleft()
                answer += 1
    print(answer)
