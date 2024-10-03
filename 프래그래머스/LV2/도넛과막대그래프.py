# https://tolerblanc.github.io/programmers/programmers-donut-stick-graph/

# 제목 : 도넛과 막대 그래프
# 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/258711
# 풀이
# 1. node에서 나가고 들어오는 간선의 개수로 구분이 필요하다.
# 2. 도넛 모양 그래프는 모든 노드가 나가고 들어오는 간선이 한개씩이다.
# 3. 막대그래프는 나가는 간선이 존재하지 않는 노드가 있다.
# 4. 8자는 나가는 간선이 두개가 있는 노드가 있다.
# 5. DFS로 그래프를 탐색하면 시간이 초과된다.
# 6. 위의 조건을 가지고 노드가 발견되면 그래프의 형태를 파악하고 다른 그래프를 탐색한다.

from collections import defaultdict

def solution(edges):
    answer = [0, 0, 0, 0]
    graph = defaultdict(list)
    out_ = defaultdict(int)
    in_ = defaultdict(int)
    for e in edges:
        graph[e[0]].append(e[1])
        out_[e[0]] += 1
        in_[e[1]] += 1
    # print(f'graph: {graph}')
    # print(f'out_: {out_}')
    # print(f'in_: {in_}')
    centor_node = [g for g in graph.keys() if out_[g] >=2 and in_[g] == 0][0]
    answer[0] = centor_node
    # print(f'centor_node: {centor_node}')

    doughnut = 0
    bar = 0
    eight = 0
    visited = set()
    for start_node in graph[centor_node]:
        visited.add(start_node)
        curr = start_node
        while curr:
            if out_[curr] == 0:
                bar += 1
                break
            elif out_[curr] == 2:
                eight+=1
                break
            curr = graph[curr][0]
            if curr in visited and out_[curr] == 1:
                doughnut+=1
                break
            visited.add(curr)

    answer[1] = doughnut
    answer[2] = bar
    answer[3] = eight
    return answer

edges = [[4, 11], [1, 12], [8, 3], [12, 7], [4, 2], [7, 11], [4, 8], [9, 6], [10, 11], [6, 10], [3, 5], [11, 1], [5, 3], [11, 9], [3, 8]]
# edges = [[2, 3], [4, 3], [1, 1], [2, 1]]
print(solution(edges))