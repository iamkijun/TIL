from functools import total_ordering
import sys
sys.stdin = open('input.txt','r')

N = int(input())

maxV = 0

def ssum(n):
    total = 0
    i = 0
    count = 0
    while True:
        total += i
        if total >n:
            break
        i += 1
        count +=1
    return count

print(ssum(N)-1)