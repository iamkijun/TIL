from curses.ascii import isalpha
import sys
sys.stdin = open('Stack/input.txt','r')

N = int(input())

S = list(input())

num_list = [0] * N

for n in range(N):
    num = int(input())
    num_list[n] = num

stk = []

for val in S:
    if val.isalpha():
        stk.append(num_list[ord(val)-65])
    else:
        b = stk.pop()
        a = stk.pop()
        if val == '+':
            stk.append(a+b)
        elif val == '-':
            stk.append(a-b)
        elif val == '*':
            stk.append(a*b)
        elif val == '/':
            stk.append(a/b)

print(f'{stk[0]:.2f}')