def solution(n):
    answer = 0
    for i in range(2,n+1):
        s = True
        for val in range(2,int(i**0.5)+1):
            if i % val == 0:
                s = False
                break
        if s:
            answer +=1
        
    return answer