from collections import defaultdict
def solution(graph, start):
    adj_list = defaultdict(list)
    for u, v in graph:
        adj_list[u].append(v)
    def dfs(node, visited, result):
        visited.append(node)
        result.append(node)
        for n in adj_list[node]:
            if n not in visited:
                dfs(n, visited, result)

    visited = []
    result = []
    dfs(start, visited, result)
    return result

# graph_ = [['A', 'B'], ['B', 'C'], ['C', 'D'], ['D', 'E']]
# start = 'A'

graph_ = [['A', 'B'], ['A', 'C'], ['B', 'D'], ['B', 'E'], ['C', 'F'], ['E', 'F']]
start = 'A'

print(solution(graph_, start))