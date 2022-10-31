import sys
sys.stdin = open('Math/input.txt','r')

M, N = map(int, input().split())

for i in range(M,N+1):
    #예외 처리
    if i == 1:
        continue
    
    for j in range(2,int(i**0.5)+1):
        if i % j == 0:      # j가 i의 약수일 경우, 소수가 아니기 때문에
            break
    else:
        print(i)
