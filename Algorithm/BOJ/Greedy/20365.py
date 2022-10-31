import sys
sys.stdin = open("Greedy/input.txt","r")

N = int(input())

S = list(input())

turn = 1

B = 1
R = 1
if S[0] == 'B':
    B +=1
elif S[0] == 'R':
    R +=1

for i in range(1, N):
    if S[i-1] == 'B' and S[i] == 'R':
        R += 1

    elif  S[i-1] == 'R' and S[i] == 'B':
        B += 1

    if i>0 and S[i-1] != S[i]:
        turn +=1


print(min([turn,R,B]))