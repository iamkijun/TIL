import sys
sys.stdin = open('DP/input.txt','r')

N = int(input())

li = list(map(int, input().split()))

dp = [-1000] * (N+1)
dp[0] = li[0]

for i in range(1,N+1):
    for j in range(i):
        if sum(li[j:i]) > dp[i]:
            dp[i] = sum(li[j:i])

print(max(dp))
