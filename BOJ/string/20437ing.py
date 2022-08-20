import sys
sys.stdin = open('input.txt','r')

T = int(input())

for t in range(1,T+1):
    W = list(input())
    K = int(input())
    
    for i in range(len(W)-K+1):
        W[i:i+K]