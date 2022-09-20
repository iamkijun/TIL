import sys
sys.stdin = open("D3/input.txt")

T = int(input())

for t in range(1,T+1):

    N= int(input())

    N_list = list(map(int, input().split()))
    sum=0
    for i in range(len(N_list)):
        sum += N_list[i]

    avg = sum/ len(N_list)
    count = 0

    for i in range(len(N_list)):
        if N_list[i] <= avg:
            count+=1
    
    print(f'#{t} {count}')