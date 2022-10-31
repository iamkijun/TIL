import sys
sys.stdin = open('D2/input.txt','r')

T = int(input())

for t in range(1,T+1):
    
    N = int(input())
    i  = 1
    num_list = []

    while len(num_list) != 10:

        a = N * i 
        a_list = []

        while a > 0:
            k= a % 10
            a_list.append(k)
            a = a // 10
        
        for val in a_list:
            if val not in num_list:
                num_list.append(val)
            elif val in num_list:
                continue
        
        i = i + 1
        
    print(f'#{t} {N*(i-1)}')