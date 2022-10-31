def solution(array, commands):
    answer = []
    for val in commands:
        new = array[val[0]-1:val[1]]
        new.sort()
        answer.append(new[val[2]-1])
    return answer