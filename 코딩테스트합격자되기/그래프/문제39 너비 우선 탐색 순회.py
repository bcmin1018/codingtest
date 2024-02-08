from collections import defaultdict, deque
def solution(graph, start):
    adj_list = defaultdict(list)
    for u, v in graph:
        adj_list[u].append(v)

    def bfs(start):
        visited = []
        queue = deque([start])
        visited.append(start)
        result.append(start)

        while queue:
            node = queue.popleft()
            for n in adj_list[node]:
                if n not in visited:
                    visited.append(n)
                    queue.append(n)
                    result.append(n)
    result = []
    bfs(start)
    return result

graph =[(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7), (4, 8), (5, 8), (6, 9), (7, 9)]
start = 1
print(solution(graph, start))

