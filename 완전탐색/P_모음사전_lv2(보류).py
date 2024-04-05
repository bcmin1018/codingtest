
def solution(word):
    answer = 0
    visited = []
    def dfs(start_word, answer):
        # if ''.join(visited) == list(word):
        #     return answer
        # depth가 5가 되었을 때 다시 전으로 돌아가지만 depth는 차감이 안되므로 오류
        if len(visited) > 5:
            return

        visited.append(start_word)
        answer += 1
        for w_ in ['A', 'E', 'I', 'O', 'U']:
            # visited.append(w_)
            dfs(w_, answer)
            # answer-=1

    for w in ['A', 'E', 'I', 'O', 'U']:
        dfs(w, 0)
    return answer

word = "AAAAE"
solution(word)