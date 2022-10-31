def solution(s, n):
    answer = ''

    for val in s:
        if val.isalpha():
            if val.islower():
                temp = ord(val)+n
                if temp >122:
                    temp -= 26
                answer += chr(temp)
            elif val.isupper():
                temp = ord(val)+n
                if temp >90:
                    temp -= 26
                answer += chr(temp)
        else:
            answer += val
        
                
        
    return answer