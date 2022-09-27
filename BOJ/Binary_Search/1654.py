import sys
sys.stdin = open('Binary_Search/input.txt','r')

K, N = map(int, input().split())
li = []

for i in range(K):
    li.append(int(input()))

s= 1
e= max(li)

while s<=e:
    
    mid = (s+e)//2
    cnt = 0
    for val in li:
        cnt += (val//mid)
    
    if cnt >= N:
        s = mid + 1
    elif cnt < N:
        e = mid - 1

print(e)