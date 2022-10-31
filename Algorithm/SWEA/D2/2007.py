import sys
sys.stdin = open("D2/input.txt","r")

T = int(input())

for t in range(1, T+1):
    n = input()
    maxV =0
    for j in range(10):
        for k in range(1,11):
            if n[j:j+k] == n[j+k:j+2*k]:
                for i in range(2,k):
                    if k % i ==0:
                        if n[j:j+i] == n[j+i:j+2*i]:
                            maxV = i
                            break
                else:
                    maxV = k
            
    
    print(f'#{t} {maxV}')