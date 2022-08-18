import sys
sys.stdin = open("input.txt","r")

T = int(input())

dct = {'(':')','{':'}'}
tbl = [')', '}']

for t in range(1,T+1):

    st = input()

    ans = 1
    stk = []

    for val in st:
        if val in dct: # val이 열리는 괄호인 경우
            stk.append(dct[val])
        elif val in tbl: #val이 닫히는 괄호인 경우
            if stk and val == stk.pop():
                pass
            else:
                ans = 0
                break
    if stk: #모든 괄호 비교 후 남은 괄호 체크
        ans = 0

    print(f'#{t} {ans}')

