# https://school.programmers.co.kr/learn/courses/30/lessons/176962
# def end_time_cal(s_time, w_time):
#     hh, mm = map(int, s_time.split(":"))
#     n_hh = ((mm + int(w_time)) // 60) + hh
#     n_mm = (mm + int(w_time)) % 60
#     return str(n_hh) + ":" + str(n_mm)

def time_transform(start_time):
    h, m = map(int, start_time.split(":"))
    return 60 * h + m


def solution(plans):
    sorted_plans = sorted(plans, key=lambda x: x[1])
    n_plans = []
    for p in sorted_plans:
        p[1] = time_transform(p[1])
        p.append(p[1] + int(p[2]))
        n_plans.append(p)
    print(n_plans)

    answer = []
    stack = []
    for i in range(1, len(plans)):
        c_work = plans[i - 1][0]
        c_start_time = plans[i - 1][1]
        c_work_time = int(plans[i - 1][2])
        c_end_time = plans[i - 1][3]

        n_work = plans[i][0]
        n_start_time = plans[i][1]
        n_work_time = plans[i][2]
        n_end_time = plans[i][3]

        if c_end_time < n_start_time:
            answer.append(c_work)
            work = n_start_time - c_end_time

            while work > 0:
                target = stack[-1]
                if target[2] - work == 0:
                    answer.append(target[0])
                    stack.pop()
                    work = 0
                elif target[2] - work > 0:  # 스택에 있는 걸 다 못 끝냈을 때
                    target[2] = target[2] - (target[2] - work)
                    break
                elif target[2] - work < 0:
                    answer.append(target[0])
                    stack.pop()
                    work = work - target[2]

        elif c_end_time == n_start_time:
            answer.append(c_work)
        elif c_end_time > n_start_time:
            work = n_start_time - c_start_time
            plans[i - 1][2] = c_work_time - work
            stack.append(plans[i - 1])

            # if stack:
            #     work_time = plans[i][1] - plans[i - 1][3]
            #     if stack[-1][2] - work_time == 0:
            #         answer.append(stack[-1][0])
            #         stack.pop()
            #     elif stack[-1][2] - work_time > 0:
            #         continue
            #     elif stack[-1][2] - work_time < 0:
            #         stack.pop()

    # sorted_plans = sorted(plans, key=lambda x: x[1])
    # n_plans = []
    # for p in sorted_plans:
    #     end_time = end_time_cal(p[1], p[2])
    #     p.append(end_time)
    #     n_plans.append(p)
    # print(n_plans)

    # stack = []
    # result = []
    # for i in range(0, len(n_plans)-1):
    #     print(f'{i}번째 순회 중 스택: {stack}  결과: {result}')
    #     # 뒤의 과제의 시작 시간이 빨라 하던 작업을 마무리 못했을 때
    #     if n_plans[i][3] > n_plans[i+1][1]:
    #         stack.append(n_plans[i])
    #
    #     # 현재 주어진 과제를 모두 완료했을 때
    #     if n_plans[i][3] <= n_plans[i+1][1]:
    #         result.append(n_plans[i][0])
    #
    #         if stack:
    #             if stack[-1][1] > n_plans[i+1][1]:
    #                 continue
    #             else:
    #                 if stack[-1][3] < n_plans[i+1][1]:
    #                     result.append(stack[-1][0])
    #                     stack.pop()
    return answer


plans = [["science", "12:40", "50"], ["music", "12:20", "40"], ["history", "14:00", "30"], ["computer", "12:30", "100"]]
print(solution(plans))
