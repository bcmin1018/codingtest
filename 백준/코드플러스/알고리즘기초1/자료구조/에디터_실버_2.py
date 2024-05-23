# https://www.acmicpc.net/problem/1406
s = list(input())
n = int(input())
c_idx = len(s)
for _ in range(n):
    input_ = list(map(str, input().split()))
    if input_[0] == "L":
        if c_idx == 0:
            continue
        c_idx -= 1
    elif input_[0] == "D":
        if c_idx == len(s):
            continue
        c_idx += 1
    elif input_[0] == "B":
        del s[c_idx]
    elif input_[0] =="P":
        if c_idx == len(s):
            s.extend(input_[1])
        else:
            tmp = s[c_idx:]
            s[c_idx] = input_[1]
            s.extend(tmp)
            c_idx += 1
print(s)
