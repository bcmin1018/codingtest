#https://www.acmicpc.net/problem/1976

N = int(input())
M = int(input())

#초기화
cities = [i for i in range(N+1)]
parent = [i for i in range(N+1)]

#연결정보
maps = [list(map(int, input().split())) for i in range(N)]
connection = []
for i in range(N):
    for j in range(N):
        if maps[j][i] == 1:
            connection.append((i+1, j+1))

#여행 계획
trip_plan = list(map(int, input().split()))

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x_parent = find(x)
    y_parent = find(y)

    if x_parent > y_parent:
        parent[x_parent] = y_parent
    else:
        parent[y_parent] = x_parent
    # 만약 1의 부모를 가진 집단 중의 한 수가 2의 부모 집단과 합쳐지면 나머지 노드들의 부모들도 모두 2로 바껴야하나?

for x_, y_ in connection:
    union(x_, y_)

answer = "YES"
for i in range(M-1):
    if find(trip_plan[i]) != find(trip_plan[i+1]):
        answer = "NO"

print(answer)









