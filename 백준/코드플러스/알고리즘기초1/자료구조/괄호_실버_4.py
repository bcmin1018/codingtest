n = int(input())
for _ in range(n):
    vps = list(input())
    stack = []
    VPS = True
    for v in vps:
        if v == "(":
            stack.append(v)
        else:
            if len(stack) == 0:
                VPS = False
                break
            stack.pop()

    if len(stack) > 0:
        VPS = False

    if VPS:
        print("YES")
    else:
        print("NO")


