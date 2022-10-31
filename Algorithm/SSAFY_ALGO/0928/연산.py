from ast import operator
import sys
sys.stdin = open('input.txt','r')

def operator(s,e):
    visited = [0] * 1000001
    q = [0]*1000000         #선형 큐를 만들어서 사용
    rd = 0
    wr = 0
    q[wr] = s
    wr +=1
    visited[s] = 1

    while q:
        # c_num = q.popleft()       #현재 숫자, 연산 횟수
        c = q[rd]
        rd +=1

        if c == e:
            return visited[c] - 1

        for n in [c+1,c-1,c*2,c-10]:
            if 1<=n <= 1000000 and not visited[n]:
                q[wr] = n
                wr += 1
                visited[n] = visited[c] + 1


T = int(input())

for t in range(1,T+1):
    
    N, M = map(int, input().split())

    ans = operator(N,M)

    print(f'#{t} {ans}')
