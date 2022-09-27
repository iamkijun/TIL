import sys
sys.stdin = open('Binary_Search/input.txt','r')

N = int(input())

s = 0
e = N-1

while s<=e:
    mid = (s+e) // 2
    if mid ** 2 < N:
        s = mid + 1
    else:
        e = mid - 1

print(s)