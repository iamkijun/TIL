s = "3people unFollowed me"

def solution(s):
    s= s.lower()

    idx = 0
    answer = ''
    while idx < len(s):
        if idx == 0 or s[idx-1] == ' ':
            answer += s[idx].upper()
        else:
            answer+= s[idx]
        idx+=1
    return answer
print(solution(s))