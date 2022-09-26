import sys
sys.stdin = open("Graph/input.txt","r")

R, C = map(int, input().split())

arr = [['A']*(C+2)] +[['A'] +list(input())+ ['A'] for _ in range(R)] +[['A']*(C+2)]

di =[-1,1,0,0]
dj =[0,0,-1,1]

def escape(ci,cj,n):
    global cnt

    if c

    q =[]
    q.append([ci,cj])
    visited[ci][cj] == 1

    while q:
        ci, cj = q.pop(0)

        for dr in range(4):
            ni, nj = ci+di[dr], cj+dj[dr]

            if arr[ni][nj] == '.':
            


ci,cj,fi,fj = -1,-1,-1,-1

for i in range(1,R+1):
    if 'J' in arr[i]:
        ci = i
        cj = arr[i].index('J')

    if 'F' in arr[i]:
        fi = i
        fj = arr[i].index('F')

    if ci!=-1 and fi!=-1:
        break



visited = [[0] * (C+2) for _ in range(R+2)]
cnt = 0
escape(ci,cj,0)