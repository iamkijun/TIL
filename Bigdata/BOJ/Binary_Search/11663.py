import sys
sys.stdin = open('Binary_Search/input.txt','r')

N, M = map(int, input().split())
li = list(map(int, input().split()))
li.sort()

def idx_binary(n):
    s=0
    e=N-1

    while s<=e:
        mid = (s+e)//2

        if mid <= n:
            e = mid - 1
        else:
            s = mid + 1

    return idx

for m in range(M):
    S, E =map(int, input().split())
    

