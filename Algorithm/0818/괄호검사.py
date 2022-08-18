import sys
sys.stdin = open("input.txt","r")

T = int(input())

def pop(s):
    stk = []  # 스택

    ans = 1

    for val in S:
        #열린 괄호는 stk에 누적
        if val == '(':
            stk.append('(')

        elif val == '{':
            stk.append('{')

        #닫힌 괄호는 stk가 원소를 가지며 마지막 원소와 짝이 많을때만 진행, 아니면 0
        elif val == ')':
            if stk and stk[-1] == '(':
                stk.pop(-1)
            else:
                ans = 0
                return ans

        elif val == '}':
            if stk and stk[-1] == '{':
                stk.pop(-1)
            else:
                ans = 0
                return ans

    # 열린 괄호가 남아있을 경우, 0
    if stk != []:
        ans = 0

    return ans

for t in range(1, T+1):

    S = input()

    result = pop(S)

    print(f'#{t} {result}')