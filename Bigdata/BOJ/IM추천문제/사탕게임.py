이거 어케품
import sys
sys.stdin = open('input.txt','r')

N = int(input())

arr =[list(map(str, input())) for _ in range(N)]

max_len = 0

count = 0
#[1] 행 비교
for i in range(N):
    for j in range(N):
        for di,dj in [[-1,0],[1,0],[0,-1],[0,1]]:
            if 0<= i+di < N and 0 <= j+dj < N:      # 상하좌우 값이 범위 안에 있을 때
                arr[i][j], arr[i+di][j+dj] = arr[i+di][j+dj], arr[i][j] #바꿔주기
                
                #행 비교
                lens = 0
                for k in range(N-j):
                    if len(set(arr[i][j:j+k])) == 1:
                        if k+1 > max_len:
                            max_len = k+1

                arr[i][j], arr[i+di][j+dj] = arr[i+di][j+dj], arr[i][j] #다시 원위치

#[2] 열 비교
for i in range(N):
    for j in range(N):
        if i<j:
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]

for i in range(N):
    for j in range(N):
        for di,dj in [[-1,0],[1,0],[0,-1],[0,1]]:
            if 0<= i+di < N and 0 <= j+dj < N:      # 상하좌우 값이 범위 안에 있을 때
                arr[i][j], arr[i+di][j+dj] = arr[i+di][j+dj], arr[i][j] #바꿔주기
                
                #행 비교
                lens = 0
                for k in range(N-j):
                    if len(set(arr[i][j:j+k])) == 1:
                        if k+1 > max_len:
                            max_len = k+1

                arr[i][j], arr[i+di][j+dj] = arr[i+di][j+dj], arr[i][j] #다시 원위치

print(max_len)