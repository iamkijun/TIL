import sys
# input = sys.stdin.readline
sys.stdin = open('Brute_Force/input.txt','r')

A = int(input())

T = int(input())

bdg = int(input())

n = 2 #현재 반복 횟수
bdg_num = 4
bdg_li = []
cnt = 0
while True:
    bdg_li += [0,1,0,1]+ [0]*n + [1]*n
    cnt += bdg_num//2
    if cnt < T:
        bdg_num += 1
        n+=1
    else:
        

print(bdg_li)



for i in range(len(bdg_li)):
    if bdg_li[i] == bdg:
        cnt += 1
        if cnt == T:
            print(i%A)
            break
