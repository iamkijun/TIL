import sys
sys.stdin = open('input.txt','r')

T = int(input())

def union_sum(A,N,K):
    global cnt
    cnt = 0 

    for i in range(0,(1<<12)):
        li = []
        for j in range(12):
            if i&(1<<j):
                li.append(A[j])
        if len(li) == N and sum(li) == K:
            cnt +=1
        
    return cnt

A = [x for x in range(1,13)]

for t in range(1,T+1):
    
    N, K = map(int, input().split())

    ans = union_sum(A,N,K)

    print(f'#{t} {ans}')