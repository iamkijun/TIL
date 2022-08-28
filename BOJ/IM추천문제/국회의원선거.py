import sys
sys.stdin = open('IM추천문제/input.txt','r')

N =int(input())
li = []
for _ in range(N):
    n = int(input())
    li.append(n)
cnt = 0
while True:
    if li[0] == max(li):
        if li.count(max(li)) == 1:
            break
        else:
            cnt+=1 
            break
    
    else:
        li[li.index(max(li))] -=1
        li[0] += 1
        cnt+=1

print(cnt)