import sys
sys.stdin = open("input.txt","r")

T = int(input())

for t in range(1,T+1):

    S = list(input())

    i = 0

    while len(S) != i+1:
        if len(S) > 1: #S가 최소 두개의 문자로 이루어졌을 때 진행
            if S[i] == S[i+1]:
                S = S[:i] + S[i+2:] #같을 때 같은거 빼고 재정의

                if i ==0: #맨 앞자리일 경우 i를 그대로 진행,
                    i = 0
                else: # 중간일 경우 하나 빼서 다시 세기
                    i -= 1
            else: # i를 1씩 늘려나가면서 확인
                i += 1

        else: #S가 하나의 문자로만 이루어져있을 때
            break


    print(f'#{t} {len(S)}')