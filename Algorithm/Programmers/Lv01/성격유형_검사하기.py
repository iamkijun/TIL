survey = ["AN", "CF", "MJ", "RT", "NA"]
choices = [5, 3, 2, 7, 5]

def solution(survey, choices):
    dic = {'R':0,'T':0,'C':0,'F':0,'J':0,'M':0,'A':0,'N':0}

    answer = ''

    for i in range(len(choices)):
        if choices[i] > 4:
            dic[survey[i][1]] += choices[i] -4
        elif choices[i] < 4:
            dic[survey[i][0]] += 4- choices[i]

    kinds = [['R','T'],['C','F'],['J','M'],['A','N']]
    
    for val in kinds:
        if dic[val[0]] >= dic[val[1]]:
            answer += val[0]
        else:
            answer += val[1]

    return dic, answer

print(solution(survey,choices))