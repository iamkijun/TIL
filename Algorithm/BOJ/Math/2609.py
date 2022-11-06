import sys
sys.stdin = open('Math/input.txt','r')

N, M = map(int,input().split())

def gcd(N,M):
    while M > 0:
        N, M = M, N % M
    return N

def lcm(N, M):
    return (N * M) // gcd(N,M)

print(gcd(N,M))
print(lcm(N,M))