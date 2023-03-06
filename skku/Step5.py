import time

# 반복 하는 형태
# def countdown(n):
#     while n > 0:
#         print(n)
#         time.sleep(1)
#         n = n - 1
#     print("GO !")
#
# countdown(int(input("insert sec: ")))

# 재귀 형태
# def countdown(n):
#     if n > 0:
#         print(n)
#         time.sleep(1)
#         countdown(n-1)
#     else:
#         print("GO !")
#
# countdown(int(input("insert sec: ")))

# 1 부터 n 까지 자연수 합 계산
# def sigma(n):
#     if n > 0:
#         return n + sigma(n-1)
#     else:
#         return 0
#
# sigma(int(input("insert : ")))


# 꼬리 재귀
# 추가적인 저장 공간을 재귀 함수들 끼리 넘기는 것.

# def sigma1(n):
#     return loop(n, 0)
#
# def loop(n, sum):
#     if n > 0:
#         return loop(n-1, n+sum)
#     else:
#         return sum
#
# sigma1(5)


# def sigma2(n):
#     sum = 0
#     while n > 0:
#         sum = n + sum
#         n = n - 1
#     return sum
# print(sigma2(5))


# def power(b, n):
#     if n > 0:
#         return b * power(b, n-1)
#     else:
#         return 1
#
# print(power(10, 3))

# def power2(b, n):
#     return loop(b, n, 1)
#
# def loop(b, n, sum):
#     if n > 0:
#         return b * loop(b, n-1, sum * b)
#     else:
#         return 1
# print(power2(2, 5))

# def power2(b, n):
#     prod = 1
#     while n > 0:
#         prod = b * prod
#         n = n - 1
#     return prod






