
import sys
sys.stdin = open('input.txt','r')

C, R = map(int, input().split())
K = int(input())

arr = [[-1]* (C+2)] + [[-1] + [0] * C + [-1] for _ in range(R)] + [[-1]* (C+2)]

di = [-1,0,1,0] #상->우->하->좌
dj = [0,1,0,-1]

i = R+1         #현위치 y좌표
j = 1           #현위치 x좌표

d= 0            #방향키 인덱스

si = di[d]
sj = dj[d]

num = 0 #초기값
iserror =0
while num < K:
    if num > C*R:
        iserror =1
        break

    if arr[i+si][j+sj] == 0: #이동할 수 있을 때,
        i = i+si
        j = j+sj
        num+=1
        arr[i][j] = num

    else:                    #이동할 수 없을 때,
        d = (d+1)%4
        si = di[d]
        sj = dj[d]
        i = i+si
        j = j+sj
        num+=1
        arr[i][j] = num

    if num == K:              #값을 찾았으니까 종료
        break
        
if iserror == 0:
    print(j,R-i+1) #x,y
else:
    print(0)
