
def solution(word):
    answer = 0
    visited = ['Z'] * 5
    def dfs(start_word, depth, answer):
        # if ''.join(visited) == list(word):
        #     return answer
        if depth == 5:
            return
        # depth가 5가 되었을 때 다시 전으로 돌아가지만 depth는 차감이 안되므로 오류
        visited[depth] = start_word
        answer += 1
        for w_ in ['A', 'E', 'I', 'O', 'U']:
            dfs(w_, depth +1, answer)
            depth-=1


    for w in ['A', 'E', 'I', 'O', 'U']:
        dfs(w, 0, answer)
    return answer

word = "AAAAE"
solution(word)