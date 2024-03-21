
def convert_time(start_time):
    h, m = map(int, start_time.split(":"))
    return 60 * h + m


def solution(plans):
    sorted_plans = sorted(plans, key=lambda x: x[1])
    n_plans = []
    for p in sorted_plans:
        p[1] = convert_time(p[1])
        p[2] = int(p[2])
        p.append(p[1] + int(p[2]))
        n_plans.append(p)
    print(n_plans)

    answer = []
    stack = []
    left_time = 0

    for i in range(0, len(n_plans)):
        print(f'{i+1} 번쨰')
        c_work = n_plans[i][0]
        c_start_time = n_plans[i][1]
        c_work_time = n_plans[i][2]
        c_end_time = n_plans[i][3]

        while stack:
            if c_end_time < stack[-1][1]:
                answer.append(stack[-1][0])


        stack.append(n_plans[i])

        if i < len(n_plans)-1:
            work = n_plans[i+1][1] - c_start_time
            left_time += work

        if i < len(n_plans)-1:
            n_start_time = n_plans[i+1][1]
            if c_end_time < n_start_time:
                answer.append(c_work)
                work = n_start_time - c_end_time
                print(f'work {work}')
                while work > 0:
                    target = stack[-1]
                    if target[2] - work == 0:
                        answer.append(target[0])
                        stack.pop()
                        work = 0
                    elif target[2] - work > 0:  # 스택에 있는 걸 다 못 끝냈을 때
                        target[2] = target[2] - work
                        work = 0
                    elif target[2] - work < 0:
                        answer.append(target[0])
                        stack.pop()
                        work = work - target[2]
            elif c_end_time == n_start_time:
                answer.append(c_work)
            elif c_end_time > n_start_time: # 뒷 작업을 진행
                work = n_start_time - c_start_time
                if stack:
                    stack[-1][2] = stack[-1][2] - work
                stack.append(n_plans[i])
                print(stack)
    return answer


plans = [["science", "12:40", "50"], ["music", "12:20", "40"], ["history", "14:00", "30"], ["computer", "12:30", "100"]]
print(solution(plans))
