# def solution(n):
#     numbers = list(str(n))
#     digits = sorted(numbers, reverse=True)
#     return int(''.join(digits))
# print(solution(118372))


def solution(price, money, count):
    total = 0
    for i in range(count):
        total += price * (i+1)
    if total < money:
        return 0
    else:
        return total - money

print(solution(3, 20, 4))