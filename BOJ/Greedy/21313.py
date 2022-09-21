import sys
sys.stdin = open("Greedy/input.txt","r")

N = int(input())

if N % 2 == 0:
    ans = [1,2] * (N//2)
elif N % 1 == 0:
    ans = [1,2] * (N//2) +[3]

print(*ans)