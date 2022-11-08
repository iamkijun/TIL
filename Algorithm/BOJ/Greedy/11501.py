import sys
sys.stdin = open("Greedy/input.txt","r")

input = sys.stdin.readline

T = int(input())

for t in range(1,T+1):

    N = int(input())

    li = list(map(int, input().split()))

    total = 0

    mx = li[-1]
    
    for i in range(N-2,-1,-1):
        if li[i] > mx:     #오늘 가격이 mx보다 크다면
            mx =li[i]
        else:
            total += mx-li[i]

    print(total)
