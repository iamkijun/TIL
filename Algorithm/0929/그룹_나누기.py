import sys
sys.stdin = open('input.txt','r')

T = int(input())

for t in range(1,T+1):

    N, M = map(int, input().split())

    group = [[] for _ in range(N+1)]

    li = list(map(int,input().split()))

    for i in range(0,M*2,2):
        group[li[i]].append(li[i+1])
        group[li[i+1]].append(li[i])

    group_num = 0

    for i in range(1,N+1):
        q = group[i]
        while q:
            c = q.pop(0)
            q = 

    print(f'#{t}',group)