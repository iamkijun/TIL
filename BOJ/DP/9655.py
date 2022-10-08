import sys
sys.stdin = open('DP/input.txt','r')

N = int(input())

if N % 2 == 0:
    print('CY')
else:
    print('SK')