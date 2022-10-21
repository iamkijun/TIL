import sys
sys.stdin = open('Implement/input.txt','r')


M = int(sys.stdin.readline())

S = set()

for _ in range(M):
    li = list(sys.stdin.readline().strip().split())

    if len(li) == 2:
        N = int(li[1])


        if li[0] == 'add':
            S.add(N)
        
        elif li[0] == 'check':
            if N in S:
                print(1)
            else:
                print(0)
        
        elif li[0] == 'remove':
            if N in S:
                S.remove(N)
        
        elif li[0] == 'toggle':
            if N in S:
                S.remove(N)
            else:
                S.add(N)
    else:
        if li[0] == 'all':
            S = set([x for x in range(1,21)])

        elif li[0] == 'empty':
            S = set()
