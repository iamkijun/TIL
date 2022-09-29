def solution(s):
    answer =[]
    s_li = list(s)
    temp =''
    for val in s_li:
        if val.isalpha():
            temp += val
        else:
            answer.append(temp)
            temp=''
    answer.append(temp) 
    result = ''
    
    for val in answer:
        temp =''
        for i in range(len(val)):
            if i % 2 == 0:
                temp += val[i].upper()
            else:
                temp += val[i].lower()
        result += temp+' '
        
    return result[:-1]