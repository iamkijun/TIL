N = int(input())

for n in range(1,N+1):
    i = n
    re =''
    while i > 0:
        if i % 10 == 3 or i % 10 == 6 or i % 10 == 9:
            re += '-'
        i = i//10

    if re =='':
        print(n, end=' ')
    else:
        print(re, end=' ')
    
        
        
