# https://www.acmicpc.net/problem/11720

import sys
sys.stdin = open("input.txt", "r")

sum_ = 0
N = int(input())
for num in list(map(int, str(input()))):
    sum_ += num
print(sum_)
