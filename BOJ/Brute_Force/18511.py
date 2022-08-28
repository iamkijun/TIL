import sys
from uuid import NAMESPACE_X500
sys.stdin = open('input.txt','r')

N, K = map(int, input().split())

li = list(map(int, input().split()))

def backtrack(a,k,input):
    global MAXCANDIDATES
    bit = [0] * MAXCANDIDATES
    
    if k == input :
        for i in range(1, k+1):
            print(a[i], end=" ")
        print()
    else:
        k += 1
        ncandidates = construct_candidateds(a, k, input, c)
        for i in range(ncandidates):
            a[k] = c[i]
            backtrack(a, k, input)

def construct_candidates(a, k, input, c):
    in_perm = [False] * NMAX

    for i in range(1, k):
        in_perm[a[i]] == True

    ncandidates = 0
    for i in range(1, input+1):
        if in_perm[i] == False:
            c[ncandidates] = i
            ncandidates += 1
    return ncandidates

print()