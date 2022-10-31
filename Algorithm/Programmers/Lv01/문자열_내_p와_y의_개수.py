def solution(s):
    p_num, y_num = 0, 0
    
    for val in s:
        if val == 'p' or val == 'P':
            p_num +=1
        elif val == 'y' or val == 'Y':
            y_num +=1
            
    if p_num == y_num:
        return True
    else:
        return False