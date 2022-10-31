import sys
sys.stdin = open('Data_Structure/input.txt','r')

from collections import deque

T = int(input())

def bfs(si, sj):
    q = deque()
    q.append([si,sj])

    while q:
        
        ci, cj = q.popleft()

        if abs(ci-ei) + abs(cj-ej) <= 1000:
            print("happy")
            return
        
        for i in range(n):
            if not visited[i]:
                ni, nj = conv[i]

                if abs(ni-ci) + abs(nj-cj) <= 1000:
                    q.append([ni,nj])
                    visited[i] = 1

    print("sad")
    return


for t in range(T):

    n = int(input())

    #시작점
    si, sj = map(int, input().split())
    #편의점 위치
    conv = [list(map(int,input().split())) for _ in range(n)]
    #끝점
    ei, ej = map(int, input().split())

    #방문 위치
    visited = [0] * (n+1)

    bfs(si,sj)