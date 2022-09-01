import sys
sys.stdin = open('input.txt','r')

N = int(input())

Q = list(range(1,N+1))

while len(Q) != 1:
    Q.pop(0)
    Q.append(Q.pop(0))

print(*Q)