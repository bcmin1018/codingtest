# https://www.acmicpc.net/problem/9093
N = int(input())

for i in range(N):
    result = []
    ss = input().split()
    stack = []
    for s in ss:
        for s_ in list(s):
            stack.append(s_)
        while stack:
            t = stack.pop()
            result.extend(t)
        result.extend(" ")
    print(''.join(result))

