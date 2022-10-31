import sys
sys.stdin = open('input.txt','r')

T = int(input())

for t in range(1,T+1):

    N, M = map(int, input().split())

    # 피자 모음
    li = list(map(int, input().split()))


    #화덕q 선언, [1] q를 순서대로 채움
    q = []
    for i in range(N):
        q.append([i+1,li[i]]) #피자번호, 치즈의 양

    i+=1

    #[2] q가 not empty일 동안 무한루프
    while q:
        ans, piz = q[0][0], q[0][1] #피자번호, 치즈량
        q.pop(0)
        piz = piz//2

        if piz == 0: #꺼내야 하는 경우
            if i<M:
                q.append([i+1,li[i]//2]) #다음 피자로 교체
                i+=1

        else:        #맨 뒤에다 재투입(아직 안녹아서)
            q.append((ans,piz))

    print(f'#{t} {ans}')




    # [2] while