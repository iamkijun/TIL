import sys
sys.stdin = open("Backtracking/input.txt","r")

N = int(input())

N_list = [x for x in range(1,N+1)]

def permutation(N_list, N):
    result = []

    if N == 0:
        return [[]]

    for i in range(N):
        element = N_list[i]
        for rest in permutation(N_list[:i]+N_list[i+1:], N-1):
            result.append([element]+rest)
    
    return result

ans= permutation(N_list, N)

for val in ans:
    print(*val)