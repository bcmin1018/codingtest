# https://tolerblanc.github.io/programmers/programmers-donut-stick-graph/

# 제목 : 도넛과 막대 그래프
# 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/258711
# 풀이
# 1. node에서 나가고 들어오는 간선의 개수로 구분이 필요하다.
# 2. 생성된 노드는 나가는 간선이 2개 이상이다.
# 3. 막대그래프는 나가는 간선이 존재하지 않는 노드가 있다.
# 4. 8자는 들어오고 나가는 간선이 각각 두개씩 존재한다.
# 5. 도넛은
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
    print(graph)
    print(out_)
    print(in_)
    centor_node = [g for g in graph.keys() if out_[g] >=2 and in_[g] == 0][0]
    answer[0] = centor_node
    print(centor_node)

    doughnut = 0
    for node in graph[centor_node]:









    return answer

# edges = [[4, 11], [1, 12], [8, 3], [12, 7], [4, 2], [7, 11], [4, 8], [9, 6], [10, 11], [6, 10], [3, 5], [11, 1], [5, 3], [11, 9], [3, 8]]
edges = [[2, 3], [4, 3], [1, 1], [2, 1]]
print(solution(edges))