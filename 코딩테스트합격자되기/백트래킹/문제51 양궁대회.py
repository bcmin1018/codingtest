from collections import defaultdict


def dfs(visited, hit_point, k, dic):
    visited[k] = 1
    for k in range(0, len(info)):
        for v in dic[k]:
            if visited[v] == 1

def solution(n, info):
    dic = defaultdict(list)
    for k in range(0, len(info)):
        for v in range(0, n + 1):
            dic[k].append(v)

    hit_point = [0] * len(info)
    visited = [0] * len(info)





        visited[k] = 1
        print(hit_point)
        for v in dic[k]:
            if visited[v] != 1:
                hit_point[k] = v
                dfs(visited, hit_point, v, dic)

    dfs(visited, hit_point, k, dic)

n = 5
info = [2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]
solution(n, info)
