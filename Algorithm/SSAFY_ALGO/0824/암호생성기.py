import sys
sys.stdin = open('input.txt','r')

for t in range(1,11):
    N = int(input())

    q = list(map(int, input().split()))
    
    cnt = 0 #싸이클을 돌릴 때 쓸 cnt 선언

    while True:
        #[1] 종료조건 : q[-1]이 0이하면 q[-1]을 0으로 바꾸고 종료
        if q[-1] <= 0:
            q[-1] = 0
            break
        
        #[2] 연산작업
        q.append(q.pop(0)-(cnt+1))

        cnt +=1
        
        #[3] 초기화 : 한 싸이클 돌때마다 cnt값 초기화
        if cnt == 5:
            cnt = 0

    print(f'#{N}',*q)