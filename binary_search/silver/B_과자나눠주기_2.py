# 최대 막대과자 길이를 구해야하므로 upper bound로 구해야함.
M, N = map(int, input().split())
cookies = list(map(int, input().split()))
left, right = 1, len(cookies)
while left <= right:
    mid = (left+right) // 2
    total = sum([c//mid for c in cookies])
    if total >= M:
        left = mid + 1
    else:
        right = mid - 1
print(left-1)