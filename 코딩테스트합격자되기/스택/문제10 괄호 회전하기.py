def solution(s):
    stack = []
    answer = 0
    for i in range(len(s)):
        for j in range(len(s)):
            c = (i + j) % len(s)

            if s[c] == "[" or s[c] == "(" or s[c] == "{":
                stack.append(s[c])
            else:
                if not stack: # ], ), } 가 왔는데 stack이 비어있으면 종료
                    break
                elif stack:
                    if s[c] == "]" and stack[-1] == "[":
                        stack.pop()
                    elif s[c] == ")" and stack[-1] == "(":
                        stack.pop()
                    elif s[c] == "}" and stack[-1] == "{":
                        stack.pop()
                    else:
                        break
        else:
            if not stack:
                answer+=1
    return answer

s = '}]()[{'
print(solution(s))