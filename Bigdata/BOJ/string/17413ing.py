import sys
sys.stdin = open('input.txt','r')

S = list(input())

new_S = []
stk = []

for i in range(len(S)):
    if S[i] == '<':
        idx_s = i
        stk.append('<')
    elif S[i] == '>':
        idx_e = i
        stk.pop(-1)
        new_S.append(''.join(S[idx_s:idx_e+1]))
    
print(new_S)