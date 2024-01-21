def solution(N, stages):
    p = len(stages)
    N_list = [0] * (N+2)
    for s in stages:
        N_list[s] += 1

    fails = {}
    for i in range(1, N+1):
        if N_list[i] == 0:
            fails[i] = 0
        else:
            fails[i] = N_list[i]/p
            p -= N_list[i]
    print(fails)
    result = sorted(fails, key=lambda x : fails[x], reverse=True)
    return result

N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
# stages = [4,4,4,4,4]
print(solution(N, stages))

# print([0] * N)
