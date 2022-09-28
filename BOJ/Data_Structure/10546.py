'''
3
leo
kiki
eden
eden
kiki
'''

import sys
input = sys.stdin.readline

# sys.stdin = open('Data_Structure/input.txt')

N = int(input())

running = {}

for i in range(N):
    a = input()
    if a not in running:
        running[a] = 1
    else:
        running[a] += 1

for j in range(N-1):
    b = input()
    running[b] -=1

v_running = {v:k for k,v in running.items()}

print(v_running[1])
