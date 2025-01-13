n = int(input())

computers = [i for i in range(0, n+1)]
parent_computers = [i for i in range(0, n+1)]

def find_parent(parents, x):
    if parents[x] != x: #나의 부모가 나와 같지 않다면 루트 노드를 탐색해야한다.
        find_parent(parents, x)
    return parents[x]

def union_parent(parents, a, b):
    a = find_parent(parents, a)
    b = find_parent(parents, b)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b

iter = int(input())
for _ in range(iter):
    a, b = map(int, input().split())
    union_parent(parent_computers, a, b)
