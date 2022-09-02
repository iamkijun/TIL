import sys
sys.stdin = open("input.txt","r")

input = sys.stdin.readline

T = int(input())

for t in range(1,T+1):

    N = int(input())

    li = list(map(int, input().split()))

    total = 0

    while True:
        if len(li) <= 1 or li== sorted(li,reverse=True):
            break 
        maxV = max(li)
        idx = li.index(maxV)

        zero_list= [0] * len(li)
        zero_list= [maxV] * idx

        total += sum(zero_list[:idx]) - sum(li[:idx])

        li = li[idx+1:]

    print(f'{total}')