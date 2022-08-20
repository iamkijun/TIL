import sys
sys.stdin = open('input.txt','r')

S= list(input())

while S != 0:
    if S[:2] == ['p','i']:
        S = S[2:]

    elif S[:2] == ['k','a']:
        S = S[2:]
    
    elif S[:3] == ['c','h','u']:
        S = S[3:]

    else:
        break

if len(S) == 0:
    print("YES")
else:
    print("NO")