def solution(s):
    answer = ''
    li_s = list(s)
    for i in range(len(s)-1):
        if s[i].isdigit():
            answer += str(s[i])
        if s[i:i+2] == 'ze':
            answer += '0'
        elif s[i:i+2] == 'on':
            answer += '1'
        elif s[i:i+2] == 'tw':
            answer += '2'
        elif s[i:i+2] == 'th':
            answer += '3'
        elif s[i:i+2] == 'fo':
            answer += '4'
        elif s[i:i+2] == 'fi':
            answer += '5'
        elif s[i:i+2] == 'si':
            answer += '6'
        elif s[i:i+2] == 'se':
            answer += '7'
        elif s[i:i+2] == 'ei':
            answer += '8'
        elif s[i:i+2] == 'ni':
            answer += '9'
    if s[-1].isdigit():
        answer += str(s[-1])
    return int(answer)