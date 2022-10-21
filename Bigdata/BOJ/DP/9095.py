import sys
sys.stdin = open('DP/input.txt','r')

dp = [1,2,4]
for i in range(4,11):
    dp.append(sum(dp[-3:]))

for _ in range(int(input())):
    print(dp[int(input())-1])