import sys
sys.stdin = open('input.txt','r')


T = int(input())

for t in range(1,T+1):
    N = int(input())
    ans = []
    k =''
    for i in range(N):
        s= input()
        if k:
            continue
        else:
            ans.append(s)
            for j in range(0,i):
                new = s + ans[j]
                if new == new[::-1]:
                    k = new
    if k:
        print(k)
    else:
        print(0)