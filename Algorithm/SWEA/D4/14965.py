import sys
sys.stdin = open("D4/input.txt")

T = int(input())
for t in range(1, T+1):

    N = int(input())
    arr = []

    for _ in range(N):
        li = list(map(int, input().split()))
        arr.append(li)
    



    print(f'#{t} ')