import sys
sys.stdin = open('input.txt','r')

T = int(input())

for t in range(1,T+1):

    N, M, K = map(int, input().split())

    N_list = list(map(int, input().split()))