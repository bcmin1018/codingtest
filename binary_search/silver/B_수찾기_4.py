N = int(input())
n = list(map(int, input().split()))
M = int(input())
m = list(map(int, input().split()))

n = sorted(n)
def b_search(n, key):
    left = 0
    right = len(n) -1
    answer = 0
    while left <= right:
        mid = (left + right) // 2
        if n[mid] == key:
            answer = 1
            break
        elif n[mid] > key:
            right = mid -1
        else:
            left = mid +1

    return answer

for m_ in m:
    print(b_search(n, m_))



