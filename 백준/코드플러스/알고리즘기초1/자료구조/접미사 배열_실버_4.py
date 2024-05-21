# https://www.acmicpc.net/problem/11656
word = input()
word_lst = []
for i in range(len(word)):
    word_lst.append(word[i:])

word_lst.sort()
for word_ in word_lst:
    print(word_)
