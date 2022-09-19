import sys
sys.stdin = open('input.txt','r')

T = int(input())

for t in range(1,T+1):
    S = str(input())

    print(f'#{t}',end=" ")

    for i in range(len(S)//7):
        li = S[7*i:7*i+7]
        ans = 0
        for j in range(7):
            if li[j] == '1':
                ans += 2**(6-j)
        
        print(ans, end=" ")
    
    print()

