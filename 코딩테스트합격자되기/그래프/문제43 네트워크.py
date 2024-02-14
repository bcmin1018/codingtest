from collections import defaultdict


def dfs(adj_list, node, visited):
    visited[node] = 1
    for n in adj_list[node]:
        if visited[n] != 1:
            dfs(adj_list, n, visited)

def solution(n, computers):
    adj_list = defaultdict(list)
    for i in range(n):
        for j in range(n):
            if computers[j][i] == 1:
                adj_list[i].append(j)

    answer = 0
    visited = [0] * n
    for i in range(n):
        if visited[i] != 1:
            start_node = i
            dfs(adj_list, start_node, visited)
            answer += 1
    return answer

n = 3
# computers = [[1,1,0], [1,1,0], [0,0,1]]
computers = [[1,1,0], [1,1,1], [0,1,1]]
print(solution(n, computers))




