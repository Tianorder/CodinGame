# the standard input according to the problem statement.

keyword = input()
sentence = input()
upper_sentence = sentence.upper()
upper_keyword = keyword.upper()
loc = upper_sentence.find(upper_keyword)
out_sentence = sentence
while loc != -1:
    out_sentence = out_sentence[:loc] + upper_keyword + out_sentence[loc + len(keyword):]
    loc = upper_sentence.find(upper_keyword, loc + 1)

print(out_sentence)
