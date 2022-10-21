import sys
sys.stdin = open("Greedy/input.txt","r")
import copy

S = list(input())
S2 = copy.deepcopy(S)
change1 = 0
i = 0
#[0으로 만들기]
while True:
    
    if i == len(S):
        break
    elif S[i] == '1':
        S[i] = '0'
        change1 +=1
        i+=1
        if i == len(S):
            break
        while S[i] == '1':
            S[i] = '0'
            i+=1
            if i == len(S):
                break
    else:
        i+=1

change2 = 0
i = 0
#[0으로 만들기]
while True:
    
    if i == len(S2):
        break
    elif S2[i] == '0':
        S2[i] = '1'
        change2 +=1
        
        i+=1
        if i == len(S2):
            break
        while S2[i] == '0':
            S2[i] = '1'
            i+=1
            if i == len(S2):
                break
    else:
        i+=1



print(min(change1,change2))