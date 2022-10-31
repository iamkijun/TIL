import sys
sys.stdin = open("D3/input.txt")

T = int(input())

for t in range(1,T+1):

    S = input()
    s_list=[]
    for i in range(len(S)):
        if S[i] == 'a' or S[i] == 'e' or S[i] == 'i' or S[i] == 'o' or S[i] == 'u':
            pass
        else:
            s_list.append(S[i])
    print(f'#{t}',end=" ")
    print(''.join(s_list))