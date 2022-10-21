
T = int(input())

for t in range(1,T+1):
    S = list(input())
    print(S)
    count = 0
    
    if 'A' in S[0:]:
        count += 1
    else:
        print('Good')
        continue

    if 'F' in S[S.index('A')+1:]:
        count += 1
    else:
        print('Good')
        continue
    
    if 'C' in S[S[S.index('A')+1:].index('F')+1:]:
        count += 1
    else:
        print('Good')
        continue

    if len(S[S[S[S.index('A')+1:].index('F')+1:].index('C')+1:])==0:
        pass
    elif len(S[S[S[S.index('A')+1:].index('F')+1:].index('C')+1:])==1:
        if S[S[S[S.index('A')+1:].index('F')+1:].index('C')+1:] in ['A','B','C','D','E','F']:
            pass
        else:
            print('Good')
            continue
    else:
        print('Good')
        print(count)
        continue

    print(count)