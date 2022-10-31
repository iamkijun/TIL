'''
3 5
1 2 4
2 3 4 5 6
'''

import sys
# input = sys.stdin.readline

sys.stdin = open('Data_Structure/input.txt')

A, B = map(int, input().split())

A_list = list(map(int, input().split()))
B_list = list(map(int, input().split()))

A_B = 0
B_A = 0

for a in A_list:
    if a not in B_list:
        A_B +=1
for b in B_list:
    if b not in A_list:
        B_A +=1

print(A_B + B_A)