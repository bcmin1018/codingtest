from collections import defaultdict

def dfs(adj_lst, node, visited):
    visited.append(node)
    for a in adj_lst[node]:
        if a not in visited:
            dfs(adj_lst, a, visited)

def solution(n, wires):
    adj_lst = [[] for _ in range(n+1)]
    for u, v in wires:
        adj_lst[u].append(v)
        adj_lst[v].append(u)
    print(adj_lst)


    min_lst = []
    for u, v in wires:
        total = n
        visited = []
        adj_lst[u].remove(v)
        adj_lst[v].remove(u)
        print(f'{u}번째 노드와 {v} 간의 연결을 삭제')

        if u not in visited:
            dfs(adj_lst, u, visited)
        print(f'{u} 번째 노드 일때 {visited}를 방문했다.')
        min_lst.append(abs((total - len(visited)) - len(visited)))

        adj_lst[u].append(v)
        adj_lst[v].append(u)
        print(min_lst)
    return min(min_lst)

n = 7
wires = [[1,2], [2,7], [3,7], [3,4], [4,5], [6,7]]
# wires = [[1,2], [2,3], [3,4]]
print(solution(n, wires))

