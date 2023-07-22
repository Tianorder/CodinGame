# 这是一道典型的动态规划题
# 由于数据过大，存放到了单词查找树
import sys
# the standard input according to the problem statement.

dict = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--.."
    }

l = input()
# print("l: " + l, file=sys.stderr, flush=True)
n = int(input())
word_list = []
for i in range(n):
    w = input()
    # print(w, file=sys.stderr, flush=True)
    word = ""
    for ch in w:
        word += dict[ch]
    print(word, file=sys.stderr, flush=True)
    word_list.append(word)


def print_trie(root, prefix=""):
    if not root:
        return

    print(prefix + "+--" if prefix else "", file=sys.stderr, flush=True)

    for char, child in sorted(root.children.items()):
        indicator = "|  " if prefix else "   "
        print(prefix + indicator + char, file=sys.stderr, flush=True)
        print_trie(child, prefix + indicator)


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
        self.count = 0


def insert_word(root, word):
    node = root
    for char in word:
        if char not in node.children:
            node.children[char] = TrieNode()
        node = node.children[char]
    node.is_word = True
    node.count += 1


def count_combinations(l):
    root = TrieNode()
    for word in word_list:
        insert_word(root, word)
    print_trie(root)

    n = len(l)
    dp = [0] * (n + 1)
    dp[0] = 1

    for i in range(n):
        node = root
        for j in range(i, n):
            char = l[j]
            if char not in node.children:
                break
            node = node.children[char]
            if node.is_word:
                dp[j + 1] += dp[i] * node.count

    return dp[-1]
print(count_combinations(l))
