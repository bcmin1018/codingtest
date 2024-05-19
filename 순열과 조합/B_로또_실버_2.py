from itertools import combinations
while True:
    test = list(map(int, input().split()))
    if test[0] == 0:
        break
    for i in combinations(test[1:], 6):
        print(*i)
    print("")