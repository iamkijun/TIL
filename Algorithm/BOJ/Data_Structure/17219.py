import sys

sys.stdin = open('Data_Structure/input.txt')

N, M = map(int, input().split())

sites = {}

for n in range(N):
    
    urls, pw = sys.stdin.readline().split()

    sites[urls] = pw

for m in range(M):
    site = sys.stdin.readline().rstrip()

    print(sites[site])