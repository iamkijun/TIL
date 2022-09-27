import sys
sys.stdin = open('Binary_Search/input.txt','r')

N, M = map(int, input().split())

li = list(map(int, input().split()))

s = 1
e = max(li)

while s<=e:
    mid = (s+e)//2

    cnt = 0

    for i in range(len(li)):
        if li[i] > mid:
            cnt += (li[i]-mid)
    
    if cnt >= M:
        s = mid + 1
    else:
        e = mid - 1

print(e)