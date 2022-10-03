import sys
sys.stdin = open("Backtracking/input.txt","r")

L, C = map(int ,input().split())

li = list(input().split())
li.sort()

need  = ['a','e','i','o','u']

def permutation(li,L,C):
    result = []
    if L == 0:
        return [[]]

    for i in range(C):
        # if li[i] in need:
        element= li[i]

        for rest in permutation(li[:i]+li[i+1:],L-1,C-1):
            result.append([element]+rest)

    result.sort()
    
    return result

ans = permutation(li,L,C)
distinct = []

for val in ans:
    mo = 0
    ja = 0
    for val2 in val:
        if val2 in need:
            mo +=1
        elif val2 not in need:
            ja +=1
    
    if mo>=1 and ja>=2 and set(val) not in distinct:
        print(''.join(val))
        distinct.append(set(val))
