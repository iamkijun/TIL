import sys
sys.stdin = open("Greedy/input.txt","r")

S = list(input())

idx = 0

ans = ''

if S == 'X':
    ans = '-1'
elif S == '.':
    ans = '.'

while idx < len(S):

    if S[idx] == 'X':
        cnt = 1
        while True:
            idx +=1
            if idx < len(S):
                if S[idx] == 'X':
                    cnt += 1
                elif S[idx] == '.':
                    break
            else:
                break

        if cnt % 2 == 1:
            ans = '-1'
            break

        else:
            if cnt % 4 == 0:
                ans += 'AAAA'*(cnt//4)
            elif cnt % 4 == 2:
                ans += 'AAAA'*(cnt//4) + 'BB'
            elif cnt == 2:
                ans += 'BB'

    else:
        ans += '.'
        idx +=1

print(ans)