import sys
sys.stdin = open("Graph/input.txt","r")

S = input()

max_ans = ''
min_ans = ''
i = 0
while i < len(S):
    if S[i] == 'K':
        min_ans += '5'
        i += 1

    elif S[i] == 'M':
        if 'K' in S[i:]:
            k_idx= S[i:].index('K')
            min_ans += str(10**(k_idx-1))
            i += k_idx

        elif 'K' not in S[i:]:
            min_ans += str(10**(len(S[i:])-1))
            break

while S:
    if 'K' in S:
        k_idx = S.index('K')
        max_ans += str(5 * 10**len(S[:k_idx]))
        S = S[k_idx+1:]
        
    elif 'K' not in S:
        max_ans += '1'*(len(S))
        S = ''


print(max_ans)
print(min_ans)