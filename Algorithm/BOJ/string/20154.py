num = [3, 2, 1, 2, 3, 3, 3, 3, 1, 1, 3, 1, 3, 3, 1, 2, 2, 2, 1, 2, 1, 1, 2, 2, 2, 1]

S = input()
K = len(S)

S_num = [0] * (K+1)

for i in range(K):
    S_num[i] = num[ord(S[i]) - 65]

while S_num[1] != 0:
    for i in range(0,len(S_num),2):
        try:
            S_num[i//2] = S_num[i] + S_num[i+1]
            S_num[i+1] = 0
        except:
            pass
    S_num = S_num[:len(S_num)//2] + [0]

if S_num[0] % 2 == 1:
    print("I'm a winner!")
else:
    print("You're the winner?")