import sys
sys.stdin = open("D3/input.txt")

T = int(input())



for t in range(1,T+1):

    N = int(input())
    
    count = 0 
    
    while True:
        if N>=2:
            N = N/2
            count += 1
            print(N,count)
        else:
            break

    if count % 2 ==1:
        print(f'#{t} Alice')
        count+=1
    elif count % 2 ==0:
        print(f'#{t} Bob')
        count+=1