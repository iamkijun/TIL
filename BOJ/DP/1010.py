import sys
sys.stdin = open('DP/input.txt','r')

dp = [0] * 31
dp[0] = 1
for i in range(1,31):
    dp[i] = i * dp[i-1]

T = int(input())

for t in range(1,T+1):
    N, M = map(int, input().split())

    print(dp[M]//(dp[N]*dp[M-N]))