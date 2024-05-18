# https://www.acmicpc.net/problem/2309
import sys
hobits = []
for _ in range(9):
    hobits.append(int(sys.stdin.readline()))
hobits.sort()
sum_ = sum(hobits)
tmp1, tmp2 = 0, 0
for i in range(9):
    for j in range(i+1, 9):
        if sum_ - (hobits[i] + hobits[j]) == 100:
            tmp1, tmp2 = hobits[i], hobits[j]
hobits.remove(tmp1)
hobits.remove(tmp2)
for h in hobits:
    print(h)



