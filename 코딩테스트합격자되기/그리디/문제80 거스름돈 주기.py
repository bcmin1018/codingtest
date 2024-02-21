def solution(amount):
    moneny = [1, 10, 50, 100]
    result = []

    for m in reversed(moneny):
        while True:
            if amount < m:
                break
            else:
                amount = amount - m
                result.append(m)

    return result

amount = 350
print(solution(amount))