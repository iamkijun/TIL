import sys
sys.stdin = open('input.txt','r')

pri = {'+':1, '*':2, '(':0}

for t in range(1,11):

    N = int(input())

    S = list(map(str,input()))

    stk = [] #빈 스택
    eq = [] #방정식

    # [1] 중위표기식 -> 후위표기식
    for i in range(N):
        if S[i].isdigit():
            eq.append(int(S[i]))
        elif S[i] == '(':
            stk.append('(')
        elif S[i] == ')':
            while stk[-1] != '(':
                eq.append(stk[-1])
                stk.pop(-1)
            stk.pop(-1)
        else:
            if not stk:
                stk.append(S[i])
            else:
                if pri[S[i]] > pri[stk[-1]]:
                    stk.append(S[i])
                else:
                    while stk and pri[S[i]] <= pri[stk[-1]]:
                        eq.append(stk[-1])
                        stk.pop(-1)
                    stk.append(S[i])

    # [2] 남은 연산자를 순서대로 pop, eq에 추가

    while stk:
        eq.append(stk[-1])
        stk.pop(-1)

    # [3] 계산하기

    stk = []
    a, b = 0, 0

    for i in range(len(eq)):
        if eq[i] == '*':
            b = stk.pop(-1)
            a = stk.pop(-1)
            stk.append(a*b)
        elif eq[i] == '+':
            b = stk.pop(-1)
            a = stk.pop(-1)
            stk.append(a + b)
        else:
            stk.append(eq[i])

    print(f'#{t} {stk[0]}')