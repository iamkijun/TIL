T = int(input())

for i in range(1,T+1):
    a,b,c,d = map(int, input().split())
    day_list = 0
    
    if a < c:
        if a in [1,3,5,7,8,10,12]:
            day_list += 32-b
        elif a == 2:
            day_list += 29-b
        elif a in [4, 6, 9, 11]:
            day_list += 31-b

        for j in range(1,c-a):
            if a+j in [1,3,5,7,8,10,12]:
                day_list += 31
            elif a+j == 2:
                day_list += 28
            elif a+j in [4, 6, 9, 11]:
                day_list += 30
        
        if c in [1,3,5,7,8,10,12]:
            day_list += d
        elif c == 2:
            day_list += d
        elif c in [4, 6, 9, 11]:
            day_list += d

        print(f'#{i} {day_list}')        
    elif a == c:
        print(f'#{i} {d-b+1}')
    