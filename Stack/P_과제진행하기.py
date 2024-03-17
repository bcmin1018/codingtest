
def end_time_cal(s_time, w_time):
    hh, mm = map(int, s_time.split(":"))
    n_hh = ((mm + int(w_time)) // 60) + hh
    n_mm = (mm + int(w_time)) % 60
    return str(n_hh) + ":" + str(n_mm)


def solution(plans):
    sorted_plans = sorted(plans, key=lambda x: x[1])
    n_plans = []
    for p in sorted_plans:
        end_time = end_time_cal(p[1], p[2])
        p.append(end_time)
        n_plans.append(p)
    print(n_plans)

    stack = []
    result = []
    for i in range(0, len(n_plans)-1):
        print(f'{i}번째 순회 중 스택: {stack}  결과: {result}')
        # 뒤의 과제의 시작 시간이 빨라 하던 작업을 마무리 못했을 때
        if n_plans[i][3] > n_plans[i+1][1]:
            stack.append(n_plans[i])

        # 현재 주어진 과제를 모두 완료했을 때
        if n_plans[i][3] <= n_plans[i+1][1]:
            result.append(n_plans[i][0])

            if stack:
                if stack[-1][1] > n_plans[i+1][1]:
                    continue
                else:
                    if stack[-1][3] < n_plans[i+1][1]:
                        result.append(stack[-1][0])
                        stack.pop()
    return result

plans = [["science", "12:40", "50"], ["music", "12:20", "40"], ["history", "14:00", "30"], ["computer", "12:30", "100"]]
print(solution(plans))
