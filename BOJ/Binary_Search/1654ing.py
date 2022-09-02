import sys
sys.stdin = open('input.txt','r')

K, N = map(int, input().split())
li = []


for i in range(K):
    a= int(input())
    li.append(a)

def Binary(s,e,k)