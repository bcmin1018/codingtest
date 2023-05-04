def solution(arr1, arr2):
    n = len(arr1)
    m = len(arr2)
    k = len(arr2[0])

    answer = [[0 for i in range(n)] for j in range(m)]

    for i in range(n):
        for j in range(m):
            sum_ = 0
            for k in range(k):
                sum_ += arr1[i][k] * arr2[k][j]
            answer[i][j] = sum_
    return answer

arr1 = [[1,2,3,4], [1,2,3,4]]
arr2 =  [[1,2], [1,2], [1,2], [1,2]]

print(solution(arr1, arr2))

