def solution(arr, divisor):
    answer = []
    for val in arr:
        if val % divisor == 0:
            answer.append(val)
    answer.sort()
    if answer:
        return answer
    else:
        return [-1]