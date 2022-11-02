s = "()()"

def solution(s):
    answer = True
    stk = []
    for val in s:

        if val == '(':
            stk.append(val)

        elif val == ')':

            if not stk:
                answer =False
                break
            
            else:
                if stk[-1] == '(':
                    stk.pop(-1)
                elif stk[-1] == ')':
                    answer =False
                    break

    if stk:
        answer = False

    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    return True

print(solution(s))