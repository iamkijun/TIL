import sys
sys.stdin = open('Binary_Search/input.txt','r')

N = int(input())
li = list(map(int, input().split()))
M = int(input())


s = 0
e = max(li)

while s <= e:
    total = 0
    mid = (s+e)//2

    for val in li:
        if val >= mid:
            total += mid
        else:
            total += val
    
    if total<= M:
        s = mid + 1
    else:
        e = mid -1

print(e)