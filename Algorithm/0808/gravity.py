import sys
sys.stdin = open("s_input.txt","r")

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    maxV = 0

    for i in range(N):
        count =0
        for j in range(i+1,N):
            if lst[i] > lst[j]:
                count+=1
        if count > maxV:
            maxV = count

    print(f"#{test_case} {maxV}")