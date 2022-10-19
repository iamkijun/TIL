import sys
sys.stdin = open('DP/input.txt','r')

dp = [0,1,1,1,2,2]

for i in range(6,101):
    dp.append(dp[i-3]+dp[i-2])


T = int(input())

for t in range(T):
    N =int(input())

    print(dp[N])