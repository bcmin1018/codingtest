#https://www.acmicpc.net/problem/14426

# 입력 문자열의 접두사를 모두 찾아 hash 테이블로 만든다. (중복 무관) 첫번째 자리를 key로 하고 모든 접두사를 value로 한다.
# coding이면 c의 key를 찾아 coding 문자열이 있는지 탐색
from collections import defaultdict

# N, M = map(int, input().split())
#
# inputs, targets = [], []
# for _ in range(0, N):
#     inputs.append(input())
# for _ in range(0, M):
#     targets.append(input())
#
# dic = defaultdict(set)
# for input_ in inputs:
#     for i in range(1, len(input_)):
#         dic[input_[0]].add(input_[0:i])
#
# answer = 0
# for t in targets:
#     print(t[0])
#     if t in dic[t[0]]:
#         answer+=1
# print(answer)


## 5% 에서 계속 틀렸다가 나오는데 이유를 모르겠다. 다른 코드를 참고하여 아래와 같이 변경했다. with startwith
from collections import defaultdict
import sys

input = sys.stdin.readline
N, M = map(int, input().split())

dic = defaultdict(list)
targets = []
for _ in range(0, N):
    input_ = input().strip()
    dic[input_[0]].append(input_)

for _ in range(0, M):
    targets.append(input().strip())

answer = 0
for i in range(M):
    for w in dic[targets[i][0]]:
        if w.startswith(targets[i]):
            answer += 1
            break
print(answer)







