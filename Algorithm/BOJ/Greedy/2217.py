import sys
sys.stdin = open("Greedy/input.txt","r")

N = int(input())
li = [0] * N
for i in range(N):
    li[i] = int(input())

li.sort(reverse=True)

ans = [0] * N
for i in range(N):
    ans[i] = li[i]*(i+1)

print(max(ans))