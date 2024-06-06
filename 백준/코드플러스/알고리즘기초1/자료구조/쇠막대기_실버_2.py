# https://www.acmicpc.net/problem/10799

text = input()
stack = []
answer = 0
for i in range(len(text)):
    if text[i] == "(":
        stack.append(text[i])
    else:
        if text[i-1] == "(":
            stack.pop()
            answer += len(stack)
        else:
            stack.pop()
            answer += 1
print(answer)