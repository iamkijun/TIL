import sys
sys.stdin = open("Greedy/input.txt","r")

S= input()

val = ''
li = []
all_minus = 0
for i in range(len(S)):
    if S[i].isdigit():
        val += S[i]
    elif S[i] == '+':
        
        if all_minus:
            li.append(-1*int(val))
        else:
            li.append(int(val))
        val = ''
        
    elif S[i] == '-':
        if all_minus:
            li.append(-1*int(val))
        else:
            li.append(int(val))
            all_minus = 1
        val = ''

if all_minus:
    li.append(-1*int(val))
else:
    li.append(int(val))

print(sum(li))



