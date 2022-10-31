import sys
sys.stdin = open('input.txt','r')

tbl = [0,2,3,1]
def solve(s,e): #start~end의 최종 승리자의 index return 함수
    # [1] 종료조건
    if s == e:
        return s

    # [2] 하부호출, 단위작업: 2등분 해서 각각의 승자를 구하고 최종 승자 구하는 방식
    a = solve(s, (s+e)//2)          #왼쪽 승자
    b = solve((s+e)//2+1, e)        #오른쪽 승자

    if li[a] % 3 + 1 == li[b]:       #b가 이긴 경우
        return b
    else:                           #비기거나 a가 이긴 경우 a가 승자
        return a


T = int(input())

for t in range(1,T+1):

    N = int(input())

    li= [0]+ list(map(int, input().split()))

    ans= solve(1,N) # 1~N 사이의 최종 승리자의 index를 return 해주는 함수

    print(f'#{t} {ans}')

