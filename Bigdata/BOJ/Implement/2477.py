import sys
sys.stdin = open('input.txt','r')

n = int(input())

direc = [] # 방향 담을 리스트
length = [] # 길이 담을 리스트

for i in range(6):

    direction, leng = map(int, input().split())

    direc.append(direction)
    length.append(leng)


cnts =[0]*4 # 방향 갯수 세는 리스트
for j in range(6):
    cnts[direc[j]-1] +=1

a =[] # 가장 큰 값을 그리는 방향 담을 리스트

for k in range(4):
    if cnts[k] == 1:
        a.append(direc.index(k+1))

big = length[a[0]] * length[a[1]] # 가장 큰 사각형

small = length[(a[0]+3)%6] * length[(a[1]+3)%6] #가장 작은 사각형

num = (big - small) * n # (큰사 - 작사) * 갯수

print(num)
