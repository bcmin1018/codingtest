# https://www.acmicpc.net/problem/4949
# O(N) 시간복잡도

while True:
    sentence = str(input())
    if sentence == ".":
        break

    stack = []
    for word in sentence:
        if word == "(" or word == "[":
            stack.append(word)
        elif word == ")":
            if len(stack) != 0 and stack[-1] == "(":
                stack.pop()
            else:
                stack.append(word)
                break
        elif word == "]":
            if len(stack) != 0 and stack[-1] == "[":
                stack.pop()
            else:
                stack.append(word)
                break

    if len(stack) == 0:
        print("yes")
    else:
        print("no")

