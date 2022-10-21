import sys
sys.stdin = open('SAMSUNG/input.txt','r')

N = int(input())

dp = [0] * (N+2)

day = [0]
price = [0]

for _ in range(N):
    d, p = map(int,input().split())
    day.append(d)
    price.append(p)

# print(day)
# print(price)

for i in range(1, N+1):
    
    if dp[i] < dp[i-1]:
        dp[i] = dp[i-1]
    
    if i+day[i] <= N+1:
        
        if dp[i+day[i]] < dp[i] + price[i]:
            dp[i+day[i]] = dp[i] + price[i]
    
print(max(dp))
    