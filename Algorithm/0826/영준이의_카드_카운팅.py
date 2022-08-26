import sys
sys.stdin = open('input.txt','r')

T = int(input())

for t in range(1,T+1):

    S = list(map(str, input()))
    new_S = []

    for i in range(0,len(S),3):
        new_S.append(S[i:i+3])

    SDHC = [13] * 4

    for i in range(len(new_S)):
        new_S[i]= new_S[i][0] +new_S[i][1] +new_S[i][2]

        if new_S[i][0] =='S':
            SDHC[0] -= 1
        elif new_S[i][0] =='D':
            SDHC[1] -= 1
        elif new_S[i][0] =='H':
            SDHC[2] -= 1
        elif new_S[i][0] =='C':
            SDHC[3] -= 1

    new_S.sort()

    set_new_S = set(new_S)  #세트로 (중복 찾기 위해)
    set_new_S = list(set_new_S) #다시 리스트로

    set_new_S.sort()

    if new_S != set_new_S:
        print(f'#{t} ERROR')
    else:
        print(f'#{t}', *SDHC)