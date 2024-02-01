n = int(input())

lsts = []
for _ in range(n):
    lst = str(input())
    lsts.append(lst)

for lst in lsts:
    stack = []
    for s in lst:
        if s == "(":
            stack.append(s)
        elif s == ")":
            if stack:
                stack.pop()
            else:
                print("NO")
                break
    else:
        if not stack:
            print("YES")
        else:
            print("NO")


