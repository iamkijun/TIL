import sys
sys.stdin = open('input.txt','r')

pri ={'+' : 1, '*' : 2} #우선순위 설정

for t in range(1,11):
    N = int(input())
    S = input()

    eq = '' #방정식
    stk = [] # 빈 스택

    # [1] 중위표기식 -> 후위표기식
    for ch in S:
        if ch.isdigit(): #숫자인 경우: eq에 추가
            eq += ch
        else:            #연산자인 경우
            if not stk:
                stk.append(ch)
            else:
                if pri[ch] > pri[stk[-1]]:
                    stk.append(ch)
                else:
                    while stk and pri[ch] <= pri[stk[-1]]:
                        eq += stk[-1]
                        stk.pop(-1)
                    stk.append(ch)

    # [2] 남은 연산자를 순서대로 pop, eq에 추가

    while stk:
        eq += stk[-1]
        stk.pop(-1)

    stk = []
    a, b = 0, 0

    for val in eq:
        if val.isdigit():
            stk.append(val)

        elif val == '*':
            a = stk.pop(-1)
            b = stk.pop(-1)
            stk.append(int(a)*int(b))

        elif val == '+':
            a = stk.pop(-1)
            b = stk.pop(-1)
            stk.append(int(a)+int(b))

    print(f'#{t} {stk[0]}')