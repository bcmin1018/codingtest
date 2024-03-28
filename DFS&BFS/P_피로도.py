def solution(k, dungeons):
    visited = [0] * len(dungeons)
    def dfs(node, k):
        print(k)
        if dungeons[node][0] > k: # 최소 피로도 보다 피가 낮으면 다른 곳 찾아!
            return
        k = k - dungeons[node][1] # 던전 깨고 피로도 차감
        visited[node] = 1
        for i in [1, -1]: # 다음 곳 서치
            n_node = node+i
            if n_node < len(dungeons) and visited[n_node] == 0 and dungeons[n_node][0] <= k:
                print(f'{dungeons[n_node]}')
                dfs(n_node, k)
                # print(n_node)
                # print(node, n_node)
                # print(visited)
                # visited[n_node] = visited[node] + 1


    dfs(0, k)
    return sum(visited)




# k = 80
# k = 8
k = 10
# dungeons = 	[[80,20],[50,40],[30,10]]
# dungeons = [[7, 3], [5, 4], [1, 1]]
dungeons = [[9, 2], [10, 3], [7, 3], [5, 4], [1, 1]]
print(solution(k, dungeons))