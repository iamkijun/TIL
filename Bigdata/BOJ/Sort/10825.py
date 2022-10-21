import sys
sys.stdin = open('Sort/input.txt','r')

N = int(input())

ans = []

for _ in range(N):
    li = list(input().split())
    
    li[1] = int(li[1])
    li[2] = int(li[2])
    li[3] = int(li[3])

    ans.append(li)

ans.sort(key = lambda x:((-x[1]),x[2],(-x[3]),x[0]))

for val in ans:
    print(val[0])