#https://www.acmicpc.net/problem/5052
#TODO: 10프로에서 틀렸습니다가 나오는데 적절한 반례를 찾지 못하였다.
import sys
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word: str):
        node = self.root
        for char in word:
            if node.is_end_of_word is True:
                return "EMERGENCY"
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word


t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    phone_numbers = int(sys.stdin.readline().rstrip())
    trie = Trie()
    consistency = True
    for _ in range(phone_numbers):
        number = sys.stdin.readline().rstrip()
        search_result = trie.search(number)
        if search_result is False:
            trie.insert(number)
            continue
        if search_result == "EMERGENCY":
            consistency = False
        if search_result is True:
            consistency = False
    if consistency is True:
        print("YES")
    else:
        print("NO")