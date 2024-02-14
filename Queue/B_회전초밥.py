# https://www.acmicpc.net/problem/28107
from collections import deque
N, M = map(int, input().split())
dic = {}
for i in range(N):
    dic[i+1] = list(map(int, input().split()))
print(f'{dic}')

dq = deque()
sushi = list(map(int, input().split()))
for s in sushi:
    dq.append(s)
print(f'sushi : {dq}')


answer = [0] * (N+1)
for k in dic.keys():
    sushi_made = dq.popleft()
    print(f'now sushi is {sushi_made}')
    for p in range(1, N+1):
        if dic[p][0] == sushi_made:
            print(f'person no {p} match eat sushi')
            answer[p] +=1
            dic[p] = dic[p][1:]
            break
        else:
            print(f'person no {p} not match so skip')
            continue
print(*answer[1:])

