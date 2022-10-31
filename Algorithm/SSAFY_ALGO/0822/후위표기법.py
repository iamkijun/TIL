import sys
sys.stdin = open('0822/input.txt','r')

T = int(input())

for t in range(1,T+1):

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

    print(f'#{t}', end=' ')
    print(''.join(l))
