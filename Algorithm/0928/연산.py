from ast import operator
import sys
sys.stdin = open('0928/input.txt','r')

def operator():
    while q:
        c_num, cnt = q.pop(0)       #현재 숫자, 연산 횟수
        
        if c_num == M:
            return cnt

        #[3] 2곱하기
        if 1<= c_num *2 <=2*M and not visited[c_num*2]:
            q.append([c_num*2,cnt+1])
            visited[c_num*2] = 1
        
        #[1] 1더하기
        if 1<= c_num +1 <=2*M and not visited[c_num+1]:
            q.append([c_num+1,cnt+1])
            visited[c_num+1] = 1
        #[2] 1빼기
        if 1<= c_num -1 <=2*M and not visited[c_num-1]:
            q.append([c_num-1,cnt+1])
            visited[c_num-1] = 1
        
        #[4] 10빼기
        if 1<= c_num -10 <=2*M and not visited[c_num-10]:
            q.append([c_num-10,cnt+1])
            visited[c_num-10] = 1



T = int(input())

for t in range(1,T+1):
    
    N, M = map(int, input().split())

    visited = [0] * (2*M)

    q = []
    q.append([N,0])
    print(f'#{t} {operator()}')
