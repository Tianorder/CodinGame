import sys
# the standard input according to the problem statement.

n = int(input())
word_list = [input() for _ in range(n)]
print(word_list, file=sys.stderr, flush=True)


# 输入原始序列和子序列，返回原始序列
def get_next_sequence(sequence, wordB):
    length_list = []
    if wordB in sequence:
        sequence.remove(wordB)
    for index, wordA in enumerate(sequence):
        if wordA == wordB:
            continue
        if wordB in wordA:
            length_list.append((0, wordA, index))
            continue
        if wordA in wordB:
            length_list.append((0, wordB, index))
            continue
        loc = 0
        start_length = 9999
        char = wordB[0]
        if char in wordA:
            for _ in range(wordA.count(char)):
                loc = wordA.find(char, loc + 1)
                if wordB.startswith(wordA[loc:]):
                    start_length = len(wordB) - (len(wordA) - loc)
                    start_new_word = wordA + wordB[len(wordA) - loc:]
                    length_list.append((start_length, start_new_word, index))
                    break
        loc = 9999
        end_length = 9999
        char = wordB[-1]
        if char in wordA:
            for _ in range(wordA.count(char)):
                loc = wordA.rfind(char, 0, loc - 1)
                if wordB.endswith(wordA[:loc + 1]):
                    end_length = len(wordB) - loc - 1
                    end_new_word = wordB[:-loc-1] + wordA
                    length_list.append((end_length, end_new_word, index))
                    break
    if length_list:
        print("length_list", length_list, file=sys.stderr, flush=True)
        min_length = min(length_list)
        print("min_length", min_length, file=sys.stderr, flush=True)
        sequence[min_length[2]] = min_length[1]
        print("sequence", sequence, file=sys.stderr, flush=True)
    else:
        if wordB not in sequence:
            sequence.append(wordB)


sequence = []
out = 0
for word in word_list:
    get_next_sequence(sequence, word)
for word in sequence:
    get_next_sequence(sequence, word)

print(sum(len(word) for word in sequence))