import sys
input = sys.stdin.readline
# sys.stdin = open('Brute_Force/input.txt','r')

A,B,C,M = map(int, input().split())
now_stemina = 0
stacked_work = 0
for i in range(24):
    if now_stemina + A <= M:
        stacked_work += B
        now_stemina += A
    else:
        now_stemina -= C
        now_stemina = max(0,now_stemina)

print(stacked_work)