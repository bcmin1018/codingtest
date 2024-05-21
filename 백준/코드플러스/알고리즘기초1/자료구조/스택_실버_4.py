#https://www.acmicpc.net/problem/10828
import sys
N = int(input())

stack = []
for _ in range(0, N):
    lst = sys.stdin.readline().split()
    func, num = "push", 0
    if len(lst) == 1:
        func = lst[0]
    else:
        func, num = lst[0], lst[1]
    if func == "push":
        stack.append(num)
    elif func == "pop":
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif func == "size":
        print(len(stack))
    elif func == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif func == "top":
        if len(stack) > 0:
            print(stack[-1])
        else:
            print(-1)
