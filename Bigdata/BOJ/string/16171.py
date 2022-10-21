S = input()

K = list(input())

new = []
for i in range(len(S)):
    if S[i].isupper():
        new.append(S[i])
    elif S[i].islower():
        new.append(S[i])
    else:
        pass

s = ''.join(new)
k = ''.join(K)

if k in s:
    print(1)
else:
    print(0)