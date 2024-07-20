from collections import defaultdict
def solution(info, edges):
    answer = []
    graph = defaultdict(list)
    for e in edges:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])

    def dfs(pos, s, w):
        n_s, n_w, backup_node = s, w, info[pos]
        if v[pos][s][w] == True:
            return
        v[pos][s][w] = True


        if info[pos] == 0:
            n_s = s + 1
        if info[pos] == 1:
            n_w = w + 1
        info[pos] = -1

        if n_s > n_w:
            for next_pos in graph[pos]:
                answer.append(n_s)
                dfs(next_pos, n_s, n_w)

        info[pos] = backup_node
        v[pos][s][w] = False

    v = [[[False for _ in range(18)] for _ in range(18)] for _ in range(18)]

    dfs(0, 0, 0)
    return max(answer)


info = [0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0]
edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 8], [6, 9], [9, 10]]
print(solution(info, edges))