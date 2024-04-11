M, N = map(int, input().split())
cookies = list(map(int, input().split()))
left, right = 1, max(cookies)
while left <= right:
    mid = (left+right) // 2
    max_person = sum([c//mid for c in cookies])
    if max_person >= M: # 작게 나눈 경우
        left = mid+1
    else:
        right = mid-1
print(right)

