import sys
sys.stdin = open('IM추천문제/input.txt','r')

N, L = map(int, input().split())

total = 0 #총 시간

j = 0 #현재 위치

for i in range(N):
    
    D, R, G = map(int, input().split())
    
    s = 0 #걸리는 시간
    
    while j <= D:
        if j == D:
            if (total+s) % (R+G) < R: # 빨간불일 때
                wating = R - ((total+s) % (R+G))   # 대기시간 = 빨간불 전체 - 지금까지 켜져있던 시간
                s += wating
            else:
                j += 1
                s += 1
        elif j < D:
            j += 1
            s += 1
    
    total = total + s

total += (L-D-1)  #마지막 신호등에서 도로의 끝까지(j+=1했으므로 -1빼줘야 됨)

print(total)