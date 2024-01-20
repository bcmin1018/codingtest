def solution(N, stages):
    p = len(stages)
    N_list = [0] * (N+1)
    print(f"첫  {N_list}")
    for s in stages:
        if s > N:
            continue
        N_list[s] += 1
    print(f"N_list 다 채움  {N_list}")
    result = [0] * (N+1)
    for i, f in enumerate(N_list):
        result[i] = f/p
        p = p-f
    print(f"result 정렬 전  {result}")

    sorted_result = [0] * (N+1)
    for i, r in enumerate(result[1:]):



    # sorted_result = sorted(result[1:], reverse=True)
    return sorted_result


N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
print(solution(N, stages))

# print([0] * N)
