import sys
sys.stdin = open("Graph/input.txt","r")

N = int(input())

for n in range(N):
    x, y, r = map(int,input().split())