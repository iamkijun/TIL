import sys
sys.stdin = open('input.txt','r')

T = int(input())

for t in range(1,T+1):

    N, S = input().split()

    ans = []
    for val in S:
        if '0'<=val<='9':
            n = ord(val)-ord('0')
        else:
            n = ord(val)-ord('A')+10

        for i in range(3,-1,-1):
            ans.append(str((n>>i)&1))

    print(f'#{t}',''.join(ans))