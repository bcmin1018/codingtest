# 제목 : 문자열 압축
# 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/60057?language=python3
# 1개 이상의 단위로 문자열을 자른다.
# 같은 문자열이 나왔을떄 어떻게 숫자를 추가해야할까 -> 처음, 나중

# 일단 어느 한 공간에 대상을 넣고 다음 대상을 추가적으로 넣을떄 체크를 해서 같으면 계속 넣고 그렇지 않으면 공간에 있는 대상을 통과 시킨다.
def solution(s):
    answer = len(s)
    slice_ = 1
    while slice_ < len(s) // 2:
        stack = []
        temp = []
        for i in range(0, len(s)+1, slice_):
            if stack:
                if stack[-1] == s[i:i+slice_]:
                    stack.append(s[i:i+slice_])
                else:
                    cnt = len(stack)
                    if cnt > 1:
                        temp.append(str(cnt))
                    temp.append(stack[-1])
                    for _ in range(cnt):
                        stack.pop()
                    stack.append(s[i:i + slice_])
            else:
                stack.append(s[i:i + slice_])
        if answer > len(''.join(temp)):
            answer = len(''.join(temp))
        print(''.join(temp))
        slice_+=1
    return answer


s = "aabbaccc"
print(solution(s))