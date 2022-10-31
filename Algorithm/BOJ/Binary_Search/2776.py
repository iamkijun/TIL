import sys
sys.stdin = open('Binary_Search/input.txt','r')

T = int(input())

def binary(n):
    s = 0
    e = N-1

    while s <= e:
        mid = (s+e)//2

        if N_li[mid] < n:
            s = mid + 1
        elif N_li[mid] > n:
            e = mid - 1
        elif N_li[mid] == n:
            return 1

    return 0


for t in range(T):
    N = int(input())
    N_li = list(map(int, input().split()))
    N_li.sort()

    M = int(input())
    M_li = list(map(int, input().split()))

    for val in M_li:
        print(binary(val))
