import sys
sys.stdin = open('IM추천문제/input.txt','r')

T = int(input())

for t in range(1,T+1):
    tc, N = map(str, input().split())

    N = int(N)

    li = list(map(str, input().split()))

    # [1] str형 원소를 숫자로 변경

    str_to_num = {  "ZRO":0,
                    "ONE":1,
                    "TWO":2, 
                    "THR":3, 
                    "FOR":4, 
                    "FIV":5, 
                    "SIX":6, 
                    "SVN":7, 
                    "EGT":8, 
                    "NIN":9 }

    for i in range(N):
        li[i] = str_to_num[li[i]]
    
    # [2] 정렬

    #버블소트로 정렬
    # for i in range(N-1,0,-1):
    #     for j in range(i):
    #         if li[j] > li[j+1]:
    #             li[j], li[j+1] = li[j+1], li[j]
    
    #셀렉션소트로 정렬
    for i in range(N):
        minIdx = 0
        for j in range(i):
            

    # [3] 숫자를 str형으로 다시 변경

    num_to_str = {  '0':"ZRO",
                    '1':"ONE",
                    '2':"TWO",
                    '3':"THR",
                    '4':"FOR",
                    '5':"FIV",
                    '6':"SIX",
                    '7':"SVN",
                    '8':"EGT",
                    '9':"NIN"}
    
    for i in range(N):
        li[i] = num_to_str[str(li[i])]

    print(f'{tc}', end=" ")
    print(*li)
