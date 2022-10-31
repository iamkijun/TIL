import sys
sys.stdin = open("Greedy/input.txt","r")

N = int(input())

X = []

total_num = 0

for i in range(N):
    a, a_num = map(int,input().split())
    total_num += a_num
    X.append([a,a_num])

X = sorted(X, key = lambda i: i[0])

stacked_num = 0
for j in range(N):
    stacked_num += X[j][1]
    if stacked_num >= total_num/2:
        print(X[j][0])
        break