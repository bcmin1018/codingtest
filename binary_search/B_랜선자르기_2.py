K, N = map(int, input().split())
cable = []
for _ in range(K):
    cable.append(int(input()))
left = 1
right = max(cable)

while left <= right:
    mid = (left + right) // 2
    n = sum([c // mid for c in cable])
    if n >= N:
        left = mid +1
    else:
        right = mid-1
print(right)
