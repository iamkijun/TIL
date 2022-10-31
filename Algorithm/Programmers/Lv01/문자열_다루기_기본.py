def solution(s):
    answer = False
    
    if len(s) == 4 or len(s) == 6:
            answer = True
    try:
        for val in s:
            if int(val):
                pass
    except:
        answer =False
    
    return answer