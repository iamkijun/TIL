import sys
sys.stdin = open('input.txt','r')

def gwalho(arr):
    stk = []
    open_gwalho = ['(','[','{','<'] #열린 괄호 리스트
    close_gwalho = {')':'(',
                    ']':'[',
                    '}':'{',
                    '>':'<'}        #닫힌 괄호의 짝들을 딕셔너리 value로 저장

    for val in arr:
        if val in open_gwalho:      #열린 괄호일 때 무조건 저장
            stk.append(val)
        elif val in close_gwalho:   #닫힌 괄호일 때
            if stk.pop(-1) == close_gwalho[val]:    #스택의 마지막 원소가 val의 value값과 같을때 패스
                pass
            else:                                   #다르면 유효하지 않으므로 0을 리턴
                return 0
    
    return 1                        #for문을 종료 없이 돌았다는 것은 유효하다는 뜻이므로 1을 리턴


for t in range(1,11):
    li = list(map(str, input()))

    print(f'#{t} {gwalho(li)}')

