import sys
sys.stdin = open('input.txt','r')

icp = {'(':3, '*':2, '+':1} #incmoing priority
isp = {'(':0, '*':2, '+':1} #in stack priority

T = 10

for t in range(1,T+1):
    N = int(input())

    st = input()
    stk = []
    eq = ''

    for ch in st:
        if ch.isdigit():
            eq += ch

        else:
            # 무조건 스택에 즉시 push (icp는 가장 높아야)
            # '(' 스택에 저장된 경우,  isp는 가장 낮아야
            if ch == '(':
                stk.append(ch)
            # ')' => '('만날때까지 모두 꺼냄(계산기2에서 했던 하나의 식)
            elif ch == ')':
                while stk[-1]!='(':
                    eq += stk.pop()
                stk.pop()

            else:       #기타 연산자일 경우
                while stk and isp[stk[-1]] >= icp[ch]:
                    eq += stk.pop()
                stk.append(ch)

    while stk:
        eq += stk.pop()

    # [2] 후위표기식 계산
    for ch in eq:
        if ch.isdigit():
            stk.append(int(ch))
        else:
            try:
                b = stk.pop()
                a = stk.pop()
                if ch == '+':
                    stk.append(a+b)
                elif ch == '*':
                    stk.append(a*b)
            except:
                print('error')

    print(f'#{t} {stk[0]}')
