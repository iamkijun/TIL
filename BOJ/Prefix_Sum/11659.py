import sys

sys.stdin = open('Prefix_Sum/input.txt','r')

N, M = map(int, input().split())

li = [0] + list(map(int,input().split()))

prefix_sum = []

temp = 0
for i in li:
    temp += i
    prefix_sum.append(temp)

for m in range(M):
    s, e = map(int, input().split())
    print(prefix_sum[e] - prefix_sum[s-1])
# print(li)
# print(prefix_sum)