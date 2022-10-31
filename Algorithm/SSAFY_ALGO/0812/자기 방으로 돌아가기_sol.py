import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for t in range(1,T+1):
    N= int(input())

    # 빈도수 표시
    cnts = [0] * 200
    ans = 0

    # M명에 대해 빈도수 표시
    for _ in range(N):
        S, E = map(int, input().split()) #start, end

        # S>E 인 경우에는 빈도수 표시가 안됨
        if S > E:
            S, E = E, S

        for i in range((S-1)//2, (E-1)//2 + 1):
            cnts[i] += 1


    #최대값 찾기
    for n in cnts:
        if ans<= n:
            ans = n



    print(f'#{t} {ans}')
