n = 5
lost = [2,4]
reserve = [1,3,5]

def solution(n, lost, reserve):
    answer = 0
    new_lost = set(lost) - set(reserve)
    new_reserve = set(reserve) - set(lost)

    for val in new_lost:
        if val-1 in new_reserve:
            new_reserve.remove(val-1)
        elif val+1 in new_reserve:
            new_reserve.remove(val+1)
        else:
            answer += 1


    return n-answer