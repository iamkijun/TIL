import sys
sys.stdin = open('input.txt','r')

T = int(input())

for t in range(1,T+1):

    N, K = map(int,input().split())

    N_list = []
    for n in range(1,N+1):
        N_list.append(n)

    K_list = list(map(int, input().split()))

    for k in range(K):
        N_list.remove(K_list[k])


    print(f'#{t}',*N_list)