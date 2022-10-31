import sys
sys.stdin = open('input.txt','r')
'''
3
2 3
0 1 1
0 2 1
1 2 6
4 7
0 1 9
0 2 3
0 3 7
1 4 2
2 3 8
2 4 1
3 4 8
4 6
0 1 10
0 2 7
1 4 2
2 3 10
2 4 3
3 4 10
'''
INF = 10*1000
T = int(input())

def prim(s):
    mst = [0]*(V+1)
    mst[s] = 1
    cnt = 0

    for _ in range(V):        # 포함 안된 V-1개 노드 포함
        mn = INF
        i_min = 0
        # mst에 포함된 노드 찾으면, 포함 안된 모든 노드와의
        for s in range(V+1):
            if mst[s]==1:
                for e in range(V+1):
                    # e가 mst 미포함이고 더 짧은 경로면
                    if mst[e]==0 and mn>arr[s][e]:
                        mn = arr[s][e]
                        i_min = e
        mst[i_min] = 1
        cnt += mn
    return cnt


for t in range(1,1+T):
    V, E = map(int, input().split())
    arr = [[INF]*(V+1) for _ in range(V+1)]

    for i in range(E):
        n1, n2, w =map(int, input().split())
        arr[n1][n2] = w
        arr[n2][n1] = w

    ans = prim(0)
    print(f'#{t} {ans}')
