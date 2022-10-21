import sys
sys.stdin = open('Binary_Search/input.txt','r')
# input = sys.stdin.readline

N, M = map(int,input().split())
N_li = []
for _ in range(N):
    N_li.append(int(input()))

N_li.sort()

def binary(n):
    s = 0
    e = N-1

    while s<=e:

        mid = (s+e)//2

        if N_li[mid] < n:
            s = mid +1

        elif N_li[mid] > n:
            e = mid -1

        elif N_li[mid] == n:
            if e == mid:
                break
            e = mid

    if N_li[mid] == n:
        return mid
    else:
        return -1

for _ in range(M):
    num = int(input())
    print(binary(num))