# https://www.acmicpc.net/problem/1406
import sys
# s = list(sys.stdin.readline())
# n = int(sys.stdin.readline())
# c_idx = len(s)
# for _ in range(n):
#     input_ = list(map(str, sys.stdin.readline().split()))
#     if input_[0] == "L": # 왼쪽
#         if c_idx == 0: # 커서가 맨 왼쪽에 있다면
#             continue
#         c_idx -= 1 # 왼쪽으로 커서 이동
#     elif input_[0] == "D": # 오른쪽
#         if c_idx == len(s): # 맨 왼쪽
#             continue
#         c_idx += 1 # 오른쪽으로 커서 이동
#     elif input_[0] == "B": # 왼쪽에 있는 문자 삭제
#         if c_idx == 0: # 맨 왼쪽이면 무시
#             continue
#         c_idx -= 1 # 왼쪽으로 커서 이동
#         del s[c_idx] # 삭제
#     elif input_[0] == "P": # 문자를 커서 왼쪽에 추가
#         if c_idx == len(s):  # 맨 마지막
#             s.extend(input_[1]) # 뒤에 추가
#         elif c_idx == 0: # 맨 앞에
#             tmp = s[c_idx:]
#             s[c_idx] = input_[1]
#             s = [s[0]] + tmp
#         else: # 중간
#             tmp = s[c_idx:]
#             s[c_idx] = input_[1]
#             s.extend(tmp)
#         c_idx += 1
# print("".join(s))

import sys
s = list(sys.stdin.readline().rstrip())
n = int(sys.stdin.readline())
t = []

for _ in range(n):
    cmd = list(sys.stdin.readline().split())
    if cmd[0] == "L":
        if s:
            t.append(s.pop())

    elif cmd[0] == "D":
        if t:
            s.append(t.pop())

    elif cmd[0] == "B":
        if s:
            s.pop()

    else:
        s.append(cmd[1])

s.extend(reversed(t))
print("".join(s))