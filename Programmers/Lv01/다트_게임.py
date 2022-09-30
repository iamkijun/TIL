def solution(dartResult):
    score_list = []
    idx = 0
    stk =[]
    while idx < len(dartResult):

        if dartResult[idx].isdigit():
            if dartResult[idx] == '1':
                if dartResult[idx+1] == '0':
                    stk.append(10)
                    idx+=2
                    continue
            stk.append(int(dartResult[idx]))

        elif dartResult[idx] == 'S':
            score_list.append(stk.pop(-1))
        elif dartResult[idx] == 'D':
            score_list.append(stk.pop(-1)**2)
        elif dartResult[idx] == 'T':
            score_list.append(stk.pop(-1)**3)

        elif dartResult[idx] == '*':
            if len(score_list) >=2:
                score_list[-2] = score_list[-2]*2
            score_list[-1] = score_list[-1]*2

        elif dartResult[idx] == '#':
            score_list[-1] = score_list[-1]*(-1)

        idx+=1
    
    answer = sum(score_list)
    return answer