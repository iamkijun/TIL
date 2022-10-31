import sys
# input = sys.stdin.readline
sys.stdin = open('Data_Structure/input.txt','r')

N, M = map(int, input().split())
dic_int = {}
dic_chr = {}
for i in range(N):
    monster = input().strip()
    dic_int[i] = monster
    dic_chr[monster] = i

for i in range(M):
    what = input().strip()
    if what.isdigit():
        print(dic_int[int(what)-1])
    else:
        print(dic_chr[what]+1)