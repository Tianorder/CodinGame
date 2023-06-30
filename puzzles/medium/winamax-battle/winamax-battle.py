# the standard input according to the problem statement.

n = int(input())  # the number of cards for player 1
card_dict = {"J": 11, "Q": 12, "K": 13, "A": 14}
cardp_1_list = []
for i in range(n):
    cardp_1 = input()  # the n cards of player 1
    cardp_1 = cardp_1[:-1]
    if cardp_1 in card_dict:
        cardp_1 = card_dict[cardp_1]
    else:
        cardp_1 = int(cardp_1)
    cardp_1_list.append(cardp_1)
m = int(input())  # the number of cards for player 2
cardp_2_list = []
for i in range(m):
    cardp_2 = input()  # the m cards of player 2
    cardp_2 = cardp_2[:-1]
    if cardp_2 in card_dict:
        cardp_2 = card_dict[cardp_2]
    else:
        cardp_2 = int(cardp_2)
    cardp_2_list.append(cardp_2)

# 判断war中是否没牌
def is_pat(cardp_1_list, cardp_2_list):
    if not cardp_1_list or not cardp_2_list:
        print("PAT")
        exit()


count = 0
while cardp_1_list and cardp_2_list:
    count += 1
    cardp_1 = cardp_1_list.pop(0)
    cardp_2 = cardp_2_list.pop(0)
    if cardp_1 > cardp_2:
        cardp_1_list.extend([cardp_1, cardp_2])
    elif cardp_1 < cardp_2:
        cardp_2_list.extend([cardp_1, cardp_2])
    else:
        list1 = [cardp_1]
        list2 = [cardp_2]
        while cardp_1 == cardp_2:
            for i in range(3):
                is_pat(cardp_1_list, cardp_2_list)
                list1.append(cardp_1_list.pop(0))
                list2.append(cardp_2_list.pop(0))
            is_pat(cardp_1_list, cardp_2_list)
            cardp_1 = cardp_1_list.pop(0)
            cardp_2 = cardp_2_list.pop(0)
            list1.append(cardp_1)
            list2.append(cardp_2)
            if cardp_1 > cardp_2:
                cardp_1_list.extend(list1 + list2)
            elif cardp_1 < cardp_2:
                cardp_2_list.extend(list1 + list2)

if cardp_1_list:
    out = "1 " + str(count)
elif cardp_2_list:
    out = "2 " + str(count)
else:
    out = "PAT"
print(out)
