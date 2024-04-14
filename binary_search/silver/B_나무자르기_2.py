# 높이의 최대값 즉 같은 높이를 가져갈 수 있어도 최대한 나무를 회손 시키지 않기 위해 절단기를 최대한 높이 설정해야한다.
# upperbound로 구하고 right 값을 출력하면 가져갈 수 있는 수 중에 최대 절단 높이를 구할 수 있다.
M, N = map(int, input().split())
tree = list(map(int, input().split()))

left = 0
right = max(tree)-1

while left <= right:
    mid = (left + right) // 2
    rest = sum([t-mid for t in tree if t > mid])
    if N > rest: # 절단선이 높아 적게 남았을 때는 절단선을 낮춘다.
        right = mid -1
    else:
        left = mid + 1
print(right)


