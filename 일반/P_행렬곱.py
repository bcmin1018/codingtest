def solution(arr1, arr2):
    n = len(arr1)
    m = len(arr2[0])
    k = len(arr1[0]) # 2*4  4*2  겹치는 것은 4

    answer = [[0 for _ in range(m)] for _ in range(n)]

    for i in range(n):
        for j in range(m):
            sum_ = 0
            for ki in range(k):
                sum_ += arr1[i][ki] * arr2[ki][j]
            answer[i][j] = sum_
    return answer

# arr1 = [[1, 4], [3, 2], [4, 1]]
# arr2 = [[3, 3], [3, 3]]

arr1 = [[2, 3, 2], [4, 2, 4], [3, 1, 4]]
arr2 = [[5, 4, 3], [2, 4, 1], [3, 1, 1]]

print(solution(arr1, arr2))

