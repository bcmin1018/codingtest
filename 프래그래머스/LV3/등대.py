from collections import defaultdict
import sys
sys.setrecursionlimit(100001)

def solution(n, lighthouse):
    counter = defaultdict(list)
    for l in lighthouse:
        counter[l[0]].append(l[1])
        counter[l[1]].append(l[0])

    light = [False] * (n+1)
    def dfs(node, parent_node):
        # answer = 0
        children = counter[node]
        for child in children:
            if parent_node == child:
                continue

            dfs(child, node)
            if light[child] == False and light[node] == False: #부모 자식 모두 불이 안켜져 있으면 부모가 불을 밝힌다.
                light[node] = True
    dfs(1, 1)
    return sum(light)

n = 10
lighthouse = [[4, 1], [5, 1], [5, 6], [7, 6], [1, 2], [1, 3], [6, 8], [2, 9], [9, 10]]
print(solution(n, lighthouse))