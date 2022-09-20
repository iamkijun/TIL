import sys
sys.stdin = open('D3/input.txt','r')

for t in range(1,11):
    N = int(input())

    li = list(map(int, input().split()))

    for i in range(2,N-2):
        