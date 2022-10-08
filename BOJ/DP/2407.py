import sys
sys.stdin = open('DP/input.txt','r')

dp = [0] * 101

dp[1] = 1

for i in range(2,101):
    dp[i] = i * dp[i-1]

n, m = map(int, input().split())

print(dp[n]//(dp[m]*dp[n-m]))