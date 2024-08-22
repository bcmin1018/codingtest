#https://www.acmicpc.net/problem/14426

# 입력 문자열의 접두사를 모두 찾아 hash 테이블로 만든다. (중복 무관) 첫번째 자리를 key로 하고 모든 접두사를 value로 한다.
# coding이면 c의 key를 찾아 coding 문자열이 있는지 탐색
from collections import defaultdict

N, M = map(int, input().split())

inputs, targets = [], []
for _ in range(0, N):
    inputs.append(input())
for _ in range(0, M):
    targets.append(input())

dic = defaultdict(set)
for input_ in inputs:
    for i in range(1, len(input_)):
        dic[input_[0]].add(input_[0:i])

answer = 0
for t in targets:
    if t in dic[t[0]]:
        answer+=1
print(answer)







