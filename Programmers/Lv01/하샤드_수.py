def solution(x):
    total = x
    li = []
    while True:
        li.append(x%10)
        x = x // 10
        if x == 0:
            break
    if total % sum(li) == 0:
        answer = True
    else:
        answer = False
    return answer