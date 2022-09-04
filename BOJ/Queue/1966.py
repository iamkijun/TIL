import sys
sys.stdin = open('Queue/input.txt','r')


T = int(input())

for t in range(1,T+1):

    N, M = map(int, input().split())

    queue = list(map(int, input().split()))

    idx = [x for x in range(N)]

    idx[M] = 'target'
    
    i = 0

    while True:
        if queue[0] == max(queue):
            i+=1
            if idx[0] == 'target':
                print(i)
                break
            else:
                queue.pop(0)
                idx.pop(0)
        else:
            queue.append(queue.pop(0))
            idx.append(idx.pop(0))

    