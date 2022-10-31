import sys
sys.stdin = open('input.txt')

T= int(input())

for t in range(1,T+1):

    N = int(input())

    li = list(map(int, input().split()))

    print(f'#{t} ')
    
    