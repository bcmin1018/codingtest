# 예산의 총 합이 전체 예산 보다 작거나 같아야 한다.
# 가장 낮은 예산인 0은 left, 가장 높은 예산을 right
# 가능한 최대 상한선을 찾아야하므로 upper bound 사용

N = int(input())
budget = list(map(int, input().split()))
t_budget = int(input())

left, right = 0, max(budget)
while left <= right:
    mid = (left + right) // 2
    if t_budget >= sum([mid if b > mid else b for b in budget]):
        left = mid + 1
    else:
        right = mid - 1

print(left-1)