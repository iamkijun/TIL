def solution(a, b):
    if a>b:
        answer = sum([x for x in range(b,a+1)])
    elif b>a:
        answer = sum([x for x in range(a,b+1)])
    else:
        answer = a
    
    return answer