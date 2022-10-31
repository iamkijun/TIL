import sys
sys.stdin = open('input.txt','r')

T = int(input())

le = 'abcdefghijklmnopqrstuvwxyz'

for t in range(1,T+1):
    S = input()
    cnt =0
    j = 0
    for i in range(len(S)):
        if le[j] == S[i]:   
            cnt +=1
            j+=1
        else:
            break
    
        
        

    print(f'#{t} {cnt}')