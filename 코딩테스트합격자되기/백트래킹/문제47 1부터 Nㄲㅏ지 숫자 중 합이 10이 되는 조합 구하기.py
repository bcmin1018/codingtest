def dfs(node, sum, N, selected_nums, result):
    if sum == 10:
        result.append(selected_nums)

    for i in range(node+1, N+1):
        if sum + i <= 10:
            dfs(i, sum+i, N, selected_nums + [i], result)

def solution(N):
    result = []
    for i in range(1, N+1):
        dfs(i, i, N, [i], result)
    return result

N = 7
print(solution(N))