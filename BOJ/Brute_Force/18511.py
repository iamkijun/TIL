import sys
sys.stdin = open('Brute_Force/input.txt','r')

N, K = map(int, input().split())

K_li = list(map(int, input().split()))
K_li.sort(reverse=True)

ans = 0

for i in range(len(str(N))-1,-1,-1):  #3
    for val in K_li:
        if val * (10**i) <= N:
            ans += val * (10**i)
            break

print(ans)