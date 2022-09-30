def solution(a, b):
    month_lens = [31,29,31,30,31,30,31,31,30,31,30,31]
    days = ['FRI','SAT','SUN','MON','TUE','WED','THU']
    
    le = b-1
    for i in range(a-1):
        le += month_lens[i]
    
    le = le % 7
    answer = days[le]
    
    return answer