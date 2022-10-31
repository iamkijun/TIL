import sys
sys.stdin = open('Brute_Force/input.txt','r')

N = int(input())

for n in range(N):
    num, strike, ball = map(int, input().split())
    