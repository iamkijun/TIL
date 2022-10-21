import sys
sys.stdin = open('DP/input.txt','r')

N = int(input())

li = list(map(int, input().split()))

dp = [0] * N
dp[0] = li[0]

for i in range(1,N):
    for j in range(i):
        if li[i] > li[j]:
            dp[i] = max(dp[i],dp[j]+li[i])
        else:
            dp[i] = max(dp[i], li[i])

print(max(dp))
print(li)
print(dp)

'''
10
1 100 2 50 60 3 5 6 7 8
'''