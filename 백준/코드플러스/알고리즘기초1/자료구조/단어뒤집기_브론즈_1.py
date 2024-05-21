n = int(input())
for _ in range(n):
    words = input().split()
    answer = []
    for word in words:
        answer.append(word[::-1])
    print(" ".join(answer))