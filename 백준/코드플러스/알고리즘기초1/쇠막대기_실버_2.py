# https://www.acmicpc.net/problem/10799

text = list(input())
stack = []
answer = 0
for t in text:
    if t == "(":
        stack.append(t)
    else:
        if stack[-1] == "(":
            stack.pop()
            # 레이저 발사


