
#https://thought-process-ing.tistory.com/100
from itertools import permutations

n = int(input())
sign = list(input().split())
num = [i for i in range(0, 10)]
answer = []
for case in permutations(num, n+1):
    for i in range(0, n):
        if sign[i] == ">":
            if case[i] < case[i+1]:
                break
        else:
            if case[i] > case[i+1]:
                break
    else:
        answer.append(case)
answer.sort()
print("".join(map(str, answer[-1])))
print("".join(map(str, answer[0])))




