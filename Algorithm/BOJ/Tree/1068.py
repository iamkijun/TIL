import sys
sys.stdin = open('Tree/input.txt','r')

N = int(input())

li = list(map(int, input().split()))

K = int(input())

cnt = 0

def dfs(k, arr):
    arr[k] = -2
    for i in range(len(arr)):
        if k == arr[i]:
            dfs(i, arr)

dfs(K,li)
cnt = 0
for i in range(len(li)):
    if li[i] != -2 and i not in li:
        cnt +=1

print(cnt)