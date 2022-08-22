from multiprocessing.connection import answer_challenge
import sys
sys.stdin = open('0822/input.txt','r')

T = int(input())

def f(i,N,s,t):         #s:부분집합의 합, t: 찾고자 하는 값
    global answer
    global cnt
    cnt += 1
    if i == N:
        if s == t:          #부분집합의 합이 t면
            answer += 1
        return
    elif s > t:
        return
    else:
        f(i+1,N, s+A[i], t)     #A[i]를 포함
        f(i+1,N, s, t)          #A[i]를 포함시키지 않음


for t in range(1,T+1):
    N, K = map(int, input().split())

    arr = list(map(int, input().split()))

    ans = 0

    for i in range(1<<N):
        total = 0
        for j in range(N):
            if i & (1<<j):
                total += arr[j] 
                
        if total == K:
            ans +=1

    print(f'#{t} {ans}')
