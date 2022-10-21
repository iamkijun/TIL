import sys
sys.stdin = open("Graph/input.txt","r")

R, C, N = map(int, input().split())

arr =[list(input()) for _ in range(R)]

O_list= []

for i in range(R):
    for j in range(C):
        if arr[i][j] == 'O':
            O_list.append([i,j])

if N <= 0:
    for val in arr:
        print(''.join(val))

elif N % 2 == 0:
    for val in arr:
        print('O'*C)

elif N % 4 == 1:
    for val in arr:
        print(''.join(val))

elif N % 4 == 3:
    for ci,cj in O_list:
        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
            if 0<=ci+di<R and 0<=cj+dj<C and arr[ci+di][cj+dj] == '.':
                arr[ci+di][cj+dj] = 'O'

    for i in range(R):
        for j in range(C):
            if arr[i][j] == 'O':
                arr[i][j] = '.'
            elif arr[i][j] == '.':
                arr[i][j] = 'O'
    
    for val in arr:
        print(''.join(val))