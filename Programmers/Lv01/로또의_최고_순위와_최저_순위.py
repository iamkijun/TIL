lottos = [44, 1, 0, 0, 31, 25]
win_nums = [31, 10, 45, 1, 6, 19]

def solution(lottos, win_nums):
    answer = []

    zero_cnt = 0

    correct = 0

    for val in lottos:
        if val in win_nums:
            correct += 1
        elif val == 0:
            zero_cnt += 1

    rank = 6
    if correct == 6:
        rank = 1
    elif correct == 5:
        rank = 2 
    elif correct == 4:
        rank = 3
    elif correct == 3:
        rank = 4
    elif correct == 2:
        rank = 5

    answer.append(rank)

    correct += zero_cnt
    
    rank = 6
    if correct >= 6:
        rank = 1
    elif correct == 5:
        rank = 2 
    elif correct == 4:
        rank = 3
    elif correct == 3:
        rank = 4
    elif correct == 2:
        rank = 5

    answer.append(rank)

    answer.sort()

    return answer

