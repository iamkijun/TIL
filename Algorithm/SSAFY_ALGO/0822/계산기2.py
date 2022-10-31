import sys
sys.stdin = open('0822/input.txt','r')

for t in range(1,11):
    
    N = int(input())
    S = list(input())


    num = ['0','1','2','3','4','5','6','7','8','9']
    
    l = []     #최종 리스트
    stk = []    #연산자 저장하는 리스트

    pri =  { 
            '+':1,
            '*':2
            }           #우선순위 딕셔너리로 만들기

    for i in range(len(S)):

        if S[i] in num:
            l.append(S[i])           #숫자면 최종 리스트에 차곡차곡 넣기

        else:
            while stk and pri[S[i]] <= pri[stk[-1]]: #리스트가 존재하고, 우선순위가 stk 마지막 원소와 같거나 낮을 경우
                l.append(stk.pop())                  #stk에서 빼서 최종 리스트에 저장
                
            stk.append(S[i])
    
    for j in range(len(stk)):   # stk에 남아있는 원소들 처리
        l.append(stk.pop())
    
    # 위에 식을 통해 l을 후위 표기법으로 나타낸 리스트로 만듬-------------------------------------------

    # 아래식은 계산식--------------------------------------------------------------------------

    a = 0 #계산할때 쓸거 변수 선언 1
    b = 0 #계산할때 쓸거 변수 선언 2
    stack=[] #계산할 때 쓸 숫자 담아둘 스택 선언
    
    for val in l:
        if val in num:
            stack.append(int(val)) #숫자일 경우, stack에 차곡차곡

        elif val == '*':
            a = stack.pop()
            b = stack.pop()
            stack.append(a*b) #곱셈 연산자일 경우, stack에서 두개 뽑아서 곱한 값을 다시 넣어주기

        elif val == '+':
            a = stack.pop()
            b = stack.pop()
            stack.append(a+b) #덧셈 연사자일 경우, stack에서 두개 뽑아서 더한 값을 다시 넣어주기

    print(f'#{t} {stack[0]}')