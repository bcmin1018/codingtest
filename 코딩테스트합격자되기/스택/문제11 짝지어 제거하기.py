
def solution(strings):
    stack = []
    for s in strings:
        if stack:
            if stack[-1] == s:
                stack.pop()
            else:
                stack.append(s)
        else:
            stack.append(s)

    if stack:
        return 0
    else:
        return 1

# s = "baabaa"
s = "cdcd"
print(solution(s))