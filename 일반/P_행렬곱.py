def solution(arr1, arr2):
    n = len(arr1[0])
    m = len(arr1)
    answer = [[0 for i in range(n)] for j in range(m)]

    for i in range(n):
        for lst1 in arr1:
            nlist2 = []
            for lst2 in arr2:
                nlist2.append(lst2[i])
            print(lst1 * nlist2)





    # answer = [[0 for m in range(arr2)] for i in range(arr1)]
    # for i, node1 in enumerate(arr1):
    #     for di in range(n):
    #         sum_ = 0
    #         for j, node2 in enumerate(arr2):
    #             sum_ += node1[di] * node2[di]
    #         answer[i][j] = sum_
    return answer

arr1 = [[2, 3, 2], [4, 2, 4], [3, 1, 4]]
arr2 = [[5, 4, 3], [2, 4, 1], [3, 1, 1]]

print(solution(arr1, arr2))

