import sys
sys.stdin = open('Prefix_Sum/input.txt','r')

n = int(input())

li = list(map(int, input().split()))

prefix_sum = []

temp = 0
for i in range(n):
    temp += li[i]
    prefix_sum.append(temp)

ans = 0
for i in range(n):
    ans += li[i] * (prefix_sum[-1] - prefix_sum[i])

print(ans)